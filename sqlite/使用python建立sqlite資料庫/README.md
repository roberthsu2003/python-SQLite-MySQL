# 使用python建立sqlite資料庫和建立資料表

## 使用2種套件連結sqlite

### 1 PySQLite套件
PySQLite提供標準的 Python DBI API 2.0相容的介面,而目前市面上常見的資料庫MySQL, PostgreSQL, Oracle,都有支援DBI API 2.0。所以範例將會**採用PySQLite套件**


### 2 APSW套件

如果專案只會使用sqlite,應該使用APSW模組，這個使用的是原生SQLite C,可以有最好的效能。但只可以使用在sqlite資料庫。

## pysqlite已經成為python3.x版的標準套件

代表我們不需要再安裝外部套件，就可以直接使用。


