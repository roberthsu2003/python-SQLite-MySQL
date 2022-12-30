# SQLAlchemy

使用關聯式資料庫時，時常會遇到不同類型的資料庫，如sqlite,MySql,PostgreSQL,Oracle.

由於各種不同類型的資料庫，都會有些微的差別，對於開發者來說，這將會造成對應不同的資料庫，編寫控制資料庫的程式碼將也會有所不同。

而SQLAlchemy就是解決不同種類的資料庫，可以只使用**同一套編寫控制資料庫程式碼**。

##  安裝套件

```python
>>> pip install sqlalchemy
```

## 連結資料庫

一開始必需先建立一個連結物件
不同資料庫連結的方法請參考[這裏](https://docs.sqlalchemy.org/en/20/core/engines.html#postgresql)

```python
import sqlalchemy as db

engine = db.create_engine('sqlite:///sqlAlchemy_sample_data/citys.db')
```

## 取出table資料和資料庫的metadata

```python
import sqlalchemy as db

engine = db.create_engine('sqlite:///sqlAlchemy_sample_data/census.sqlite')

connection = engine.connect()
metadata = db.MetaData()

census = db.Table('census',metadata,autoload=True,autoload_with=engine)

#輸出欄位名稱
print(census.columns.keys())

#列印city table的metadata
print(repr(metadata.tables['census']))


結果:================================
['state', 'sex', 'age', 'pop2000', 'pop2008']
Table('census', MetaData(), Column('state', VARCHAR(length=30), table=<census>), Column('sex', VARCHAR(length=1), table=<census>), Column('age', INTEGER(), table=<census>), Column('pop2000', INTEGER(), table=<census>), Column('pop2008', INTEGER(), table=<census>), schema=None)
```

## 取出city_table欄位資料(query)
- table(city)物件已經有了
- metabata(city)物件已經有了


```python
#建立query物件
query = db.select([census])
resultProxy = connection.execute(query)

#取出所有資料
resultSet = resultProxy.fetchall()

#取出前5筆
print(resultSet[:5])

結果:============================
[('Illinois', 'M', 0, 89600, 95012), ('Illinois', 'M', 1, 88445, 91829), ('Illinois', 'M', 2, 88729, 89547), ('Illinois', 'M', 3, 88868, 90037), ('Illinois', 'M', 4, 91947, 91111)]
```

## 取出大量table資料

```python
#建立query物件
query = db.select([census])
resultProxy = connection.execute(query)

while True:
    partial_results = resultProxy.fetchmany(5)
    if(partial_results == []):
        break
    print(partial_results)
    
resultProxy.close()

結果:==============================
[('Illinois', 'M', 0, 89600, 95012), ('Illinois', 'M', 1, 88445, 91829), ('Illinois', 'M', 2, 88729, 89547), ('Illinois', 'M', 3, 88868, 90037), ('Illinois', 'M', 4, 91947, 91111)]
[('Illinois', 'M', 5, 93894, 89802), ('Illinois', 'M', 6, 93676, 88931), ('Illinois', 'M', 7, 94818, 90940), ('Illinois', 'M', 8, 95035, 86943), ('Illinois', 'M', 9, 96436, 86055)]
[('Illinois', 'M', 10, 97280, 86565), ('Illinois', 'M', 11, 94029, 86606), ('Illinois', 'M', 12, 92402, 89596), ('Illinois', 'M', 13, 89926, 91661), ('Illinois', 'M', 14, 90717, 91256)]
...
...
...
```

```python
#建立query物件
'''
SELECT * FROM census 
WHERE sex = F
'''
query = db.select([census]).where(census.columns.sex == 'F')
resultProxy = connection.execute(query)

#取出所有資料
resultSet = resultProxy.fetchone()
print(resultSet)

結果:=======================================
('Illinois', 'F', 0, 85910, 90286)
```

```python
#建立query物件
#建立query物件
'''
SELECT state, sex
FROM census
WHERE state IN (Texas, New York)
'''
query = db.select([census.columns.state, census.columns.sex]).where(census.columns.state.in_(['Texas', 'New York']))
resultProxy = connection.execute(query)

#取出所有資料
resultSet = resultProxy.fetchall()
print(resultSet)

結果:======================
[('New York', 'M'), ('New York', 'M'), ('New York', 'M'), ('New York', 'M'), ('New York', 'M'), ('New York', 'M'), ('New York', 'M'), ('New York', 'M'), ('New York', 'M'), ('New York', 'M'), ('New York', 'M'), ('New York', 'M'), ('New York', 'M'), ('New York', 'M'), ('New York', 'M'), ('New York', 'M'), ('New York', 'M'), ('New York', 'M'), ('New York', 'M'), ('New York', 'M'), ('New York', 'M'), ('New York', 'M'), ('New York', 'M'), ('New York', 'M'), ('New York', 'M'), 
...
...
...
```


```python
#建立query物件
'''
SELECT * FROM census
WHERE state = 'California' AND NOT sex = 'M'
'''
query = db.select([census]).where(db.and_(census.columns.state == 'California', census.columns.sex != 'M'))
resultProxy = connection.execute(query)

#取出所有資料
resultSet = resultProxy.fetchall()
print(resultSet)


結果:===================================
[('California', 'F', 0, 239605, 274356), ('California', 'F', 1, 236543, 269140), ('California', 'F', 2, 240010, 262556), ('California', 'F', 3, 245739, 259061), ('California', 'F', 4, 254522, 255544), ('California', 'F', 5, 260264, 253899), ('California', 'F', 6, 261296, 247677), ('California', 'F', 7, 264083, 250117), ('California', 'F', 8, 270447, 233293), ('California', 'F', 9, 271482, 231261), ('California', 'F', 10, 270567, 235225),......
```

```python
#建立query物件
'''
SELECT * FROM census
ORDER BY State DESC, pop2000
'''
query = db.select([census]).order_by(db.desc(census.columns.state), census.columns.pop2000)
resultProxy = connection.execute(query)

#取出所有資料
resultSet = resultProxy.fetchall()
print(resultSet)

結果:==================================
[('Wyoming', 'M', 84, 490, 643), ('Wyoming', 'M', 83, 515, 726), ('Wyoming', 'M', 82, 634, 792), ('Wyoming', 'M', 81, 687, 845), ('Wyoming', 'F', 84, 801, 878), ('Wyoming', 'M', 80, 826, 976), ('Wyoming', 'M', 79, 844, 961), ('Wyoming', 'F', 83, 866, 1056), ('Wyoming', 'M', 78, 942, 1051), ('Wyoming', 'F', 82, 963, 1006), ('Wyoming', 'F', 81, 1000, 1089), ('Wyoming', 'F', 80, 1097, 1194), ('Wyoming', 'M', 77, 1110, 1056), ('Wyoming', 'M', 76, 1142, 1188),.....
```

```python
#建立query物件
'''
SELECT SUM(pop2008)
FROM census
'''
query = db.select([db.func.sum(census.columns.pop2008)])
resultProxy = connection.execute(query)

#取出所有資料
resultSet = resultProxy.fetchone()
print(resultSet)

結果:===========================
(302876613,)
```

```python
#建立query物件
'''
SELECT SUM(pop2008) as pop2008, sex
FROM census
Group by sex
'''
query = db.select([db.func.sum(census.columns.pop2008).label('pop2008'), census.columns.sex]).group_by(census.columns.sex)
resultProxy = connection.execute(query)

#取出所有資料
resultSet = resultProxy.fetchall()
print(resultSet)

結果:=============================
[(153959198, 'F'), (148917415, 'M')]
```

```python
#建立query物件
'''
SELECT DISTINCT state
FROM census
'''
query = db.select([census.columns.state.distinct()])
resultProxy = connection.execute(query)

#取出所有資料
resultSet = resultProxy.fetchall()
print(resultSet)

結果:=============================
[('Illinois',), ('New Jersey',), ('District of Columbia',), ('North Dakota',), ('Florida',), ('Maryland',), ('Idaho',), ('Massachusetts',), ('Oregon',), ('Nevada',), ('Michigan',), ('Wisconsin',), ('Missouri',), ('Washington',), ('North Carolina',),.....
```

- [參考網站](https://towardsdatascience.com/sqlalchemy-python-tutorial-79a577141a91)








