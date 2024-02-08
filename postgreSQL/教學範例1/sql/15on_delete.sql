/*ON DELETE action*/
/*ON DELETE SET NULL->當foreign key 對應的primary key 初刪除時,對應的foreign key資料全設為NULL*/
/*ON DELETE SET CASECAD->當foreign key 對應的primary key 初刪除時,對應的foreign key資料全部刪除*/
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

CREATE TABLE branch(
	branch_id INT,
	branch_name VARCHAR(20),
	manager_id INT,
	PRIMARY KEY(branch_id),
	FOREIGN KEY(manager_id)
	REFERENCES employee(emp_id) ON DELETE SET NULL
);

ALTER TABLE employee
ADD FOREIGN KEY(branch_id) REFERENCES branch(branch_id) ON DELETE SET NULL;

/*小綠是promary key,當小綠離職後,則對應的部門主管將設為NULL*/
DELETE FROM employee
WHERE name = '小綠';

SELECT *
FROM branch;





