import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """
    建立資料庫和連線至資料庫
    :param db_file: 資料庫的檔案名稱
    :return: Connection物件
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)

    return conn

def update_task(conn, task):
    """
    :param conn: Connection物件
    :param task: tuple(要修改的資料)
    :return: None
    """

    sql = '''UPDATE task 
             SET priority = ?,
                 begin_date = ?,
                 end_date = ?
             WHERE id = ?    
    '''

    cursor = conn.cursor()
    cursor.execute(sql, task)
    conn.commit()


def main():
    database = "pythonsqlite.db"

    #建立資料庫和Connection物件
    conn = create_connection(database)
    with conn:
        update_task(conn, (2, '2021-01-04', '2021-05-06', 2))



if __name__ == "__main__":
    main()