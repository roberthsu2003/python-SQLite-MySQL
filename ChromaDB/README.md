# 向量資料庫

## 安裝

```
pip install chromadb
```

## 建立Chroma Client

```python
import chromadb
chroma_client = chromadb.Client()
```

## 建立collection

```python
collection = chroma_client.create_collection("my_collection")
```

## 增加一些文字文件至collection

```python
collection.add(documents=[
    "This is a document about pineapple",
    "This is a document about oranges"
],
ids=["id1", "id2"])
```


## 要求collection

```python
collection.add(documents=[
    "This is a document about pineapple",
    "This is a document about oranges"
],
ids=["id1", "id2"])

#====output=====
{'data': None,
 'distances': [[1.0404011011123657, 1.2430806159973145]],
 'documents': [['This is a document about pineapple',
                'This is a document about oranges']],
 'embeddings': None,
 'ids': [['id1', 'id2']],
 'included': [<IncludeEnum.distances: 'distances'>,
              <IncludeEnum.documents: 'documents'>,
              <IncludeEnum.metadatas: 'metadatas'>],
 'metadatas': [[None, None]],
 'uris': None}
```

