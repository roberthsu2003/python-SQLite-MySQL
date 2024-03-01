## 練習建立資料表

- 使用city.csv檔
- 使用employees.csv檔
- 使用invoices.csv檔
- 使用artists.csv檔

###  建立city資料表
- 使用city.csv檔
- 建立id,primary key

```sql
CREATE TABLE IF NOT EXISTS city(
	id SERIAL PRIMARY KEY,
	name VARCHAR(30),
	population INT
);
```



