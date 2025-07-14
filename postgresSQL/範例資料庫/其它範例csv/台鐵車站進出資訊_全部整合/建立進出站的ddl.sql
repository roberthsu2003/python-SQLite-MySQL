-- public.台鐵車站資訊 definition

-- Drop table

-- DROP TABLE 台鐵車站資訊;

CREATE TABLE 台鐵車站資訊 (
	"stationCode" int4 NOT NULL,
	"stationName" varchar(50) NULL,
	"name" varchar(50) NULL,
	"stationAddrTw" varchar(50) NULL,
	"stationTel" varchar(50) NULL,
	gps varchar(50) NULL,
	"haveBike" varchar(50) NULL,
	CONSTRAINT 台鐵車站資訊_pkey PRIMARY KEY ("stationCode")
);


-- public.每日各站進出站人數 definition

-- Drop table

-- DROP TABLE 每日各站進出站人數;

CREATE TABLE 每日各站進出站人數 (
	日期 date NULL,
	車站代碼 int4 NULL,
	進站人數 int4 NULL,
	出站人數 int4 NULL,
	CONSTRAINT 每日各站進出站人數_車站代碼_fkey FOREIGN KEY (車站代碼) REFERENCES 台鐵車站資訊("stationCode")
);