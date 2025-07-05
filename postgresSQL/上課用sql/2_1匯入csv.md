# PostgreSQL 匯入 CSV 檔案教學

## 1. 匯入城市資料 - 使用 SQLite 建立的城市.sql

### 步驟說明
1. 將 `城市.csv` 透過 DB Browser 匯入
2. 透過 DB Browser 匯出 `城市.sql`
3. [下載城市.sql檔案](./其它範例csv/city.sql)
4. 使用 pgAdmin4 開啟城市.sql，並執行

## 2. 匯入目前天氣資料

### 資料來源
- [下載目前天氣.csv](./其它範例csv/目前天氣.csv)

### 建立資料表
```sql
/* 建立目前天氣資料表 */
CREATE TABLE IF NOT EXISTS 目前天氣(
    城市 VARCHAR(10),
    啟始時間 DATE,
    結束時間 DATE,
    最高溫度 REAL,
    最低溫度 REAL,
    感覺 VARCHAR,
    PRIMARY KEY(城市)
);
```

### 匯入步驟
使用 pgAdmin 匯入 `目前天氣.csv` 至資料表 `目前天氣`

![匯入步驟1](./images/pic1.png)
![匯入步驟2](./images/pic2.png)
![匯入步驟3](./images/pic3.png)

## 3. 匯入台鐵車站資訊和車站進出資料

### 資料來源
- [台鐵車站資訊.csv](https://github.com/roberthsu2003/python-SQLite-MySQL/blob/master/postgresSQL/範例資料庫/其它範例csv/台鐵車站資訊.csv)
- [2019-2023進出資訊](https://github.com/roberthsu2003/python-SQLite-MySQL/blob/master/postgresSQL/範例資料庫/其它範例csv/每日各站進出站人數20190423-20231231.zip)

### 建立關聯式資料表

#### 車站資料表
```sql
CREATE TABLE IF NOT EXISTS stations(
    id SERIAL PRIMARY KEY,
    stationCode VARCHAR(5) UNIQUE NOT NULL,  /* 必須設定，因為是 foreign key 的 parent */
    stationName VARCHAR(20) NOT NULL,
    name VARCHAR(20),
    stationAddrTw VARCHAR(50),
    stationTel VARCHAR(20),
    gps VARCHAR(30),
    haveBike BOOLEAN
);

-- 刪除資料表（如果需要重新建立）
DROP TABLE IF EXISTS stations;

-- 查詢資料
SELECT * FROM stations;
```

#### 車站進出資料表
```sql
CREATE TABLE IF NOT EXISTS station_in_out(
    date TIMESTAMP,
    staCode VARCHAR(5) NOT NULL,
    gateInComingCnt INTEGER,
    gateOutGoingCnt INTEGER,
    PRIMARY KEY (date, staCode),
    FOREIGN KEY (staCode)  /* 可設可不設，有設可以保持資料的完整性 */
        REFERENCES stations(stationCode)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- 刪除資料表（如果需要重新建立）
DROP TABLE IF EXISTS station_in_out;
```

### 查詢範例

#### JOIN 查詢
```sql
SELECT * 
FROM station_in_out in_out 
JOIN stations s ON in_out.staCode = s.stationCode;
```

#### 時間查詢語法
```sql
-- 查詢特定日期
SELECT * FROM table_name WHERE date_column = 'YYYY-MM-DD';

-- 查詢時間範圍
SELECT * FROM table_name 
WHERE timestamp_column BETWEEN 'start_timestamp' AND 'end_timestamp';

-- 查詢最近7天
SELECT * FROM table_name 
WHERE timestamp_column >= NOW() - INTERVAL '7 days';

-- 查詢未來7天
SELECT * FROM tasks 
WHERE task_due_date BETWEEN NOW() AND NOW() + INTERVAL '7 days';
```

#### 布林值查詢
```sql
SELECT * FROM table_name WHERE boolean_column = TRUE;
```

## 4. 匯入 DVD 租賃店專案資料庫

### DVD Rental Database 資料架構

![DVD Rental Database 架構圖](./images/dvd-rental-sample-database-diagram.png)

### 下載和安裝步驟

#### 下載 DVD Rental Database (PostgreSQL)
- [下載位址](./dvd_rental_database/)
- 解壓縮後會產生一個 `dvdrental` 的資料夾

#### 使用 pgAdmin4 還原資料庫
1. 建立一個 `dvdrental` 的資料庫
2. 執行 restore（注意是資料夾）

![還原步驟1](./images/pic4.png)
![還原步驟2](./images/pic5.png)

---

> **資料來源**: [PostgreSQL Tutorial - Sample Database](https://www.postgresqltutorial.com/postgresql-getting-started/postgresql-sample-database/)


