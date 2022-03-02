## 選取資料

### 語法:

```
SELECT DISTINCT column_list
FROM table_list
```

### 選取範例

- 匯入tracks.csv

![](./images/pic2.png)

```
SELECT
	trackid,
	name,
	composer,
	unitprice
FROM
	tracks;
```

```
SELECT * FROM tracks;
```

