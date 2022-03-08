# 使用python更新資料

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

def update_task(conn, task):
    sql = '''UPDATE task 
             SET priority = %s,
                 begin_date = %s,
                 end_date = %s
             WHERE id = %s    
    '''

    with conn.cursor() as cursor:
        cursor.execute(sql, task)
    conn.commit()

if __name__ == "__main__":
    conn = create_connection()
    if conn is not None:
        with conn:
            update_task(conn, (2, '2021-01-04', '2021-05-06', 2))

```