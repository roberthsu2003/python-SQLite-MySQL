## DELETE操作
### 語法

```
DELETE FROM table
WHERE search_condition
ORDER BY criteria
LIMIT row_count OFFSET offset;
```

### DELETE範例

- 匯入 artists.csv

#### DELETE範例(建立artists_backup資料表和匯入資料)

```

CREATE TABLE artists_backup(
   artistid INTEGER PRIMARY KEY AUTOINCREMENT,
   name NVARCHAR
);


INSERT INTO artists_backup 
SELECT artistid,name
FROM artists;

```

#### DELETE範例(檢查資料)

```
SELECT
	artistid,
	name
FROM
	artists_backup;
```

#### DELETE範例(刪除一列資料)

```
DELETE FROM artists_backup
WHERE artistid = 1;
```

#### DELETE範例(使用LIKE)

```
DELETE FROM artists_backup
WHERE name LIKE '%Santana%';
```

#### 刪除所有資料

```
DELETE FROM artists_backup;
```
