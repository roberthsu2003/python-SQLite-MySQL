/*連結 join*/
/*先將部門增加一筆資料*/
INSERT INTO branch VALUES(4, '偷懶', NULL);

/*取得所有部門經理的名字*/

SELECT *
FROM employee
JOIN branch
ON emp_id = manager_id

/*取得所有部門經理的名字*/
SELECT emp_id, name, branch_name 
FROM employee
JOIN branch
ON emp_id = manager_id

/*取得所有部門經理的名字*/
SELECT employee.emp_id, employee.name, branch.branch_name 
FROM employee
JOIN branch
ON employee.emp_id = branch.manager_id

/*left_join取得所有部門經理的名字和所有員工id和名字*/
SELECT employee.emp_id, employee.name, branch.branch_name 
FROM employee LEFT JOIN branch /*所有員工有employee.emp_id的都要列出*/
ON employee.emp_id = branch.manager_id

/*right_join取得所有部門經理的名字和所有部門名稱*/
SELECT employee.emp_id, employee.name, branch.branch_name 
FROM employee RIGHT JOIN branch /*所有員工有employee.emp_id的都要列出*/
ON employee.emp_id = branch.manager_id
