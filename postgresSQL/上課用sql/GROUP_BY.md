## GROUP_BY

### 語法

```sql
SELECT 
   column_1, 
   column_2,
   ...,
   aggregate_function(column_3)
FROM 
   table_name
GROUP BY 
   column_1,
   column_2,
   ...;
```

- SELECT column_1,column_2,GROUP BY只可以使用SELECT 後的欄位column_1,column_2(先SELECT再GROUPBy)
- SELECT後使用聚合涵式
- GROUP BY 前面有FROM和WHERE子句
- GROUP BY 後面有HAVING,SELECT,DISTINCT,ORDER BY,LIMIT

### 使用dvd_rental範例資料庫內的payment資料表

![](./images/pic15.png)

### 使用GROUP BY 沒有聚合函式
- 取出payment的所有客戶的coutomer_id(不重覆)

```sql
SELECT customer_id
FROM payment
GROUP BY customer_id
ORDER BY customer_id ASC;
```

#### 結果:

```
customer_id
-------------
           1
           2
           3
           4
           5
           6
           7
           8
...
```

### 使用GROUP BY 和聚合函式SUM
- 取出每個customer_id,amount欄位的總合

```sql
SELECT customer_id, SUM(amount)
FROM payment
GROUP BY customer_id
ORDER By customer_id;
```

#### 結果:

```
customer_id |  總合
-------------+--------
           1 | 114.70
           2 | 123.74
           3 | 130.76
           4 |  81.78
           5 | 134.65
           6 |  84.75
           7 | 130.72
...
```

### 使用GROUP BY 和聚合函式SUM(),並依據總合由大到小排序

- 取出customer_id和總合(amount),並且依據總合由大到小排序

```sql
SELECT customer_id, SUM(amount) as 總合
FROM payment
GROUP BY customer_id
ORDER By 總合 DESC;
```

#### 結果:

```
customer_id |  總合
-------------+--------
         148 | 211.55
         526 | 208.58
         178 | 194.61
         137 | 191.62
         144 | 189.60
```

### 使用GROUP BY,SUM,和join的子句(使用payment和customer資料表)
取出fist_name和last_name成為full_name和總合(amount),並且依據總合由大到小排序

```sql
SELECT 
	first_name || ' ' || last_name as full_name,
	SUM(amount) as 總合
FROM payment INNER JOIN customer ON payment.customer_id = customer.customer_id 
GROUP BY full_name
ORDER BY 總合 DESC;
```

```sql
SELECT 
	first_name || ' ' || last_name as full_name,
	SUM(amount) as 總合
FROM payment INNER JOIN customer USING(customer_id) 
GROUP BY full_name
ORDER BY 總合 DESC;
```

#### 結果:

```
       full_name       | 總合
-----------------------+--------
 Eleanor Hunt          | 211.55
 Karl Seal             | 208.58
 Marion Snyder         | 194.61
 Rhonda Kennedy        | 191.62
 Clara Shaw            | 189.60
...
```

### GROUP BY和聚合函式COUNT()

- 從payment資料表,取出所有員工的訂單總數

```sql
SELECT staff_id, COUNT(payment_id)
FROM payment
GROUP BY staff_id
``` 

#### 結果:

```
staff_id | count
----------+-------
        1 |  7292
        2 |  7304
```

### GROUP BY多個欄位

- 取出每個員工,在每一個客戶的訂單金額總合

```sql
SELECT staff_id,customer_id,SUM(amount)
FROM payment
GROUP BY staff_id,customer_id
ORDER BY staff_id
```

#### 結果:

```
staff_id     | customer_id |  sum
-------------+-------------+--------
           1 |           1 |  60.8
           1 |          480|  25.93
           1 |           41|  50.88
           1 |           70|  50.89
           1 |           28|  49.87
```

### GROUP BY 和 data欄位

- 取出每日訂單的總合

```sql
/*::為cast operator*/
SELECT payment_date::date AS 日期,
	   SUM(amount) as 總合
FROM payment
GROUP BY 日期
ORDER BY 日期 DESC;

```

#### 結果:

```
日期           |   總合
--------------+---------
 2007-05-14   |  514.18
 2007-04-30   | 5723.89
 2007-04-29   | 2717.60
 2007-04-28   | 2622.73
...
```
