## 使用dvd_rental資料庫練習
### ORDER BY 語法

```sql
SELECT 
  select_list 
FROM 
  table_name 
ORDER BY 
  sort_expression1 [ASC | DESC], 
  sort_expression2 [ASC | DESC],
  ...;
```

#### - 取出客戶的first_name,last_name,first_name必需由小到大排序

```sql
SELECT first_name, last_name
FROM customer
ORDER BY first_name ASC;
```

#### - 取出客戶的first_name,last_name,first_name必需由小到大排序(預設排序)

```sql
SELECT first_name, last_name
FROM customer
ORDER BY first_name;
```

#### - 取出客戶的first_name,last_name,last_name必需由大到小排序

```sql
SELECT first_name, last_name
FROM customer
ORDER BY last_name DESC;
```

#### - 取出客戶的first_name,last_name
- fast_name必需由小到大排序
- last_name必需由大到小排序

```sql
SELECT first_name, last_name
FROM customer
ORDER BY first_name ASC,last_name DESC;
```

### - 取出first_name,和first_name的字串長度(len)
- 依據長度(len)由大到小排序


```sql
/*LENGTH() 可以傳出字串長度*/
SELECT first_name,LENGTH(first_name) len
FROM customer
ORDER BY len DESC
```

