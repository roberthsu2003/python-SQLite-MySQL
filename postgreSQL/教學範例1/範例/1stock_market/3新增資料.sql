/*有發生限制衝突,不做任何事的語法*/
INSERT INTO 市場 values ('^TWII','台灣')
ON CONFLICT DO NOTHING;

SELECT * FROM 市場

/*股市資料*/
INSERT INTO 股市(date,open,high,low,close,adj_close,volume,name) 
values('1997-07-08',9094.26953125,9124.2998046875,8988.1298828125,8996.7197265625,8996.6865234375,0,'^TWII')

SELECT * FROM 股市
WHERE name = '^HSI'



