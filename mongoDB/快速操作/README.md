## MongoDB 快速操作
- 非關聯式資料庫(NoSQL)
- [官網python_mongodb線上學習](https://learn.mongodb.com/learning-paths/mongodb-python-developer-path)
> [本頁資料來源](https://www.mongodb.com/developer/languages/python/python-quickstart-crud/#start-a-mongodb-cluster-on-atlas)

### 直接使用altas MongoDb
	- 不需要要自行安裝和設定
	- [官方英文登入位置](https://www.mongodb.com/cloud/atlas/register)
		- 使用此英文登入位置,不然會被導入簡體登入位置(預防資料儲存至中國)
	- [官方的getting start](https://www.mongodb.com/developer/products/atlas/quickstart-mongodb-atlas-python/)
	
### 使用M0 cluster 等級是永久免費
### atlas MongoDB的架構
- 個人帳號 -> Project -> (DataBase -> Cluster) -> Collection -> Document 
- 可將DataBase和Cluster當作同個名稱等級

### 管理工具
- vscode安裝mongoDB延伸模組
- MongoDB compass
- 
### 安裝python套件:

```python
pip install pymongo[srv]==3.10.1
pip install python-dotenv==0.13.0
```

### 設定MongoDB
- 建立使用者(為了安全性,允許可以讀取資料庫)
- 允許ip address(預設有指定ip,更改為不限定0.0.0.0)
- load sample dataset -> 內建的為了測試。

### 取得使用者連線URI
- 設定至.env內

```
#.env內的設定

client = MongoClient("mongodb://username:password@localhost:27017/mydatabase?authSource=admin")
```

### 測試是否連線成功
- 顯示目前所有的可使用的資料庫(database)
- sample_mflix是可內建導入的資料庫

```python
import datetime   # This will be needed later
import os

from dotenv import load_dotenv
from pymongo import MongoClient

# Load config from a .env file:
load_dotenv()
MONGODB_URI = os.environ['MONGODB_URI']

# Connect to your MongoDB cluster:
client = MongoClient(MONGODB_URI)

# List all the databases in the cluster:
for db_info in client.list_database_names():
   print(db_info)

#====output-database名稱=====
sample_mflix
admin
local
```

### 檢查目前sample_mflix資料庫內的collection

```python
# Get a reference to the 'sample_mflix' database:
db = client['sample_mflix']

# List all the collections in 'sample_mflix':
collections = db.list_collection_names()
for collection in collections:
   print(collection)
   
#===========output=========
theaters
embedded_movies
sessions
movies
comments
users
```

### 檢查movies collection 內的第1筆document

```python
# Import the `pprint` function to print nested data:
from pprint import pprint

# Get a reference to the 'movies' collection:
movies = db['movies']

# Get the document with the title 'Blacksmith Scene':
pprint(movies.find_one({'title': 'The Great Train Robbery'}))
```

### 增加一筆document

```python
# Insert a document for the movie 'Parasite':
insert_result = movies.insert_one({
      "title": "Parasite",
      "year": 2020,
      "plot": "A poor family, the Kims, con their way into becoming the servants of a rich family, the Parks. "
      "But their easy life gets complicated when their deception is threatened with exposure.",
      "released": datetime(2020, 2, 7, 0, 0, 0),
   })

# Save the inserted_id of the document you just created:
parasite_id = insert_result.inserted_id
print("_id of inserted document: {parasite_id}".format(parasite_id=parasite_id))

#=====output=======
_id of inserted document: 677616dac013cc6e4fb5eadd
```

### 搜尋一筆資料
- bson(mongodb的dependency)

```python
import bson # <- Put this line near the start of the file if you prefer.

# Look up the document you just created in the collection:
print(movies.find_one({'_id': bson.ObjectId(parasite_id)}))

#====output====
{'_id': ObjectId('677616dac013cc6e4fb5eadd'),
 'plot': 'A poor family, the Kims, con their way into becoming the servants of '
         'a rich family, the Parks. But their easy life gets complicated when '
         'their deception is threatened with exposure.',
 'released': datetime.datetime(2020, 2, 7, 0, 0),
 'title': 'Parasite',
 'year': 2020}
```

```python
for doc in movies.find({'title':'Parasite'}):
    pprint(doc)
    
#====output====
{'_id': ObjectId('677616dac013cc6e4fb5eadd'),
 'plot': 'A poor family, the Kims, con their way into becoming the servants of '
         'a rich family, the Parks. But their easy life gets complicated when '
         'their deception is threatened with exposure.',
 'released': datetime.datetime(2020, 2, 7, 0, 0),
 'title': 'Parasite',
 'year': 2020}
```

### 更新資料

```python
# Update the document with the correct year:
update_result = movies.update_one({ '_id': parasite_id }, {
   '$set': {"year": 2019}
})

# Print out the updated record to make sure it's correct:
pprint(movies.find_one({'_id': bson.ObjectId(parasite_id)}))

#====output=====
# Update the document with the correct year:
update_result = movies.update_one({ '_id': parasite_id }, {
   '$set': {"year": 2019}
})

# Print out the updated record to make sure it's correct:
pprint(movies.find_one({'_id': bson.ObjectId(parasite_id)}))
```

### 刪除資料
```python
movies.delete_many(
    {'title':'Parasite'}
)
```









	
	