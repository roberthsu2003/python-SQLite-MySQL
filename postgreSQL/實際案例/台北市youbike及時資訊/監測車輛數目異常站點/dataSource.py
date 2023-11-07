import requests
from requests import ConnectionError,HTTPError,Timeout
import pymysql.cursors
from pymysql import Error

databasName = 'youbike.db'


__all__ = ['update_youbike_data','get_count_of_normal','get_list_of_normal']

def create_connection():
    connection = None
    try:
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='12341234',
                                     database='world',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
    except Error as e:
        print(e)
    return connection

def download_youbike_data():
    youbikeurl = "https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.json"
    try:
        response = requests.get(youbikeurl)
        response.raise_for_status()
    except ConnectionError as e:
        print("網路連線有問題")
        print(e)
        return
    except HTTPError as e:
        print("statusCode不是200,連線取得資料有問題")
        print(e)
        return
    except Timeout as e:
        print("伺服器忙線中")
        print(e)
        return
    except:
        print("不預期的錯誤")
        return

    allData = response.json()
    #解析資料,傳出[{:}]
    return list(allData["retVal"].values())





def create_table(conn):
    create_table_sql = '''
    CREATE TABLE IF NOT EXISTS youbike (
	id BIGINT AUTO_INCREMENT,
	sno VARCHAR(6) NOT NULL,
	sna VARCHAR(50),
	tot SMALLINT UNSIGNED ,
	sbi SMALLINT UNSIGNED ,
	sarea VARCHAR(10) ,
	mday DATETIME,
	lat REAL,
	lng REAL,
	ar VARCHAR(100),
	bemp SMALLINT UNSIGNED,
	act TINYINT,
	PRIMARY KEY(id),
	UNIQUE (sno)
    );
    '''
    with conn.cursor() as cursor:
        try:
            cursor.execute(create_table_sql)
        except Error as e:
            print(e)



from datetime import datetime
def update_data(conn,downloadData):
    def change_datetime_format(d):
        datetime_object = datetime.strptime(d,'%Y%m%d%H%M%S')
        return datetime_object.strftime('%Y-%m-%d %H:%M:%S')


    replace_into_sql = '''
    REPLACE INTO youbike(sno,sna,tot,sbi,sarea,mday,lat,lng,ar,bemp,act)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
    '''
    with conn.cursor() as cursor:
        for item in downloadData:
            sno = item['sno']
            sna = item['sna']
            tot = int(item['tot'])
            sbi = int(item['sbi'])
            sarea = item['sarea']
            mday = change_datetime_format(item['mday'])
            lat = float(item['lat'])
            lng = float(item['lng'])
            ar = item['ar']
            bemp = int(item['bemp'])
            act = int(item['act'])
            cursor.execute(replace_into_sql,(sno,sna,tot,sbi,sarea,mday,lat,lng,ar,bemp,act))
        conn.commit()





def update_youbike_data():
    datalist = download_youbike_data()
    conn = create_connection()
    with conn:
        create_table(conn)
        update_data(conn,datalist)


def get_count_of_normal():
    conn = create_connection()
    sql = '''
    SELECT count(*) as 正常數量
    FROM youbike
    WHERE act = 1 AND sbi > 3 AND bemp >3
    '''
    with conn:
        with conn.cursor() as cursor:
            try:
                cursor.execute(sql)
                row = cursor.fetchone()
                print(row)
            except Error as e:
                print(e)
    return row['正常數量']

def get_list_of_normal():
    conn = create_connection()
    sql = '''
        SELECT sna,tot,sbi,bemp
        FROM youbike
        WHERE act = 1 AND sbi > 3 AND bemp >3
        '''
    with conn:
        with conn.cursor() as cursor:
            try:
                cursor.execute(sql)
                rows = cursor.fetchall()
                print(rows)
            except Error as e:
                print(e)
    return rows

def get_count_of_less_bike():
    conn = create_connection()
    sql = '''
    SELECT count(*) as 正常數量
    FROM youbike
    WHERE act = 1 AND sbi <= 3
    '''
    with conn:
        with conn.cursor() as cursor:
            try:
                cursor.execute(sql)
                row = cursor.fetchone()
                print(row)
            except Error as e:
                print(e)
    return row['正常數量']

def get_list_of_less_bike():
    conn = create_connection()
    sql = '''
        SELECT sna,tot,sbi,bemp
        FROM youbike
        WHERE act = 1 AND sbi <= 3
        '''
    with conn:
        with conn.cursor() as cursor:
            try:
                cursor.execute(sql)
                rows = cursor.fetchall()
                print(rows)
            except Error as e:
                print(e)
    return rows

def get_count_of_less_stop():
    conn = create_connection()
    sql = '''
    SELECT count(*) as 正常數量
    FROM youbike
    WHERE act = 1 AND bemp <= 3 
    '''
    with conn:
        with conn.cursor() as cursor:
            try:
                cursor.execute(sql)
                row = cursor.fetchone()
                print(row)
            except Error as e:
                print(e)
    return row['正常數量']

def get_list_of_less_stop():
    conn = create_connection()
    sql = '''
        SELECT sna,tot,sbi,bemp
        FROM youbike
        WHERE act = 1 AND bemp <= 3
        '''
    with conn:
        with conn.cursor() as cursor:
            try:
                cursor.execute(sql)
                rows = cursor.fetchall()
                print(rows)
            except Error as e:
                print(e)
    return rows









