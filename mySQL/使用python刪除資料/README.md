# 使用python刪除資料

```python
import pymysql.cursors
from pymysql import Error

def create_connection():
    connection = None
    try:
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='1234',
                                     database='world',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
    except Error as e:
        print(e)
    return connection

def delete_task(conn, id):
    sql = 'DELETE FROM task WHERE id=%s'
    with conn.cursor() as cursor:
        cursor.execute(sql,(id,))
    conn.commit()

def delete_all_task(conn):
    sql = 'DELETE FROM task'
    with conn.cursor() as cursor:
        cursor.execute(sql)
    conn.commit()


if __name__ == "__main__":
    conn = create_connection()
    if conn is not None:
        with conn:
            delete_task(conn, 2)


```