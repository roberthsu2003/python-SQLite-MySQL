/*建立表格 primary key的另一種寫法*/
CREATE TABLE student(
	student_id SERIAL,
	name VARCHAR(20),
	major VARCHAR(20),
	PRIMARY KEY(student_id)
);

INSERT INTO student VALUES(1,'小白','歷史')
INSERT INTO student VALUES(2,'小黑','生物')
INSERT INTO student VALUES(3,'小綠',NULL)

/*primary key不可以重覆*/
/*INSERT INTO student VALUES(3,'小藍','小藍')*/

/*沒有填入的資料會成為NULL*/
INSERT INTO student(major,student_id) VALUES('英語',5)

/**/

SELECT * FROM student