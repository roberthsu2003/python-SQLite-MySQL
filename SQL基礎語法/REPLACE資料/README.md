## REPLACE操作
### 語法

- 先刪除原來的資料
- 再新增新的資料

```
REPLACE INTO table(column_list)
VALUES(value_list);
```

### REPLACE範例

- 只有欄位是PRIMARY KEY or UNIQUE 才可以使用REPLACE語法

#### 建立一個新資料表positions

```

CREATE TABLE IF NOT EXISTS positions (
	id INTEGER PRIMARY KEY,
	title TEXT NOT NULL,
	min_salary NUMERIC,
	UNIQUE(title)
);
```

#### 新增多筆資料

```
INSERT INTO positions (title, min_salary)
VALUES ('DBA', 120000),
       ('Developer', 100000),
       ('Architect', 150000);
```

#### 檢查資料

```
SELECT * FROM positions;
```

#### 新增沒有重覆的資料

```
REPLACE INTO positions (title, min_salary)
VALUES('Full Stack Developer', 140000);
```

#### 新增重覆的資料

```
REPLACE INTO positions (title, min_salary)
VALUES('DBA', 170000);
```
