# 使用python新增資料

- 連線至資料庫
- 使用Connection物件建立Cursor物件
- 使用INSERT語法並配合?符號,插入資料

```python
 INSERT INTO projects(name,begin_date,end_date) VALUES(?,?,?)
```

![](./images/pic1.png)

