## SubQuery 說明

### 什麼是 SubQuery（子查詢）？

SubQuery 是一個嵌套在主查詢中的查詢語句，也稱為**內部查詢**或**嵌套查詢**。子查詢的結果會被主查詢（外部查詢）使用。

**基本語法結構：**
```sql
SELECT column1, column2, ...
FROM table1
WHERE column1 operator (SELECT column1 FROM table2 WHERE condition);
```

### 子查詢的類型

1. **單值子查詢**：返回單一值（如 MAX、MIN、COUNT 等）
2. **多值子查詢**：返回多個值（需要使用 IN、ANY、ALL 等運算符）

#### 多值子查詢運算符詳解

**IN 運算符：**
- 用於檢查值是否在子查詢結果集中
- 語法：`WHERE column IN (subquery)`
- 範例：
```sql
SELECT * FROM employees 
WHERE department_id IN (SELECT id FROM departments WHERE location = '台北');
```

**ANY 運算符：**
- 用於比較值與子查詢結果集中的任何一個值
- 語法：`WHERE column operator ANY (subquery)`
- 支援的比較運算符：`=`, `>`, `<`, `>=`, `<=`, `<>`
- 範例：
```sql
SELECT * FROM products 
WHERE price > ANY (SELECT price FROM products WHERE category = '電子產品');
```

**ALL 運算符：**
- 用於比較值與子查詢結果集中的所有值
- 語法：`WHERE column operator ALL (subquery)`
- 支援的比較運算符：`=`, `>`, `<`, `>=`, `<=`, `<>`
- 範例：
```sql
SELECT * FROM employees 
WHERE salary > ALL (SELECT salary FROM employees WHERE department = '行銷部');
```

**運算符比較表：**
| 運算符 | 說明 | 使用場景 |
|--------|------|----------|
| IN | 值在結果集中 | 檢查多個可能值 |
| ANY | 值與結果集中任一值比較 | 範圍比較（如大於某個範圍的最小值） |
| ALL | 值與結果集中所有值比較 | 極值比較（如大於所有值） |
3. **相關子查詢**：內部查詢依賴於外部查詢的資料

> [!TIP]
> [**簡單範例說明**](../../上課用sql/subQuery.md)

---

### 實際範例解析

#### 1. 進站人數最多的一筆

```sql
SELECT *
FROM gate_count LEFT JOIN stations ON 站點編號 = 編號
WHERE 進站人數=(SELECT MAX(進站人數)
                FROM gate_count);
```

**執行步驟：**
1. **子查詢**：`SELECT MAX(進站人數) FROM gate_count` 先執行，找出所有記錄中的最大進站人數
2. **主查詢**：使用子查詢的結果作為條件，找出進站人數等於最大值的記錄
3. **JOIN 操作**：將結果與 stations 表格結合，獲得完整的站點資訊

**適用場景：** 當您需要找出"最高"、"最低"、"平均"等極值記錄時

#### 2. 各站點進站人數最多的一筆

```sql
SELECT *
FROM gate_count LEFT JOIN stations ON 站點編號 = 編號
WHERE (站點編號,進站人數) IN (
    SELECT 站點編號,MAX(進站人數)
    FROM gate_count
    GROUP BY 站點編號
);
```

**執行步驟：**
1. **子查詢**：
   - `GROUP BY 站點編號` 將資料按站點分組
   - `MAX(進站人數)` 找出每個站點的最大進站人數
   - 返回 `(站點編號, 最大進站人數)` 的組合
2. **主查詢**：使用 `IN` 運算符匹配子查詢返回的多個值組合
3. **JOIN 操作**：結合站點詳細資訊

**適用場景：** 當您需要找出每個分組中的最優記錄時

### 子查詢的優缺點

**優點：**
- 邏輯清晰，易於理解
- 可以處理複雜的查詢需求
- 程式碼結構化，便於維護

**缺點：**
- 執行效率可能較低（特別是相關子查詢）
- 大型資料庫中可能影響效能

### 效能優化建議

1. **考慮使用 JOIN 替代**：某些子查詢可以改寫為 JOIN 操作
2. **建立適當的索引**：在子查詢涉及的欄位上建立索引
3. **避免不必要的子查詢**：能用簡單查詢解決的不要使用子查詢

### 替代方案：Window Functions

對於找出每組最大值的需求，也可以使用視窗函數：

```sql
SELECT *
FROM (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY 站點編號 ORDER BY 進站人數 DESC) as rn
    FROM gate_count LEFT JOIN stations ON 站點編號 = 編號
) ranked
WHERE rn = 1;
```