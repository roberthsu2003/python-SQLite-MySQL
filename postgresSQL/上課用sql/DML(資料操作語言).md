# DML(資料操作語言)

SQL的DML（資料操作語言，Data Manipulation Language）是用來**操作資料庫中資料的語言**，主要涵蓋對資料的查詢、新增、更新和刪除等操作[1][3][4]。

### DML的主要功能與指令

- **SELECT**：查詢資料庫中的資料，用來取得資料。
- **INSERT**：向資料表中插入新的資料列。
- **UPDATE**：更新資料表中已存在的資料。
- **DELETE**：刪除資料表中的資料。

DML是使用者與資料庫互動時最常用的語言類型，負責處理資料內容的增刪改查，是日常資料操作的核心[1][3][4]。

### 特點

- DML操作的是資料本身，而非資料庫結構（結構操作屬於DDL）。
- DML指令通常會影響資料的狀態，且可搭配交易控制語言（TCL）來確保資料的一致性與完整性。
- DML是資料庫應用程式中最頻繁使用的SQL語言類型。

### 簡單示例

```sql
-- 查詢users資料表中所有資料
SELECT * FROM users;

-- 新增一筆資料
INSERT INTO users (id, name, email) VALUES (1, 'Alice', 'alice@example.com');

-- 更新資料
UPDATE users SET email = 'alice_new@example.com' WHERE id = 1;

-- 刪除資料
DELETE FROM users WHERE id = 1;
```

總結來說，**DML是操作資料庫中資料的語言，包含查詢、插入、更新和刪除，是資料庫應用中不可或缺的指令集**


