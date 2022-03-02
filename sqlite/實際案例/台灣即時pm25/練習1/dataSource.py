#!/usr/bin/python3.10
import requests
import sqlite3
from sqlite3 import Error

urlpath = '	https://data.epa.gov.tw/api/v1/aqx_p_02?limit=1000&api_key=9be7b239-557b-4c10-9775-78cadfc555e9&sort=ImportDate%20desc&format=json'

def create_connection(db_file):
    """
    連線至資料庫
    :param db_file: 資料庫的檔案名稱
    :return: Connection物件
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
        return

    return conn

def delete_table_pm25(conn):
    sql = 'DROP TABLE pm25;'
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()

def create_table_pm25(conn):
    sql = ''' 
    CREATE TABLE IF NOT EXISTS pm25 (
	id INTEGER PRIMARY KEY,
	站點 TEXT,
	城市 TEXT,
	pm25 REAL,
	日期 TEXT,
	單位 TEXT
    );
    '''
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()

def insert_pm25(conn, values):
    """
    新增資料至projects資料庫
    :param conn:Connection物件
    :param project:tuple(加入至資料庫的內容)
    :return:自動建立id的最後一筆
    """
    sql = ''' 
    INSERT INTO pm25 (站點,城市,pm25,日期,單位)
    VALUES (?,?,?,?,?)
    '''
    cursor = conn.cursor()
    cursor.execute(sql, values)
    conn.commit()




def saveToDataBase(datas):
    '''
    儲存資料至資料庫db25
    :param datas: list->tuple
    :return:
    '''
    conn = create_connection('pm25.db')
    print("資料庫連線成功")
    with conn:
        delete_table_pm25(conn) #刪除資料表
        create_table_pm25(conn) #建立資料表
        for value in datas:
            insert_pm25(conn, value) #插入資料


def downloadData():
    def stringToFloat(s):
        try:
            return float(s)
        except:
            return 999.0
    response = requests.get(urlpath)
    if response.status_code == 200:
        print('下載成功')
        data = response.json()
        datas = data["records"]
        importData = [
            (item['Site'], item['county'], stringToFloat(item['PM25']), item['DataCreationDate'], item['ItemUnit']) for
            item in datas]
        return importData

def download_save_to_DataBase():
    importData = downloadData()
    saveToDataBase(importData)

def get_city_name():
    conn = create_connection('pm25.db')
    print("資料庫連線成功")

    sql = ''' 
        SELECT DISTINCT 城市
        FROM pm25
        '''
    with conn:
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        city_name_list = [row[0] for row in rows]
        return  city_name_list
