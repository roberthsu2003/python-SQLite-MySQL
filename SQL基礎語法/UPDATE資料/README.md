#### UPDATE範例

- 匯入employees.csv

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

