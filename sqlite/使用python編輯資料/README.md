# 使用python更新資料
- 建立Connection物件
- 建立Cursor物件
- 使用UPDATE語法和?符號

```sql
 UPDATE tasks SET priority = ? , begin_date = ? , end_date = ?
 WHERE id = ?
```


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

def update_task(conn, task):

    sql = '''
    UPDATE task
    SET priority = ?,
		begin_date = ?,
		end_date = ?
    WHERE id = ?
    '''
    cursor = conn.cursor()
    cursor.execute(sql,task)
    conn.commit()




if __name__ == "__main__":
    conn = create_connection('phtonsqlite.db')
    if conn is not None:
        with conn:
            update_task(conn, (1, '2021-01-01', '2022-01-01', 1))

```


