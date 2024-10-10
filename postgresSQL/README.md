## PostgreSQL

### PostgreSQL Server安裝
- [postgreSQL官網](https://postgresql.org)
- [linux_raspberry安裝](./server安裝/)

### 安裝管理套件(pgAdmin4)
- [下載官網](https://www.pgadmin.org)

### 文件參考
- [postgresql官方說明](https://www.postgresql.org/docs/current/)
- [postgresql-tutorial](https://www.postgresqltutorial.com/postgresql-tutorial/)
- [psycopg2-python連結官方說明](https://www.psycopg.org/docs/)

### [範例資料庫下載](./範例資料庫)

### PostgreSQL SQL語法(上課用)

- [建立資料庫](./上課用sql/1建立資料庫.md)
- [postgre的資料表和基本型別](./上課用sql/2_0基本型別.md)
- [建立資料表](./上課用sql/2建立資料表.md)
	- [將csv匯入資料表,包含台鐵進出站關聯資料庫](./上課用sql/2_1匯入csv.md)
 - [限制](./上課用sql/4限制.md) 
- [新增資料](./上課用sql/3新增資料.md)
- [取得資料](./上課用sql/6取得資料.md)
- [修改和刪除](./上課用sql/5修改和刪除.md)
- [FOREIGN_KEY](./上課用sql/7_0FOREIGN_KEY.md)
	- 1. 使用下方簡單範例-> 適合初學者
	- 2. 使用下方簡單範例->複雜關聯資料庫(實作案例)
- [JOIN](./上課用sql/JOIN.md)
- [GROUP BY](./上課用sql/GROUP_BY.md)
- [HAVING](./上課用sql/HAVING.md)
- [SubQuery](./上課用sql/subQuery.md)
- [JSON應用](./上課用sql/16json.md)

- 複雜關聯資料庫(實作案例)
	- [適合初學者](./上課用sql/7.0適合初學者關聯資料庫.md)
	- [創建關聯資料庫](./上課用sql/7創建關聯資料庫.md)
	- [新增關聯資料庫資料](./上課用sql/8新增關聯資料庫資料.sql)
	- [搜尋關聯資料庫](./上課用sql/9搜尋關聯資料庫.sql)
	- [聚合函式](./上課用sql/10聚合函式.sql)
	- [萬用字元](./上課用sql/11萬用字元.sql)
	- [聯集union](./上課用sql/12聯集.sql)
	- [連結join](./上課用sql/13連結.sql)
	- [子查詢subQuery](./上課用sql/14子查詢.sql)
	- [on delete action](./上課用sql/15on_delete_action.sql) 


### 使用範例資料庫(dvd_rental_database)
- [範例資料庫下載](./範例資料庫/dvd_rental_database/dvdrental.zip)
- [CREATE TABLE 練習](./練習/1CREATE_TABLE)
- [INSERT INTO VALUES 練習](./練習/5INSERT_INTO)
- [SELECT 練習](./練習/2SELECT)
- [SELECT DISTINCT 練習](./練習/3SELECT_DISTINCT)
- [WHERE 練習](./練習/6WHERE)
- [ORDER BY 練習](./練習/4ORDER_BY)
- [FOREIGN KEY 練習](./練習/7Foreign_key)
- [JOIN 練習](./練習/8JOIN)
- [GROUP BY,HAVING練習](./練習/9HAVING)
- [SubQuery的練習](./練習/10subQuery)


### Psycopg python套件
- [psycopg2-python連結官方說明](https://www.psycopg.org/docs/)
- [安裝和介紹](./python/安裝和介紹)
- [python整合postgreSQL的基本語法](./python/basic_module_usage)
- [python with整合postgreSQL的語法](./python/with)
- [傳遞資料至SQL Query參數](./python/parameter)
- [SQL資料類型對應至python的資料類型](./python/type)
- [psycopg的Exceptions](./python/exception)


### 實際案例(教學範例container資料夾內有.devcontainer)
- [大盤股市_streamlit](./tutorial_container/範例/1stock_market)
- [台北市youbike_streamlit](./tutorial_container/範例/2taipei_youbike)