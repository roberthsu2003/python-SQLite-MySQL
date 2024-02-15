/*取出市場資料*/
SELECT date,adj_close,volume,股市.name,country
FROM 股市 JOIN 市場 ON 股市.name = 市場.name
WHERE 市場.country = '台灣';

/*取出市場資料,使用in*/
SELECT date,adj_close,volume,股市.name,country
FROM 股市 JOIN 市場 ON 股市.name = 市場.name
WHERE 市場.country in('台灣','香港恒生');



/*取出市場*/
SELECT * FROM "市場" 

/*取出最大日期*/
SELECT MAX(date)
FROM 股市

/*取出最小日期*/
SELECT MIN(date)
FROM 股市



