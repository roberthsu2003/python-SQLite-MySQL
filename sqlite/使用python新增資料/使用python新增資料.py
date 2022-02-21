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

def create_project(conn, project):
    """
    新增資料至projects資料庫
    :param conn:Connection物件
    :param project:tuple(加入至資料庫的內容)
    :return:自動建立id的最後一筆
    """
    sql = ''' INSERT INTO projects(name,begin_date,end_date)
    VALUES(?, ?, ?)
    '''
    cursor = conn.cursor()
    cursor.execute(sql, project)
    conn.commit()
    return cursor.lastrowid

def create_task(conn, task):
    """
    建立task資庫表的資料
    :param conn: Connection物件
    :param task: tuple(加入至資料庫的內容)
    :return: 自動建立id的最後一筆
    """
    sql = ''' INSERT INTO task(name, priority, status_id, project_id,begin_date, end_date)
    VALUES(?, ?, ?, ?, ?, ?)
    '''
    cursor = conn.cursor()
    cursor.execute(sql, task)
    conn.commit()

    return cursor.lastrowid


def main():
    database = "pythonsqlite.db"

    #建立資料庫和Connection物件
    conn = create_connection(database)
    with conn:
        #建新一個新的project
        project = ('Cool App with SQLite & Python','2020-01-01','2021-01-30')
        project_id = create_project(conn, project)

        #建立一個新的任務
        task_1 = ('Analyze the requirements of the app',1, 1, project_id, '2020-01-01','2020-01-02')
        task_2 = ('Confirm with user about top requirements', 1, 1, project_id, '2020-01-03','2020-01-05')

        #create tasks
        create_task(conn, task_1)
        create_task(conn, task_2)


if __name__ == "__main__":
    main()