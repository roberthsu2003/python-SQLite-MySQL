/*constraints*/
DROP TABLE student;
CREATE TABLE student(
	student_id SERIAL,
	name VARCHAR(20) NOT NULL,/*不可以是NULL*/
	major VARCHAR(20) UNIQUE,/*不可以重覆*/
	PRIMARY KEY(student_id)
);
SELECT * FROM student

/*出錯 NOT NULL*/
INSERT INTO student VALUES(1, NULL, '英語')

/*出錯 major UNIQUE*/
INSERT INTO student VALUES(1, '小白', '英語')
INSERT INTO student VALUES(1, '小黑', '英語')

DROP TABLE student;
CREATE TABLE student(
	student_id SERIAL,
	name VARCHAR(20),
	major VARCHAR(20) DEFAULT '歷史',/*有預設值*/
	PRIMARY KEY(student_id)
);
/*可以,因為有預設值*/
INSERT INTO student VALUES(1, '小黑')



DROP TABLE student;
CREATE TABLE student(
	student_id SERIAL,
	name VARCHAR(20),
	major VARCHAR(20) DEFAULT '歷史',/*有預設值*/
	PRIMARY KEY(student_id)
);

/*使用SERIAL會自動遞增*/
INSERT INTO student(name,major) VALUES('小黑', '英語');
INSERT INTO student(name,major) VALUES('小白', '歷史');
SELECT * FROM student



