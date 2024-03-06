/*進站人數最多的一筆*/
SELECT *
FROM gate_count LEFT JOIN stations ON 站點編號 = 編號
WHERE 進站人數=(SELECT MAX(進站人數)
				FROM gate_count);
				
/*各站點進站人數最多的一筆*/
SELECT *
FROM gate_count LEFT JOIN stations ON 站點編號 = 編號
WHERE (站點編號,進站人數) IN (
	SELECT 站點編號,MAX(進站人數)
	FROM gate_count
	GROUP BY 站點編號
);
