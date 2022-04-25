# 使用python新增資料

- 連線至資料庫
- 使用Connection物件建立Cursor物件
- 使用INSERT語法並配合?符號,插入資料

```python
 INSERT INTO projects(name,begin_date,end_date) VALUES(?,?,?)
```

![](./images/pic1.png)

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

def create_table(conn):
    sql_projects = """
    CREATE TABLE IF NOT EXISTS projects(
		id INTEGER PRIMARY KEY,
		name TEXT NOT NULL,
		begin_date TEXT,
		end_date TEXT
    );
    """

    sql_tasks = """
    CREATE TABLE IF NOT EXISTS task(
		id INTEGER PRIMARY KEY,
		name TEXT NOT NULL,
		priority INTEGER,
		project_id INTEGER NOT NULL,
		status_id INTEGER NOT NULL,
		begin_date TEXT NOT NULL,
		end_date TEXT NOT NULL,
		FOREIGN KEY(project_id) REFERENCES projects(id)
    );
    """
    try:
        cursor = conn.cursor()
        cursor.execute(sql_projects)
        cursor.execute(sql_tasks)
    except Error as e:
        print(e)

def insert_project(conn, project):
    sql = """
    INSERT INTO projects(name,begin_date,end_date)
    VALUES(?,?,?)
    """
    cursor = conn.cursor()
    cursor.execute(sql,project)
    conn.commit()

def insert_tasks(conn, task):

    sql = """
    INSERT INTO task(name, priority, status_id, project_id, begin_date,end_date)
    VALUES(?,?,?,?,?,?)
    """
    cursor = conn.cursor()
    cursor.execute(sql, task)
    conn.commit()




if __name__ == "__main__":
    conn = create_connection('phtonsqlite.db')
    if conn is not None:
        with conn:
            create_table(conn)
            insert_project(conn,('我的專案1','2020-04-01','2021-03-01'))
            insert_tasks(conn,('我的任務1',1,2,1,'2020-04-01','2021-03-01'))

```
