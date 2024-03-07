## 使用with語法

- with conn語法-自動執行conn.commit()

- with psycopg2.connect(DSN) as conn 自動執行conn.commit()和conn.close() 

- with conn.cursor as curs-自動執行執行curs.close()

## 執行一個SQL敘述的語法

```python
with psycopg2.connect(DSN) as conn:
    with conn.cursor() as curs:
        curs.execute(SQL)
```

- 內部with程式區塊執行完,自動執行curs.close()
- 外部with程式區塊執行完,如果成功,自動執行conn.commit(),失敗執行conn.rollback(),最後還會自動執行conn.close()


## 執行多個新增,更新,刪除的語法

```python
conn = psycopg2.connect(DSN)

with conn:
    with conn.cursor() as curs:
        curs.execute(SQL1)

with conn:
    with conn.cursor() as curs:
        curs.execute(SQL2)

conn.close()
```

- with conn:成功,自動執行conn.commit(),失敗執行conn.rollback(),不會執行conn.close()
- 最後一定要執行conn.close()

