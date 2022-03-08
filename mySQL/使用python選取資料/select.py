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

def select_all_task(conn):
    pass




if __name__ == "__main__":
    conn = create_connection()
    if conn is not None:
        with conn:
            pass

