## JOIN

### LEFT JOIN 說明

LEFT JOIN（左外連接）是一種 SQL 連接操作，用於結合兩個或多個資料表的資料。

#### 語法結構
```sql
SELECT 欄位列表
FROM 左表 LEFT JOIN 右表 ON 連接條件
```

#### 工作原理
- **保留左表所有記錄**：LEFT JOIN 會返回左表（FROM 子句中的第一個表）的所有記錄
- **匹配右表記錄**：當右表中有匹配的記錄時，會顯示對應的資料
- **填補空值**：當右表中沒有匹配的記錄時，右表的欄位會顯示 NULL

#### 與其他 JOIN 類型的差異
- **INNER JOIN**：只返回兩表都有匹配的記錄
- **LEFT JOIN**：返回左表所有記錄，右表沒有匹配時顯示 NULL
- **RIGHT JOIN**：返回右表所有記錄，左表沒有匹配時顯示 NULL
- **FULL OUTER JOIN**：返回兩表所有記錄，沒有匹配時顯示 NULL

#### 在此專案中的應用
在火車站進出人數專案中，我們使用 LEFT JOIN 來結合：
- **gate_count 表**（左表）：包含日期、進站人數、出站人數、站點編號
- **stations 表**（右表）：包含編號、名稱、地名、地址、youbike 資訊

這樣可以確保即使某些站點在 stations 表中沒有詳細資訊，gate_count 的資料仍然會被保留。

---

- 使用火車站進出人數專案
- 使用stations,gate_count資料表

### 使用JOIN取出所有欄位

```sql
SELECT * 
FROM gate_count LEFT JOIN stations ON 站點編號 = 編號

/*取出指定欄位*/
```



### 做用JOIN取出指定欄位

```sql
SELECT 日期,進站人數,出站人數,名稱,地名,地址,youbike
FROM gate_count LEFT JOIN stations ON 站點編號 = 編號
```

### 取出基隆市有那些火車站

```sql
SELECT DISTINCT 名稱
FROM gate_count LEFT JOIN stations ON 站點編號 = 編號
WHERE 地址 like '基隆市%';
```

### 取出基隆火車站2022年3月1日資料

```sql
SELECT *
FROM gate_count LEFT JOIN stations ON 站點編號 = 編號
WHERE 日期 = '2022-03-01' AND 名稱 = '基隆'
```

### 取出基隆火車站2022年3月份資料,時間由小到大排序

```sql
SELECT *
FROM gate_count LEFT JOIN stations ON 站點編號 = 編號
WHERE (日期 BETWEEN '2022-03-01'AND '2022-03-31') AND 名稱 = '基隆'
ORDER BY 日期 ASC
```

### 取出基隆火車站和臺北火車站2022年3月份資料,時間由小到大排序

```sql
SELECT *
FROM gate_count LEFT JOIN stations ON 站點編號 = 編號
WHERE (日期 BETWEEN '2022-03-01'AND '2022-03-31') AND 名稱 IN ('基隆','臺北')
ORDER BY 日期 ASC
```

### 取出資料進站人數最多的前10筆資料

```sql
SELECT *
FROM gate_count LEFT JOIN stations ON 站點編號 = 編號
ORDER BY 進站人數 DESC
LIMIT 10
```
