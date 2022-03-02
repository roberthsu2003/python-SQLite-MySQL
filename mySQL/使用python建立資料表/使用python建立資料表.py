import pymysql.cursors
from pymysql import err


def create_connection():
    """
    建立資料庫和連線至資料庫
    :return: Connection物件
    """
    conn = None
    try:
        conn = pymysql.connect(host='localhost',
                               user='root',
                               password='1234',
                               db='test1',
                               cursorclass=pymysql.cursors.DictCursor)

    except err as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    """
    透過Connection物件和SQL語法建立資料表
    :param conn: Connection物件
    :param create_table_sql: 字串SQL語法
    :return:None
    """

    try:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
    except err as e:
        print(e)

def main():
    sql_create_projects_table = """
    CREATE TABLE IF NOT EXISTS projects(
		id integer PRIMARY KEY,
		name text NOT NULL,
		begin_date text,
		end_date text
    );
    """

    sql_create_tasks_table = """
    CREATE TABLE IF NOT EXISTS task(
	id integer PRIMARY KEY,
	name text NOT NULL,
	priority integer,
	project_id integer NOT NULL,
	status_id integer NOT NULL,
	begin_date text NOT NULL,
	end_date text NOT NULL,
	FOREIGN KEY(project_id) REFERENCES projects(id)
    );
    """

    #建立資料庫和Connection物件
    conn = create_connection()
    if conn is not None:
        create_table(conn,sql_create_projects_table)
        create_table(conn,sql_create_tasks_table)
    else:
        print("Error! 無法建立資料連線")


if __name__ == "__main__":
    main()