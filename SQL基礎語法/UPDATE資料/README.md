#### UPDATE範例

- 匯入employees.csv

#### 語法

```
UPDATE table
SET column_1 = new_value_1,
    column_2 = new_value_2
WHERE
    search_condition 
ORDER column_or_expression
LIMIT row_count OFFSET offset;
```

#### UPDATE範例(查看資料)

```
SELECT
	employeeid,
	firstname,
	lastname,
	title,
	email
FROM
	employees;
```

#### UPDATE範例(更新一欄資料)

```
UPDATE employees
SET lastname = 'Smith'
WHERE employeeid = 3;
```

#### UPDATE範例(驗證資料)

```
SELECT
	employeeid,
	firstname,
	lastname,
	title,
	email
FROM
	employees
WHERE
	employeeid = 3;
```

#### UPDATE範例(更新多欄資料)

```
UPDATE employees
SET city = 'Toronto',
    state = 'ON',
    postalcode = 'M5P 2N7'
WHERE
    employeeid = 4;
```

#### UPDATE範例(驗證更新多欄資料)

```
SELECT
	employeeid,
	firstname,
	lastname,
	state,
	city,
	PostalCode
FROM
	employees
WHERE
	employeeid = 4;
```

