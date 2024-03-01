## 使用dvd_rental資料庫練習
### SELECT DISTINCT語法
- 重覆的資料只輸出一筆

```sql
SELECT 
  DISTINCT column1 
FROM 
  table_name;
```

### 建立 distinct_demo table

```sql
CREATE TABLE distinct_demo(
	id SERIAL NOT NULL PRIMARY KEY,
	bcolor VARCHAR,
	fcolor VARCHAR
);
```

### 加入資料

```sql
INSERT INTO distinct_demo(bcolor, fcolor)
VALUES
('red', 'red'), 
('red', 'red'), 
('red', NULL), 
(NULL, 'red'), 
('red', 'green'), 
('red', 'blue'), 
('green', 'red'), 
('green', 'blue'), 
('green', 'green'), 
('blue', 'red'), 
('blue', 'green'), 
('blue', 'blue');
```

### 重覆的資料只出現1筆

```sql
SELECT DISTINCT bcolor
FROM distinct_demo
```

### NULL資料顯示在最後

```sql
SELECT 
  DISTINCT bcolor 
FROM 
  distinct_demo 
ORDER BY 
  bcolor;
```


