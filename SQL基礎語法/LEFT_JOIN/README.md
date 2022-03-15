## LEFT JOIN操作

- From 後的資料表的列會全部顯示

![](./images/pic2.png)

![](./images/pic3.png)

### LEFT JOIN範例

- 匯入albumsAndartist.sql

![](./images/pic1.png)

#### 範例1

```
SELECT
   artists.ArtistId, 
   AlbumId
FROM
   artists
LEFT JOIN albums ON
   albums.ArtistId = artists.ArtistId
ORDER BY
   AlbumId;
```

![](./images/pic4.png)

#### 範例2

```
SELECT
   artists.ArtistId
   , AlbumId
FROM
   artists
LEFT JOIN albums ON
   albums.ArtistId = artists.ArtistId
WHERE
   AlbumId IS NULL;
```




