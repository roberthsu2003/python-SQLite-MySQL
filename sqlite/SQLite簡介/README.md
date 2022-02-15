# SQLite簡介
SQLite 和 MySQL 都是一種 RDBMS，資料庫是一種以表格（Table）作為基礎的資料儲存系統，每個表格由許多的行（Column，也稱 Field）與列（Row，也稱 Reocrd）所組成。

## SQLite優點及缺點

SQLite 如同它名稱中的 Lite，意指它在設定、管理和所需的資源方面都更加輕量。

### 優點

 1. 容易設定。基於無伺服器的特性，你非常的容易安裝且零配置。
 2. 可攜且跨平台。SQLite 是基於單一文件所組成且格式定義明確的資料庫，使得它的可攜性和跨平台性極佳，備份也極度方便。
 3. 適合開發及測試。由於其自包含特性，在開發階段中你可以使用 SQLite 作為替代手段。

### 缺點

 1. 不提供網路訪問
 2. 不適用大型應用程式
 3. 缺少提升效能的手段
 4. 沒有用戶管理

### 應用場景
1. 應用場景
2. 嵌入式設備及物聯網
3. 作為磁碟文件的替代儲存格式
4. 中低流量網站
5. 資料分析。你能輕易地使用者種格式處理資料集，且輕易地將其分享給其他人使用。
6. 資料緩存。許多場景中會將 SQLite 作為資料緩存的手段，避免了網路往返和中央資料庫伺服器的負載。
7. 伺服器端資料庫。你可以使用 SQLite 作為伺服器端資料庫的底層儲存引擎。
8. 開發或測試階段的替代及臨時方案
9. 適合教育及培訓。輕易地設置性很適合用於 SQL 的教學引擎。


> [參考來源](https://medium.com/erens-tech-book/sqlite-%E8%88%87-mysql-%E7%9A%84%E5%B7%AE%E5%88%A5-a14926030ddd)

## 參考資料
### sqlite [官方網站](https://docs.python.org/3/library/sqlite3.html)
### sqlite [語法參考](https://www.tutorialspoint.com/sqlite/sqlite_python.htm)
### python和sqlite3 [範例](https://pythonexamples.org/python-sqlite3-tutorial/)

### SQLite Python [說明](https://www.sqlitetutorial.net/sqlite-python)


