## GROUP BY, HAVING


### GROUP BY 說明
GROUP BY 子句用於將查詢結果按照指定的欄位進行分組，通常與聚合函數（如 SUM、COUNT、AVG、MAX、MIN）一起使用。

**基本語法：**
```sql
SELECT 欄位1, 聚合函數(欄位2)
FROM 表格名稱
GROUP BY 欄位1
```

### HAVING 說明
HAVING 子句用於對分組後的結果進行篩選，類似於 WHERE 子句，但 HAVING 是針對分組後的聚合結果進行條件篩選。

**基本語法：**
```sql
SELECT 欄位1, 聚合函數(欄位2)
FROM 表格名稱
GROUP BY 欄位1
HAVING 聚合函數(欄位2) > 某個值
```

### 注意事項
1. **WHERE vs HAVING**：
   - WHERE：在分組前篩選資料
   - HAVING：在分組後篩選聚合結果

2. **SELECT 欄位限制**：
   - 使用 GROUP BY 時，SELECT 中只能包含：
     - GROUP BY 中指定的欄位
     - 聚合函數的結果

3. **執行順序**：
   ```
   FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY
   ```

4. **聚合函數在 HAVING 中的使用**：
   - HAVING 中可以使用聚合函數進行條件判斷
   - 不能在 WHERE 中使用聚合函數

5. **效能考量**：
   - 盡量使用 WHERE 進行初步篩選，減少需要分組的資料量
   - HAVING 用於對分組結果的最終篩選

> [!TIP]
> [簡單範例說明-HAVING](../../上課用sql/HAVING.md)  
> [簡單範例說明-GROUP BY](../../上課用sql/GROUP_BY.md)  

---

### JOIN,GROUP BY, HAVING

- 使用火車站進出人數
- stations,gate_count

```sql
SELECT *
FROM gate_count LEFT JOIN stations ON 站點編號 = 編號
```


### 全省各站點2022年進站總人數

```sql
SELECT DATE_PART('year',日期) AS 年份,名稱,SUM(進站人數) AS 進站人數
FROM gate_count LEFT JOIN stations ON 站點編號 = 編號
WHERE 日期 BETWEEN '2022-01-01' AND '2022-12-31'
GROUP BY 年份,名稱
ORDER BY 進站人數 DESC
```

### 全省各站點2022年進站總人數大於5佰萬人的站點

```sql
SELECT DATE_PART('year',日期) AS 年份,名稱,SUM(進站人數) AS 進站人數
FROM gate_count LEFT JOIN stations ON 站點編號 = 編號
WHERE 日期 BETWEEN '2022-01-01' AND '2022-12-31'
GROUP BY 年份,名稱
HAVING SUM(進站人數) > 5000000
ORDER BY 進站人數 DESC
```


### 基隆火車站2020年,每月份進站人數

```sql
SELECT DATE_TRUNC('month',日期) AS 月份,SUM(進站人數) AS 進站人數
FROM gate_count LEFT JOIN stations ON 站點編號 = 編號
WHERE 名稱 = '基隆' AND 日期 BETWEEN '2020-01-01' AND '2020-12-31'
GROUP BY 月份
ORDER BY 進站人數
```

### 基隆火車站2020年,每月份進站人數,由多至少

```sql
SELECT DATE_PART('month',日期) AS 月份,SUM(進站人數) AS 進站人數
FROM gate_count LEFT JOIN stations ON 站點編號 = 編號
WHERE 名稱 = '基隆' AND 日期 BETWEEN '2020-01-01' AND '2020-12-31'
GROUP BY 月份
ORDER BY 進站人數 DESC
```

### 基隆火車站2020,2021,2022,每年進站人數

```sql
SELECT DATE_PART('year',日期) AS 年份,SUM(進站人數) AS 進站人數
FROM gate_count LEFT JOIN stations ON 站點編號 = 編號
WHERE 名稱 = '基隆' AND 日期 BETWEEN '2020-01-01' AND '2022-12-31'
GROUP BY 年份
ORDER BY 進站人數 DESC
```

### 基隆火車站,臺北火車站2020,2021,2022,每年進站人數

```sql
SELECT DATE_PART('year',日期) AS 年份,名稱,SUM(進站人數) AS 進站人數
FROM gate_count LEFT JOIN stations ON 站點編號 = 編號
WHERE 名稱 IN ('基隆','臺北') AND 日期 BETWEEN '2020-01-01' AND '2022-12-31'
GROUP BY 年份,名稱
ORDER BY 進站人數 DESC
```

---

## 練習題目

**練習 1：** 查詢 2021 年全省各站點進站總人數，並按進站人數由高至低排序

```sql
-- 請寫出 SQL 語法
```

**練習 2：** 查詢 2022 年進站人數超過 1000 萬人的站點

```sql
-- 請寫出 SQL 語法
```

**練習 3：** 查詢台中火車站 2020-2022 年每年的進站人數

```sql
-- 請寫出 SQL 語法
```

**練習 4：** 查詢高雄火車站 2021 年每月份的進站人數，並按月份排序

```sql
-- 請寫出 SQL 語法
```

**練習 5：** 查詢 2020 年進站人數前 10 名的站點

```sql
-- 請寫出 SQL 語法
```

**練習 6：** 查詢台北、桃園、新竹三個火車站 2022 年的進站總人數，並按站點名稱排序

```sql
-- 請寫出 SQL 語法
```

**練習 7：** 查詢 2021 年每月份全省進站總人數，並找出進站人數超過 5000 萬人的月份

```sql
-- 請寫出 SQL 語法
```

**練習 8：** 查詢嘉義火車站 2020 年第一季（1-3月）每月的進站人數

```sql
-- 請寫出 SQL 語法
```

**練習 9：** 查詢 2022 年平均每日進站人數超過 2 萬人的站點

```sql
-- 請寫出 SQL 語法
```

**練習 10：** 查詢台南、高雄兩個火車站 2020-2022 年每年進站人數的比較，並計算兩站每年的人數差距

```sql
-- 請寫出 SQL 語法
```

### 練習解答

**練習 1 解答：**
```sql
SELECT DATE_PART('year',日期) AS 年份,名稱,SUM(進站人數) AS 進站人數
FROM gate_count LEFT JOIN stations ON 站點編號 = 編號
WHERE 日期 BETWEEN '2021-01-01' AND '2021-12-31'
GROUP BY 年份,名稱
ORDER BY 進站人數 DESC
```

**練習 2 解答：**
```sql
SELECT DATE_PART('year',日期) AS 年份,名稱,SUM(進站人數) AS 進站人數
FROM gate_count LEFT JOIN stations ON 站點編號 = 編號
WHERE 日期 BETWEEN '2022-01-01' AND '2022-12-31'
GROUP BY 年份,名稱
HAVING SUM(進站人數) > 10000000
ORDER BY 進站人數 DESC
```

**練習 3 解答：**
```sql
SELECT DATE_PART('year',日期) AS 年份,SUM(進站人數) AS 進站人數
FROM gate_count LEFT JOIN stations ON 站點編號 = 編號
WHERE 名稱 = '台中' AND 日期 BETWEEN '2020-01-01' AND '2022-12-31'
GROUP BY 年份
ORDER BY 年份
```

**練習 4 解答：**
```sql
SELECT DATE_TRUNC('month',日期) AS 月份,SUM(進站人數) AS 進站人數
FROM gate_count LEFT JOIN stations ON 站點編號 = 編號
WHERE 名稱 = '高雄' AND 日期 BETWEEN '2021-01-01' AND '2021-12-31'
GROUP BY 月份
ORDER BY 月份
```

**練習 5 解答：**
```sql
SELECT DATE_PART('year',日期) AS 年份,名稱,SUM(進站人數) AS 進站人數
FROM gate_count LEFT JOIN stations ON 站點編號 = 編號
WHERE 日期 BETWEEN '2020-01-01' AND '2020-12-31'
GROUP BY 年份,名稱
ORDER BY 進站人數 DESC
LIMIT 10
```

**練習 6 解答：**
```sql
SELECT DATE_PART('year',日期) AS 年份,名稱,SUM(進站人數) AS 進站人數
FROM gate_count LEFT JOIN stations ON 站點編號 = 編號
WHERE 名稱 IN ('台北','桃園','新竹') AND 日期 BETWEEN '2022-01-01' AND '2022-12-31'
GROUP BY 年份,名稱
ORDER BY 名稱
```

**練習 7 解答：**
```sql
SELECT DATE_TRUNC('month',日期) AS 月份,SUM(進站人數) AS 進站人數
FROM gate_count LEFT JOIN stations ON 站點編號 = 編號
WHERE 日期 BETWEEN '2021-01-01' AND '2021-12-31'
GROUP BY 月份
HAVING SUM(進站人數) > 50000000
ORDER BY 月份
```

**練習 8 解答：**
```sql
SELECT DATE_PART('month',日期) AS 月份,SUM(進站人數) AS 進站人數
FROM gate_count LEFT JOIN stations ON 站點編號 = 編號
WHERE 名稱 = '嘉義' AND 日期 BETWEEN '2020-01-01' AND '2020-03-31'
GROUP BY 月份
ORDER BY 月份
```

**練習 9 解答：**
```sql
SELECT 名稱,AVG(進站人數) AS 平均每日進站人數
FROM gate_count LEFT JOIN stations ON 站點編號 = 編號
WHERE 日期 BETWEEN '2022-01-01' AND '2022-12-31'
GROUP BY 名稱
HAVING AVG(進站人數) > 20000
ORDER BY 平均每日進站人數 DESC
```

**練習 10 解答：**
```sql
SELECT DATE_PART('year',日期) AS 年份,名稱,SUM(進站人數) AS 進站人數
FROM gate_count LEFT JOIN stations ON 站點編號 = 編號
WHERE 名稱 IN ('台南','高雄') AND 日期 BETWEEN '2020-01-01' AND '2022-12-31'
GROUP BY 年份,名稱
ORDER BY 年份,名稱
```