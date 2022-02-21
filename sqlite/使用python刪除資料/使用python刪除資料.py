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

def delete_task(conn, id):
    """
    透過task id 刪除 task內的資料
    :param conn:Connection物件
    :param id:task id
    :return:
    """

    sql = 'DELETE FROM task WHERE id=?'
    cursor = conn.cursor()
    cursor.execute(sql,(id,))
    conn.commit()

def delete_all_task(conn):
    """
    刪除所有task資料庫的內容
    :param conn: Connection物件
    :return:
    """

    sql = 'DELETE FROM task'
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()




def main():
    database = "pythonsqlite.db"

    #建立資料庫和Connection物件
    conn = create_connection(database)
    with conn:
        delete_task(conn, 2)



if __name__ == "__main__":
    main()