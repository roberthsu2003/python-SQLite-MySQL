## 練習WHERE 語法

### 使用dvd_rental範例資料庫

![](./images/pic1.png)

### WHERE和=

- first_name為Jamie

```sql
SELECT last_name, first_name
FROM customer
WHERE first_name = 'Jamie'
```

### WHERE 和 AND
- first_name是Jamie,同時last_name是Rice

```sql
SELECT last_name, first_name
FROM customer
WHERE first_name = 'Jamie' AND last_name = 'Rice'
```

### WHERE 和 OR

- last_name是Rodriquez 或者 first_name是Adam

```sql
SELECT first_name, last_name
FROM customer
WHERE last_name = 'Rodriquez' OR first_name = 'Adam'
```

### WHERE 和 IN

- 取出first_name是Ann,Anne,Annie

```sql
SELECT first_name, last_name
FROM customer
WHERE first_name IN ('Ann','Anne','Annie')
```

### WHERE 和 LIKE

- 取出字串開頭是Ann的first_name

```sql
SELECT first_name, last_name
FROM customer
WHERE first_name LIKE 'Ann%'
```

### WHERE 和 BETWEEN

- 取出first_name第1個字元是A,同時first_name的字元長度是3到5的資料

```sql
SELECT first_name, LENGTH(first_name) AS name_length
FROM customer
WHERE first_name LIKE 'A%' AND LENGTH(first_name) BETWEEN 3 AND 5
```

### WHERE 和 <>

- 取出first_name,前3字為Bra,但last_name不是Motley

```sql
SELECT first_name, last_name
FROM customer
WHERE first_name LIKE 'Bra%' AND last_name <> 'Motley'
```


