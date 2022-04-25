# 使用python建立sqlite資料庫和建立資料表

## 使用2種套件連結sqlite

### 1 PySQLite套件
PySQLite提供標準的 Python DBI API 2.0相容的介面,而目前市面上常見的資料庫MySQL, PostgreSQL, Oracle,都有支援DBI API 2.0。所以範例將會**採用PySQLite套件**


### 2 APSW套件

如果專案只會使用sqlite,應該使用APSW模組，這個使用的是原生SQLite C,可以有最好的效能。但只可以使用在sqlite資料庫。

## pysqlite已經成為python3.x版的標準套件

代表我們不需要再安裝外部套件，就可以直接使用。

```
$ import sqlite3
```

## 建立資料庫，其實就是建立一個副檔名.db或是.sqlite的檔案
- 使用sqlite3.connect()函式,建立一個Connection的物件
- 當建立檔案時，如果沒有這個檔案將會自動建立並連線這個資料庫，有這個檔時，則是連線
- 使用Connection的close()方法，結束連線

```python
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

if __name__ == "__main__":
    conn = create_connection('phtonsqlite.db')
    if conn is not None:
        conn.close()
```

## 如果不想建立檔案，只是暫存在記憶體內的語法

```
sqlite3.connect(':memory:')
```


