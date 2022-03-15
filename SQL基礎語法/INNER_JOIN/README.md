## INNER JOIN操作

- 交集的觀念

![](./images/pic1.png)

![](./images/pic2.png)

### INNER JOIN範例

- 使用chinook.db

![](./images/pic3.png)

#### 範例1

```
SELECT  TrackId,name,Title
FROM tracks
INNER JOIN albums ON albums.AlbumId = tracks.AlbumId
ORDER By TrackId
```


![](./images/pic4.png)

#### 範例2

```
SELECT
    trackid,
    name,
    tracks.albumid AS album_id_tracks,
    albums.albumid AS album_id_albums,
    title
FROM
    tracks
    INNER JOIN albums ON albums.albumid = tracks.albumid;
```

![](./images/pic5.png)

#### 範例3

![](./images/pic6.png)

```
SELECT
    trackid,
    tracks.name AS track,
    albums.title AS album,
    artists.name AS artist
FROM
    tracks
    INNER JOIN albums ON albums.albumid = tracks.albumid
    INNER JOIN artists ON artists.artistid = albums.artistid;
```

![](./images/pic7.png)

