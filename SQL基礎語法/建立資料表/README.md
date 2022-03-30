## 建立資料表
### sqlite的資料類型

- MySQL 和 PostgreSQL 使用的是靜態型別
- SQLite使用的是動態型別, 代表是由儲存格的值決定該欄位型別
- SQLite定義5種型別定義當作未來取出值時,變數該定義為何種型別

| 類型 | 說明 |
|:--|:--|
| NULL | 空的或不知道的資料 |
| INTEGER | 正整數或負整數 |
| REAL | 浮點數 |
| TEXT |  文字 |
| BLOB | binary資料，如照片或影片 |

> sqlite 沒有支援日期和時間型別,是使用TEXT,INT,REAL儲存日期和時間值
> 

```sql
SELECT
	typeof(100),
	typeof(10.0),
	typeof('100'),
	typeof(x'1000'),
	typeof(NULL)

```


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