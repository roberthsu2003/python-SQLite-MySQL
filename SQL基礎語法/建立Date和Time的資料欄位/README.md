## Date 和 Time

- sqlite沒有專門的Date和Time的資料類型
- 使用TEXT,REAL,INTEGER來取代

### 使用TEXT,要符合ISO8601格式

```
YYYY-MM-DD HH:MM:SS.SSS
```

#### 範例:

```
CREATE TABLE datetime_text(
   d1 text, 
   d2 text
);
```

使用datetime-function()

UTC日期時間 -> datetime('now')

```
SELECT　datetime('now')
```

本地日期時間 -> datetime('now','localtime')

```
SELECT datetime('now','localtime')
```

#### 範例：

```
INSERT INTO datetime_text (d1, d2)
VALUES(datetime('now'),datetime('now', 'localtime'));
```

```
SELECT
	d1,
	typeof(d1),
	d2,
	typeof(d2)
FROM
	datetime_text;
```

### 使用整數格式

- 1970-01-01 00:00:00到目前的秒數

#### 範例:

```
CREATE TABLE datetime_int (d1 int);
```

- 使用function strftime('%s','now') 
- 使用function strftime('%s','now','localtime')

```
INSERT INTO datetime_int (d1)
VALUES(strftime('%s','now'));
```

```
SELECT d1 FROM datetime_int;
```

```
SELECT datetime(d1,'unixepoch')
FROM datetime_int;
```
