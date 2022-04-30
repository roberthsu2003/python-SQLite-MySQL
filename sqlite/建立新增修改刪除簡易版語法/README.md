# 建立新增修改刪除簡易版語法
## 建立資料庫

```python
import sqlite3
conn = sqlite3.connect('example.db')
print("開啟資料庫成功")
結果:===================
開啟資料庫成功
```

## 建立資料表

```python
import sqlite3
conn = sqlite3.connect('example.db')
print("開啟資料庫成功")

c = conn.cursor()
c.execute('''CREATE TABLE COMPANY
(ID INT PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL,
AGE INT NOT NULL,
ADDRESS CHAR(50),
SALARY REAL);
''')
print("company資料表建立")
conn.commit()
conn.close()

結果:=====================
開啟資料庫成功
company資料表建立
```

## insert 操作

```python
import sqlite3
conn = sqlite3.connect('example.db')
print("開啟資料庫成功")

c = conn.cursor()

c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (1, 'Paul', 32, 'California', 20000.00 )")
c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (2, 'Allen', 25, 'Texas', 15000.00)")
c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (3介面和資料整合, 'Teddy', 23, 'Norway', 20000.00)")
c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00)")
conn.commit()
print("4筆資料建立成功")
conn.close()

結果:=================
開啟資料庫成功
4筆資料建立成功
```

## 選取資料

```python
import sqlite3
conn = sqlite3.connect('example.db')
print("開啟資料庫成功")

c = conn.cursor()
cursor = c.execute("SELECT id, name, address, salary  from COMPANY")
for row in cursor:
    print("ID={:d},Name={:s},ADDRESS={:s},SALARY={:.2f}\n".format(row[0], row[1], row[2], row[3]))
print("select 成功")
conn.close()

結果:======================
開啟資料庫成功
ID=1,Name=Paul,ADDRESS=California,SALARY=20000.00

ID=2,Name=Allen,ADDRESS=Texas,SALARY=15000.00

ID=3,Name=Teddy,ADDRESS=Norway,SALARY=20000.00

ID=4,Name=Mark,ADDRESS=Rich-Mond ,SALARY=65000.00

select 成功
```

## UPDATE操作

```python
import sqlite3
conn = sqlite3.connect('example.db')
print("開啟資料庫成功")
c = conn.cursor()
c.execute("UPDATE COMPANY set SALARY = 25000.00 where ID=1")
conn.commit()
print("總共更改的筆數:", conn.total_changes)
cursor = c.execute("SELECT id, name, address, salary  from COMPANY")
for row in cursor:
    print("ID={:d},Name={:s},ADDRESS={:s},SALARY={:.2f}\n".format(row[0], row[1], row[2], row[3]))
print("select 成功")
conn.close()

結果:====================
開啟資料庫成功
總共更改的筆數: 1
ID=1,Name=Paul,ADDRESS=California,SALARY=25000.00

ID=2,Name=Allen,ADDRESS=Texas,SALARY=15000.00

ID=3,Name=Teddy,ADDRESS=Norway,SALARY=20000.00

ID=4,Name=Mark,ADDRESS=Rich-Mond ,SALARY=65000.00

select 成功
```

## DELETE操作

```python
import sqlite3
conn = sqlite3.connect('example.db')
print("開啟資料庫成功")
c = conn.cursor()

c.execute("DELETE from COMPANY where ID=2;")
conn.commit()
print("總共刪除的筆數:", conn.total_changes)
cursor = c.execute("SELECT id, name, address, salary  from COMPANY")
for row in cursor:
    print("ID={:d},Name={:s},ADDRESS={:s},SALARY={:.2f}\n".format(row[0], row[1], row[2], row[3]))
print("select 成功")
conn.close()

結果:======================
開啟資料庫成功
總共刪除的筆數: 1
ID=1,Name=Paul,ADDRESS=California,SALARY=25000.00

ID=3,Name=Teddy,ADDRESS=Norway,SALARY=20000.00

ID=4,Name=Mark,ADDRESS=Rich-Mond ,SALARY=65000.00

select 成功
```

