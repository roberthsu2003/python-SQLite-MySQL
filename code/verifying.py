import mysql.connector
print(
  "MySQL Connector/Python version: {0}"
  .format(mysql.connector.__version__)
)
print("Version as tuple:")
print(mysql.connector.__version_info__)
print("")
print("API level: {0}".format(mysql.connector.apilevel))
print("Parameter style: {0}".format(mysql.connector.paramstyle))
print("Thread safe: {0}".format(mysql.connector.threadsafety))