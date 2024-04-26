/*插入站點資訊*/
INSERT INTO 站點資訊 
VALUES('500101001','YouBike2.0_捷運科技大樓站','大安區','復興南路二段235號前',25.02605,121.5436)
ON CONFLICT DO NOTHING;

SELECT count(*)
FROM 站點資訊

/*插入youbike資訊*/
INSERT INTO youbike
VALUES('2024-02-16 10:48:19','500101001',28,1,27,true)
ON CONFLICT DO NOTHING;

SELECT count(*)
FROM youbike