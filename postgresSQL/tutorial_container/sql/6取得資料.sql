DROP TABLE student;
CREATE TABLE student(
	student_id SERIAL,
	name VARCHAR(20),
	major VARCHAR(20),
	score INT,
	PRIMARY KEY(student_id)
);
INSERT INTO student VALUES(1, '小白','英語',50);
INSERT INTO student VALUES(2, '小黃','生物',90);
INSERT INTO student VALUES(3, '小綠','歷史',70);
INSERT INTO student VALUES(4, '小藍','英語',80);
INSERT INTO student VALUES(5, '小黑','化學',20);

/*取得所有欄位*/
SELECT * FROM student;

/*取得name欄位*/
SELECT name FROM student;

/*取得name,major欄位*/
SELECT name,major FROM student;

/*排序預設為ascend*/
SELECT *
FROM student
ORDER BY score

/*排序由高至低*/
SELECT *
FROM student
ORDER BY score DESC

/*order by也可以多個欄位*/
SELECT *
FROM student
ORDER BY score,student_id

/*limit限制筆數*/
SELECT *
FROM student
LIMIT 3

/*limit和order by整合*/
SELECT *
FROM student
ORDER BY score
LIMIT 3

/*limit和order by整合*/
SELECT *
FROM student
ORDER BY score DESC
LIMIT 3

/*過濾WHERE*/
SELECT *
FROM student
WHERE major = '英語'

/*過濾WHERE*/
SELECT *
FROM student
WHERE major = '英語' AND student_id=1

/*過濾WHERE*/
SELECT *
FROM student
WHERE major = '英語'  OR score > 60

/*過濾WHERE,使用IN,等同於使用IN*/
SELECT *
FROM student
WHERE major = '英語'  OR major='生物' OR major='歷史'

SELECT *
FROM student
WHERE major in('英語','生物','歷史')















