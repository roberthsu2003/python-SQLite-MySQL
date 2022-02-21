# 連線至mySQL

```python
import mysql.connector

connect_args = {
  "host": "127.0.0.1",
  "port": 3306,
  "user": "pyuser",
  "password": "raspberry",
}

# ---- connect() function ----

db1 = mysql.connector.connect(
  **connect_args
)

print(
  "MySQL connection ID for db1: {0}"
  .format(db1.connection_id)
)
db1.close()

# ---- Explicit MySQLConnection ----

db2 = mysql.connector.MySQLConnection(
  **connect_args
)

print(
  "MySQL connection ID for db2: {0}"
  .format(db2.connection_id)
)

db2.close()

# ---- Two steps manually ----

db3 = mysql.connector.MySQLConnection()
db3.connect(**connect_args)

print(
  "MySQL connection ID for db3: {0}"
  .format(db3.connection_id)
)

db3.close()


# ---- All three steps manually ----
db4 = mysql.connector.MySQLConnection()
db4.config(**connect_args)
db4.connect()

print(
  "MySQL connection ID for db4: {0}"
  .format(db4.connection_id)
)

db4.close()

結果:===========================
MySQL connection ID for db1: 21
MySQL connection ID for db2: 22
MySQL connection ID for db3: 23
MySQL connection ID for db4: 24
```
