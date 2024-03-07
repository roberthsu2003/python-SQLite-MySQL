## 如何將python資料傳遞至SQL內
- 使用%s
- 使用tuple或list

```sql
#sql
INSERT INTO some_table (an_int, a_date, a_string)
VALUES (10, '2005-11-18', 'O''Reilly');
```

```python
#python
cur.execute("""
	INSERT INTO some_table (an_int, a_date, a_string)
	VALUES (%s, %s, %s);
	""",
	(10, datetime.date(2005, 11, 18), "O'Reilly"))
```


- 使用%(key)s
- 使用dictionary


```sql
#sql
INSERT INTO some_table (an_int, a_date, a_string)
VALUES (10, '2005-11-18', 'O''Reilly');
```

```python
#python
cur.execute("""
	INSERT INTO some_table (an_int, a_date, another_date,a_string)
	VALUES (%(int)s, %(date)s, %(date)s, %(str)s);
	""",
	 {'int': 10, 'str': "O'Reilly", 'date': datetime.date(2005, 11, 18)})
```
