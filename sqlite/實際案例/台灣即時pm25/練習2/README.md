## 持續收集資料

- 如果有相同的資料，則更新資料
- 如果有新的資料，則新增資料
- 使用2種SQL語法

```sql
CREATE TABLE IF NOT EXISTS pm25 (
	id INTEGER PRIMARY KEY,
	站點 TEXT NOT NULL,
	城市 TEXT NOT NULL,
	pm25 REAL,
	日期 TEXT NOT NULL,
	單位 TEXT,
	UNIQUE (站點,日期)
);
```

```commandline
INSERT OR REPLACE INTO pm25 (站點,城市,pm25,日期,單位)
VALUES (?,?,?,?,?);
```