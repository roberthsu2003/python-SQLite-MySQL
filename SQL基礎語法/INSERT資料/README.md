## join 操作

- 多個資料表的連結查詢
- albums的ArtistId有多個相同的id
- artists的ArtistId沒有重覆

![](./images/pic1.png)


### 語法:
```
SELECT 
    Title,
    Name
FROM 
    albums
INNER JOIN artists 
    ON artists.ArtistId = albums.ArtistId;
```

### 使用

- 匯入artists.csv

```
INSERT INTO artists (name)
VALUES('Bud Powell');
```

### 新增多筆資料

```
INSERT INTO artists (name)
VALUES
	("Buddy Rich"),
	("Candido"),
	("Charlie Byrd");
```

