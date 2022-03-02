## LIMIT操作

### 語法:
```
SELECT
	column_list
FROM
	table
LIMIT row_count;
```

### 範例

- 匯入tracks

```
SELECT
	trackId,
	name
FROM
	tracks
LIMIT 10;
```

### 語法:

```
SELECT
	column_list
FROM
	table
LIMIT row_count OFFSET offset;
```

```
SELECT
	column_list
FROM
	table
LIMIT offset, row_count;
```

### 範例

```
SELECT
	trackId,
	name
FROM
	tracks
LIMIT 10 OFFSET 10;
```


