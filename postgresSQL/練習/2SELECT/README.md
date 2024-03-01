## 使用dvd_rental資料庫練習

### SELECT語法

#### - 取得所有客戶的first_name

```sql
SELECT first_name
FROM customer;
```

#### - 取得客戶的 first_name, last_name, email

```sql
SELECT first_name, last_name, email
FROM customer;
```


#### - 取得所有客戶的欄位資料

```sql
SELECT *
FROM customer;
```

#### - 連結first_name, last_name的欄位資料,並重新命名欄位為full_name

```sql
SELECT first_name || ' ' || last_name AS full_name,email 
FROM customer;
```

#### - 顯示目前時間

```sql
SELECT NOW()
```