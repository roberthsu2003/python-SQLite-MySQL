/*union 聯集*/

/*員工名字 union 客戶名字*/
SELECT name
FROM employee
UNION
SELECT client_name
FROM client;

/*員工名字 union 客戶名字 union 部門名字*/
SELECT name
FROM employee
UNION
SELECT client_name
FROM client
UNION
SELECT branch_name
FROM branch;

/*出錯,欄位數要樣,資料類型必需一樣*/
SELECT name,sex
FROM employee
UNION
SELECT client_name
FROM client
UNION
SELECT branch_name
FROM branch;

/*2. 員工id + 員工名字 union 客戶id + 客戶名字*/
SELECT emp_id as total_id, name as total_name
FROM employee
UNION
SELECT client_id, client_name
FROM client;

/*3. 員工薪水 union 銷售金額*/
SELECT salary as total_money
FROM employee
UNION
SELECT total_sales
FROM works_with;



