/*constraints*/
DROP TABLE student;
CREATE TABLE student(
	student_id SERIAL,
	name VARCHAR(20) NOT NULL,/*不可以是NULL*/
	major VARCHAR(20) UNIQUE,/*不可以重覆*/
	PRIMARY KEY(student_id)
);
