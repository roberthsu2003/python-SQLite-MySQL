/*使用火車站進出人數*/
/*stations,gate_count*/

/*取出所有欄位*/
SELECT * 
FROM gate_count LEFT JOIN stations ON 站點編號 = 編號

/*取出指定欄位*/
SELECT 日期,進站人數,出站人數,名稱,地名,地址,youbike
FROM gate_count LEFT JOIN stations ON 站點編號 = 編號