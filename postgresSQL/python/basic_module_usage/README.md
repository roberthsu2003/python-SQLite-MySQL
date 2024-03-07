## python整合postgreSQL的基本語法

```python
import psycopg2

# 連線至postgre資料庫
conn = psycopg2.connect("dbname=test user=postgres")

# 建立cursor實體,準備執行SQL
cur = conn.cursor()

# 建立資料表
cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")

# 加入資料
# 傳遞資料進立SQL
cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)",
		      (100, "abc'def"))

# 取出SQL結果,並自動轉成python的資料結構
cur.execute("SELECT * FROM test;")
cur.fetchone() #(1, 100, "abc'def")

# 確認資料庫永久的改變,如果有錯誤,回復資料conn.rollback()
conn.commit()

# 關閉所有python和資料庫的連線(釋放資源)
cur.close()
conn.close()
```