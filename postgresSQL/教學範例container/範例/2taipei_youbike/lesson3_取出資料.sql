SELECT count(*) AS 筆數
FROM youbike

/*先測試這筆,才可以了解下面*/
SELECT MAX(日期),編號
FROM youbike
GROUP BY 編號;


/*取出最新時間youbike資料*/
SELECT 日期,站點資訊.站點名稱,行政區,站點地址,lat,lng,總車輛,可借,可還,可借,活動
FROM youbike
JOIN 站點資訊 ON youbike.編號 = 站點資訊.站點編號
WHERE (日期,編號) IN (
	SELECT MAX(日期),編號
	FROM youbike
	GROUP BY 編號
)
/*取出行政區*/
SELECT 行政區
FROM 站點資訊
GROUP BY 行政區

/*取出最新時間youbike資料,依據行政區*/
SELECT 日期,站點資訊.站點名稱,行政區,站點地址,lat,lng,總車輛,可借,可還,可借,活動
FROM youbike
JOIN 站點資訊 ON youbike.編號 = 站點資訊.站點編號
WHERE (日期,編號) IN (
	SELECT MAX(日期),編號
	FROM youbike
	GROUP BY 編號
) AND 行政區 = '大安區';




