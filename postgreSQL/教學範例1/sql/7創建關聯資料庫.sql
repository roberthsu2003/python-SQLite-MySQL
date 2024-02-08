/*創建公司資料庫*/
/*創立員工表格*/
DROP TABLE IF EXISTS employee CASCADE;
DROP TABLE IF EXISTS  branch CASCADE;
DROP TABLE IF EXISTS client  CASCADE;
DROP TABLE IF EXISTS works_with CASCADE;

CREATE TABLE employee(
	emp_id SERIAL,
	name VARCHAR(20),
	birth_date DATE,
	sex VARCHAR(1),
	salary INT,
	branch_id INT,
	sup_id INT,
 	PRIMARY KEY(emp_id)
);
/*參考語法網址 https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-foreign-key*/
/*創立部門表格*/
CREATE TABLE branch(
	branch_id INT,
	branch_name VARCHAR(20),
	manager_id INT,
	PRIMARY KEY(branch_id),
	FOREIGN KEY(manager_id)
	REFERENCES employee(emp_id) ON DELETE SET NULL
);

/*補上employee少設的2個Foreign key*/
ALTER TABLE employee
ADD FOREIGN KEY(branch_id)
REFERENCES branch(branch_id)
ON DELETE SET NULL;

ALTER TABLE employee
ADD FOREIGN KEY(sup_id)
REFERENCES employee(emp_id)
ON DELETE SET NULL;

/*創建客戶表格*/
CREATE TABLE client(
	client_id SERIAL,
	client_name VARCHAR(20),
	phone VARCHAR(20),
	PRIMARY KEY(client_id)
);

/*創建work_with表格*/
CREATE TABLE works_with(
	emp_id INT,
	client_id INT,
	total_sales INT,
	PRIMARY KEY(emp_id,client_id),
	FOREIGN KEY(emp_id) REFERENCES employee(emp_id) ON DELETE CASCADE,
	FOREIGN KEY(client_id) REFERENCES client(client_id) ON DELETE CASCADE
);



