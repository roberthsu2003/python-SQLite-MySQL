# 使用python刪除資料

- 建立Connection物件
- 建立Cursor物件
- 使用DELETE語法配合符號?

```
DELETE FROM tasks WHERE id=?
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


def delete_task(conn, id):
    sql = '''
    DELETE FROM task
    WHERE id = ?
    '''

    cursor = conn.cursor()
    cursor.execute(sql,(id,))
    conn.commit()



if __name__ == "__main__":
    conn = create_connection('phtonsqlite.db')
    if conn is not None:
        with conn:
            delete_task(conn, 1)

```

