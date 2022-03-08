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


def select_all_tasks(conn):
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM task")
        rows = cursor.fetchall()
        for row in rows:
            print(row)


def select_task_by_priority(conn, priority):
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM task WHERE priority=%s", (priority,))
        rows = cursor.fetchall()
        for row in rows:
            print(row)


if __name__ == "__main__":
    conn = create_connection()
    if conn is not None:
        with conn:
            print("1.透過priority選取資料")
            select_task_by_priority(conn, 1)
            
            print("2.選取task資料表內的所有資料")
            select_all_tasks(conn)


