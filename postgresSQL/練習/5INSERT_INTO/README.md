## 新增資料練習

### 語法

```sql
INSERT INTO table1(column1, column2, …)
VALUES (value1, value2, …);
```

### 建立資料表

```sql
CREATE TABLE links (
  id SERIAL PRIMARY KEY, 
  url VARCHAR(255) NOT NULL, 
  name VARCHAR(255) NOT NULL, 
  description VARCHAR (255), 
  last_update DATE
);
```

### 新增資料

```sql
INSERT INTO links (url, name)
VALUES('https://www.postgresqltutorial.com','PostgreSQL Tutorial');
```

### 新增資料

```sql
INSERT INTO links (url, name)
VALUES('http://www.oreilly.com','O''Reilly Media');
```

### 新增資料

```sql
INSERT INTO links (url, name, last_update)
VALUES('https://www.google.com','Google','2013-06-01');
```

### 語法:
- 回傳資料

```sql
INSERT INTO table1(column1, column2, …)
VALUES (value1, value2, …)
RETURNING output_expression AS output_name;
```

```sql
INSERT INTO links (url, name)
VALUES('https://www.postgresql.org','PostgreSQL') 
RETURNING id;

======output====
id
4
```

### INSERT 多筆資料


```sql
INSERT INTO table_name (column_list)
VALUES
    (value_list_1),
    (value_list_2),
    ...
    (value_list_n);
```



### INSERT 多筆資料並傳出資料

```sql
INSERT INTO table_name (column_list)
VALUES
    (value_list_1),
    (value_list_2),
    ...
    (value_list_n)
RETURNING * | output_expression;
```

```sql
CREATE TABLE contacts (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(384) NOT NULL UNIQUE
);

INSERT INTO contacts (first_name, last_name, email) 
VALUES
    ('John', 'Doe', 'john.doe@example.com'),
    ('Jane', 'Smith', 'jane.smith@example.com'),
    ('Bob', 'Johnson', 'bob.johnson@example.com');
```

```sql
INSERT INTO contacts (first_name, last_name, email) 
VALUES
    ('Alice', 'Johnson', 'alice.johnson@example.com'),
    ('Charlie', 'Brown', 'charlie.brown@example.com')
RETURNING *;
```

```sql
INSERT INTO contacts (first_name, last_name, email) 
VALUES
    ('Eva', 'Williams', 'eva.williams@example.com'),
    ('Michael', 'Miller', 'michael.miller@example.com'),
    ('Sophie', 'Davis', 'sophie.davis@example.com')
RETURNING id;
```

## insert 衝突後,做後續動作

```sql
INSERT INTO table_name (column1, column2, ...)
VALUES (value1, value2, ...)
ON CONFLICT (conflict_column)
DO NOTHING | DO UPDATE SET column1 = value1, column2 = value2, ...;
```

## 有衝突後,更改欄位資料

```sql
INSERT INTO inventory (id, name, price, quantity)
VALUES (1, 'A', 16.99, 120)
ON CONFLICT(id) 
DO UPDATE SET
  price = EXCLUDED.price,
  quantity = EXCLUDED.quantity;
  
```

## 有衝突後,不做任何事

```sql
INSERT INTO inventory (id, name, price, quantity)
VALUES (1, 'A', 16.99, 120)
ON CONFLICT
DO NOTHING
```




