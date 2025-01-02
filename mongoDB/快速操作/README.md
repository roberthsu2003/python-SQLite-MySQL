## MongoDB 快速操作
- 非關聯式資料庫(NoSQL)

### 直接使用altas MongoDb
	- 不需要要自行安裝和設定
	- [官方登入位置]()
	- [官方的getting start](https://www.mongodb.com/developer/products/atlas/quickstart-mongodb-atlas-python/)
	
### 使用M0 cluster 等級是永久免費
### vscode安裝mongoDB延伸模組
### 安裝套件:

```python
pip install pymongo[srv]==3.10.1
pip install python-dotven==0.13.0
```

### 設定MongoDB
- 建立使用者(為了安全性,允許可以讀取資料庫)
- 允許ip address(預設有指定ip,更改為不限定0.0.0.0)
- load sample dataset -> 內建的為了測試。

### 取得使用者連線URI
- 設定至.env內
- 
### 測試是否連線成功
- 顯示目前所有的可使用的資料庫(database)

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
```

- 檢查目前sample_mflix資料庫內的collection

```python
# Get a reference to the 'sample_mflix' database:
db = client['sample_mflix']

# List all the collections in 'sample_mflix':
collections = db.list_collection_names()
for collection in collections:
   print(collection)
```

- 檢查movies collection 內的第1筆document

```python
# Import the `pprint` function to print nested data:
from pprint import pprint

# Get a reference to the 'movies' collection:
movies = db['movies']

# Get the document with the title 'Blacksmith Scene':
pprint(movies.find_one({'title': 'The Great Train Robbery'}))
```







	
	