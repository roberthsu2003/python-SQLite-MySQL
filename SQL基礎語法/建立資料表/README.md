## 建立資料表
### sqlite的資料類型

| 類型 | 說明 |
|:--|:--|
| NULL | 空的或不知道的資料 |
| INTEGER | 正整數或負整數 |
| REAL | 浮點數 |
| TEXT |  文字 |
| BLOB | binary資料，如照片或影片 |

### 語法:
#### 限制的關鍵字:
- IF NOT EXITS
- PRIMARY
- NOT NULL
- DEFAULT 
- WITHOUT ROWID
- UNIQUE

```
CREATE TABLE [IF NOT EXISTS] [schema_name].table_name (
		column_1 data_type PRIMARY KEY,
		column_2 data_type NOT NULL,
		column_3 data_type DEFAULT 0,
		table_constraints
) [WITHOUT ROWID];
```

### 範例:

```
CREATE TABLE IF NOT EXISTS contacts (
	contact_id INTEGER PRIMARY KEY,
	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL,
	email TEXT NOT NULL UNIQUE,
	phone TEXT NOT NULL UNIQUE
);
```