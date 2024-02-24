/*subquery 子查詢*/

/*1找出研發部門的經理名字*/

SELECT name
FROM employee
WHERE emp_id=(
	SELECT manager_id
	FROM branch
	WHERE branch_name = '研發'
);

/*2找出對單一位客戶錯售金額超過50000的員工名字*/
/*子查詢有多筆資料,必需使用IN(),相同於OR*/
SELECT name
FROM employee
WHERE emp_id IN(
	SELECT emp_id
	FROM works_with
	WHERE total_sales >= 50000
);


