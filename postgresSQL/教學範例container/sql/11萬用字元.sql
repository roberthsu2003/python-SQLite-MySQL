/*wildcards 萬用字元 %代表多個字元(也可以是無),_ 代表1個字元*/
/*1. 取得電話號碼尾數是335的客戶 */
SELECT * 
FROM client
WHERE phone LIKE '%335';

/*1. 取得電話號碼開頭是254的客戶 */
SELECT * 
FROM client
WHERE phone LIKE '254%';

/*1. 取得電話號碼中有354的客戶 */

SELECT * 
FROM client
WHERE phone LIKE '%354%';

/*2. 取得姓艾的客戶 */

SELECT * 
FROM client
WHERE client_name LIKE '艾%';

/*3. 取得生日在12月的員工*/
/*date操作https://www.commandprompt.com/education/how-to-query-date-and-time-in-postgresql*/
SELECT *
FROM employee
WHERE DATE_PART('MONTH',birth_date) = 12 