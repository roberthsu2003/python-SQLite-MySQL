## insert 操作


![](./images/pic1.png)

### 語法

```
INSERT INTO table (column1,column2 ,..)
VALUES( value1,	value2 ,...);
```


### 使用

- 匯入artists.csv

### 新增一筆資料

```
INSERT INTO artists (name)
VALUES('Bud Powell');
```

### 新增多筆資料

```
INSERT INTO artists (name)
VALUES
	('Buddy Rich'),
	('Candido'),
	('Charlie Byrd');
```

