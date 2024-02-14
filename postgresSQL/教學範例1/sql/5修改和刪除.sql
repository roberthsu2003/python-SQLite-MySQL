/*修改和刪除*/
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
SELECT * FROM student;

/*將英語更改為英語文學*/
UPDATE student
SET major='英語文學'
WHERE major='英語';

/*將student_id 3,改為生物*/
UPDATE student
SET major='生物'
WHERE student_id=3;

/*將生物和化學改為生化*/
UPDATE student
SET major='生化'
WHERE major='生物' OR major='化學';

/*將student_id是1的,同時修改name和major*/
UPDATE student
SET name='小灰',major='物理'
WHERE student_id=1;

/*沒有where*/
UPDATE student
SET major='物理';

SELECT * FROM student;

/*刪除student_id=3的資料*/
DELETE FROM student
WHERE student_id=3;


/*刪除name=小灰同時major=物理*/
DELETE FROM student
WHERE name='小灰' AND major='物理';

/*刪除score < 60的資料*/
DELETE FROM student
WHERE score < 60;

/*刪除score不等於80的資料*/
DELETE FROM student
WHERE score <> 80;

/*刪除所有資料*/
DELETE FROM student

