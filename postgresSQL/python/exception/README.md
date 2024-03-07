## 例外(exception)

```python
try:
   cur.execute("SELECT * FROM barf")
except psycopg2.Error as e:
	 print(e.pgcode) #'42P01'
	 print(e.pgerror) # ERROR:  relation "barf" does not exist
LINE 1: SELECT * FROM barf
```