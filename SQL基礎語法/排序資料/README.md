## ORDER BY操作

### 語法

```
SELECT
   select_list
FROM
   table
ORDER BY
    column_1 ASC,
    column_2 DESC;
```

### ORDER BY範例

- 匯入tracks.csv

```
SELECT
	name,
	milliseconds, 
	albumid
FROM
	tracks
ORDER BY
	albumid ASC;
```

- ASC 由小到大排序
- DESC 由大到小排序

```
SELECT
	name,
	milliseconds, 
	albumid
FROM
	tracks
ORDER BY
	albumid ASC,
  milliseconds DESC;
```

