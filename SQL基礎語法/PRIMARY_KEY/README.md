## PRIMARY KEY
- 整個資料表的識別欄位
- 使用PRIMARY,NOT NULL就自動產生

### 建立一個primary key語法

```
CREATE TABLE table_name(
   column_1 INTEGER NOT NULL PRIMARY KEY,
   ...
);
```

### 建立多個primary key 語法

```
CREATE TABLE table_name(
   column_1 INTEGER NOT NULL,
   column_2 INTEGER NOT NULL,
   ...
   PRIMARY KEY(column_1,column_2,...)
);
```

### rowid自動產生,語法:
- primary key 資料類型設為 INTEGER,rowid自動產生,一定只可以是(INTEGER)

```
CREATE TABLE table(
   pk INTEGER PRIMARY KEY,
   ...
);
```

### 不要rowid自動產生,語法:

- DESC

```
CREATE TABLE table(
   pk INTEGER PRIMARY KEY DESC,
   ...
);
```


### 範例:

```sql
CREATE TABLE countries (
   country_id INTEGER PRIMARY KEY,
   name TEXT NOT NULL
);
```

```sql
INSERT INTO countries (name)
VALUES('台灣')
```

```sql
CREATE TABLE languages (
   language_id INTEGER,
   name TEXT NOT NULL,
   PRIMARY KEY (language_id)
);
```

```sql
INSERT INTO languages (name)
VALUES('繁體中文');

```
