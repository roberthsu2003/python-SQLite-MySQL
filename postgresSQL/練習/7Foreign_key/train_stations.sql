/*請參考火車站點.csv和火車進出人數資料*/
DROP TABLE IF EXISTS stations;
DROP TABLE IF EXISTS gate_count;

CREATE TABLE IF NOT EXISTS stations(
	編號 VARCHAR PRIMARY KEY, /*0900*/
	名稱 VARCHAR(20) NOT NULL,
	英文名稱 VARCHAR(50),
	地名 VARCHAR(20),
	英文地名 VARCHAR(50),
	地址 VARCHAR(255),
	英文地址 VARCHAR(255),
	電話 VARCHAR(20),
	gps VARCHAR(50),
	youbike BOOL
);
