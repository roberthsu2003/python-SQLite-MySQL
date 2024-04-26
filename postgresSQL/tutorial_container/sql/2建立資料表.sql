/*create table*/
CREATE DATABASE sql_tutorial;
/*
不需要使用這個指令,這個sql檔是由那一個Query tools打開的,如上方的描素
USE sql_tutorial;
*/

/*
postgre 的基本資料類型
字串-> VARCHAR(n)

整數數值 -> SMALLINT, INT, SERIAL  #SERIAL可以自動有的AUTOINCREMENT功能
浮點數型別 -> real, numeric(p,s)
時間型別 -> DATE,TIME,TIMESTAMP
UUID型別,比SERIAL更好,值不會重覆
*/

/*建立表格*/
CREATE TABLE student(
	student_id UUID PRIMARY KEY,
	name VARCHAR(20),
	major VARCHAR(20)
);

/*
無法使用下面指令, psql \d student
DESCRIBE student;
*/

/*刪除表格*/
DROP TABLE student;

/*修改表格-> 增加欄位*/
ALTER TABLE student ADD gpa numeric(3,2)


/*修改表格 -> 刪除欄位*/
ALTER TABLE student DROP gpa


/*建立表格 primary key的另一種寫法*/
CREATE TABLE student(
	student_id SERIAL,
	name VARCHAR(20),
	major VARCHAR(20),
	PRIMARY KEY(student_id)
);






