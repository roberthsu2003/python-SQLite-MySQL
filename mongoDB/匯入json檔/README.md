## 匯入json檔

- 匯入新北市公共自行車租賃系統

### 使用mongoDB compass匯入
- 建立新的collection
- 使用add data按鍵

### 使用python匯入

```python
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

## 取出json檔

```
# Get a reference to the 'sample_mflix' database:
db = client['sample_mflix']

# List all the collections in 'sample_mflix':
collections = db.list_collection_names()
for collection in collections:
   print(collection)
#===output===
新北市公共自行車租賃系統
```

```python
collection = db['新北市公共自行車租賃系統']
json_data = collection.find_one()['result']

#====說明===
json_data -> 儲存的json內容
```