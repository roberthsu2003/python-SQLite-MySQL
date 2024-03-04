## JOIN(連結)

## 新增2個資料表,並加入資料

```sql
CREATE TABLE basket_a(
	a INT PRIMARY KEY,
	fruit_a VARCHAR(100) NOT NULL
);

CREATE TABLE basket_b(
	b INT PRIMARY KEY,
	fruit_b VARCHAR(100) NOT NULL
);

INSERT INTO basket_a (a, fruit_a)
VALUES
    (1, 'Apple'),
    (2, 'Orange'),
    (3, 'Banana'),
    (4, 'Cucumber');
	
INSERT INTO basket_b (b, fruit_b)
VALUES
    (1, 'Orange'),
    (2, 'Apple'),
    (3, 'Watermelon'),
    (4, 'Pear');
```

### 結果
```
a | fruit_a
---+----------
 1 | Apple
 2 | Orange
 3 | Banana
 4 | Cucumber
(4 rows)


b |  fruit_b
---+------------
 1 | Orange
 2 | Apple
 3 | Watermelon
 4 | Pear
(4 rows)
```

### inner join(交集)

```sql
/*INNER JOIN-交集*/
SELECT a,fruit_a,b,fruit_b
FROM basket_a INNER JOIN basket_b ON fruit_a = fruit_b
```

![](./images/pic8.png)

### 結果:

```
a | fruit_a | b | fruit_b
---+---------+---+---------
 1 | Apple   | 2 | Apple
 2 | Orange  | 1 | Orange
```

---

### left join

```sql
/*LEFT JOIN*/
SELECT a, fruit_a, b, fruit_b
FROM basket_a LEFT JOIN basket_b ON fruit_a = fruit_b
```

![](pic9.png)

### 結果

```
 a | fruit_a  |  b   | fruit_b
---+----------+------+---------
 1 | Apple    |    2 | Apple
 2 | Orange   |    1 | Orange
 3 | Banana   | null | null
 4 | Cucumber | null | null
```

---

### left join(加上where 語法)

```sql
SELECT a, fruit_a, b, fruit_b
FROM basket_a LEFT JOIN basket_b ON fruit_a = fruit_b
WHERE b IS NULL
```

![](./images/pic10.png)

### 結果

```
a | fruit_a  |  b   | fruit_b
---+----------+------+---------
 3 | Banana   | null | null
 4 | Cucumber | null | null
```

---

### right join

```sql
SELECT a, fruit_a, b, fruit_b
FROM basket_a RIGHT JOIN basket_b ON fruit_a = fruit_b
```

![](./images/pic11.png)

### 結果

```
a   | fruit_a | b |  fruit_b
------+---------+---+------------
    2 | Orange  | 1 | Orange
    1 | Apple   | 2 | Apple
 null | null    | 3 | Watermelon
 null | null    | 4 | Pear
```

---

### right join(where)

```sql
/*RIGHT JOIN with WHERE Cause*/
SELECT a, fruit_a, b, fruit_b
FROM basket_a RIGHT JOIN basket_b ON fruit_a = fruit_b
WHERE a IS NULL
```

![](./images/pic12.png)

### 結果

```
 a   | fruit_a | b |  fruit_b
------+---------+---+------------
 null | null    | 3 | Watermelon
 null | null    | 4 | Pear
(2 rows)
```

---

### full outer join

```sql
SELECT a, fruit_a, b, fruit_b
FROM basket_a FULL OUTER JOIN basket_b ON fruit_a = fruit_b
```

![](./images/pic13.png)

### 結果

```
a   | fruit_a  |  b   |  fruit_b
------+----------+------+------------
    1 | Apple    |    2 | Apple
    2 | Orange   |    1 | Orange
    3 | Banana   | null | null
    4 | Cucumber | null | null
 null | null     |    3 | Watermelon
 null | null     |    4 | Pear
```

---

### full outer join with where

```sql
SELECT a, fruit_a, b, fruit_b
FROM basket_a FULL OUTER JOIN basket_b ON fruit_a = fruit_b
WHERE a IS NULL OR b IS NULL;
```

![](./images/pic14.png)

### 結果

```
 a   | fruit_a  |  b   |  fruit_b
------+----------+------+------------
    3 | Banana   | null | null
    4 | Cucumber | null | null
 null | null     |    3 | Watermelon
 null | null     |    4 | Pear
```



