## foreign key

- 強制設定2個資料表欄位的關係

### 檢查sqlite版植是否支援 foregin key

```
PRAGMA foreign_keys;
```

### 開啟關閉foreign key

```
PRAGMA foreign_keys = ON;
PRAGMA foreign_keys = OFF;
```
---

### 建立2個沒有關係的資料表(範例)

- suppliers內的group_id要對應到supplier_groups的group_id
- 目前沒有foreign key的限制, 所以2個欄位的值沒有任何的限制
- 現在無法預防建立suppliers資料,欄位group_id的值是supplier_groups內有提供
- 現在無法限制當supplier_groups內的值被刪除或更改時,suppliers內的group_id要如何處理

```
CREATE TABLE suppliers (
	supplier_id integer PRIMARY KEY,
	supplier_name text NOT NULL,
	group_id integer NOT NULL
);

CREATE TABLE supplier_groups (
	group_id integer PRIMARY KEY,
	group_name text NOT NULL
);
```

### 使用foreign key限制2個欄位是有關係的

- sqlite建立表格後，無法再建立foreign key
- 建立限制後,無法在child key增加沒有parent key存在的值
- 建立限制後,無法刪除parent key(當child key內有此parent key的值)

![](./images/pic3.png)

```
DROP TABLE suppliers;

CREATE TABLE suppliers (
    supplier_id   INTEGER PRIMARY KEY,
    supplier_name TEXT    NOT NULL,
    group_id      INTEGER NOT NULL,
    FOREIGN KEY (group_id)
       REFERENCES supplier_groups (group_id) 
);
```

### 增加資料

```
INSERT INTO supplier_groups (group_name)
VALUES
   ('Domestic'),
   ('Global'),
   ('One-Time');
```

- 不會出錯，group_id 2有出現在 supplier_groups->group_id

```
INSERT INTO suppliers (supplier_name, group_id)
VALUES ('HP', 2);
```


- 會出錯，group_id 4沒有出現在 supplier_groups->group_id

```
INSERT INTO suppliers (supplier_name, group_id)
VALUES('ABC Inc.', 4);
```

### foreign key限定行為

```
FOREIGN KEY (foreign_key_columns)
   REFERENCES parent_table(parent_key_columns)
      ON UPDATE action 
      ON DELETE action;
```

| foreign key action |
|:--|
| SET NULL |
| SET DEFAULT |
| RESTRICT |
| NO ACTION |
| CASCADE |

#### SET NULL

- 父_table資料被刪,子_tabel的欄位被設為NULL

```
DROP TABLE suppliers;

CREATE TABLE suppliers (
    supplier_id   INTEGER PRIMARY KEY,
    supplier_name TEXT    NOT NULL,
    group_id      INTEGER,
    FOREIGN KEY (group_id)
    REFERENCES supplier_groups (group_id) 
       ON UPDATE SET NULL
       ON DELETE SET NULL
);

```

- 新增2筆記錄
```
INSERT INTO suppliers (supplier_name, group_id)
VALUES('XYZ Corp', 3);

INSERT INTO suppliers (supplier_name, group_id)
VALUES('ABC Corp', 3);
```

- 刪除父類別記錄，檢查欄位是否變為NULL

```
DELETE FROM supplier_groups 
WHERE group_id = 3;
```

```
SELECT * FROM suppliers;
```

#### SET DEFAULT

- 欄位如果有default值,就會變成default值
- 欄位如果沒有default值,就會變成NULL值

#### RESTRICT

- 不允許改變父table的欄位值

```
DROP TABLE suppliers;

CREATE TABLE suppliers (
    supplier_id   INTEGER PRIMARY KEY,
    supplier_name TEXT    NOT NULL,
    group_id      INTEGER,
    FOREIGN KEY (group_id)
    REFERENCES supplier_groups (group_id) 
       ON UPDATE RESTRICT
       ON DELETE RESTRICT
);
```

```
INSERT INTO suppliers (supplier_name, group_id)
VALUES('XYZ Corp', 1);
```

- 刪除父table資料會出錯

```
DELETE FROM supplier_groups 
WHERE group_id = 1;
```

- 如果一定要刪除,必需先把child_table有的記錄先全部刪除，才可以刪除parent_table的記錄

```
DELETE FROM suppliers 
WHERE group_id =1;
```

```
DELETE FROM supplier_groups 
WHERE group_id = 1;
```


#### NO ACTION

 - 動作相同於RESTRICT

#### CASCADE

-  parent_table刪除,child_table就一起刪除
-  parent_table更新,child_table就一起更新

```
INSERT INTO supplier_groups (group_name)
VALUES
   ('Domestic'),
   ('Global'),
   ('One-Time');
```

```
DROP TABLE suppliers;

CREATE TABLE suppliers (
    supplier_id   INTEGER PRIMARY KEY,
    supplier_name TEXT    NOT NULL,
    group_id      INTEGER,
    FOREIGN KEY (group_id)
    REFERENCES supplier_groups (group_id) 
       ON UPDATE CASCADE
       ON DELETE CASCADE
);
```

```
INSERT INTO suppliers (supplier_name, group_id)
VALUES('XYZ Corp', 3);

INSERT INTO suppliers (supplier_name, group_id)
VALUES('ABC Corp', 4);
```

- 更新parent_table值
```
UPDATE supplier_groups
SET group_id = 100
WHERE group_name = 'Domestic';
```

```
SELECT * FROM suppliers;
```

- 刪除parent_table值

```
DELETE FROM supplier_groups 
WHERE group_id = 4;
```

```
SELECT * FROM suppliers;
```

