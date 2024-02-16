import psycopg2
import os
import streamlit as st
from pprint import pprint

@st.cache_data
def get_sarea():
    conn = psycopg2.connect(host="localhost",database='postgres',user=os.environ["POSTGRES_USER"],password=os.environ["POSTGRES_PASSWORD"])

    with conn:
        with conn.cursor() as cursor:
            #取出最新日期各站點資料
            sql = '''
                SELECT 行政區
                FROM 站點資訊
                GROUP BY 行政區
            '''
            cursor.execute(sql)
            allData = cursor.fetchall()
            return allData

    conn.close()

def info_sarea(sarea):
    conn = psycopg2.connect(host="localhost",database='postgres',user=os.environ["POSTGRES_USER"],password=os.environ["POSTGRES_PASSWORD"])

    with conn:
        with conn.cursor() as cursor:
            #取出各區最新資料
            sql = '''
            SELECT 日期,站點資訊.站點名稱,行政區,站點地址,lat,lng,總車輛,可借,可還,活動
            FROM youbike
            JOIN 站點資訊 ON youbike.編號 = 站點資訊.站點編號
            WHERE (日期,編號) IN (
	            SELECT MAX(日期),編號
	            FROM youbike
	            GROUP BY 編號
            ) AND 行政區 = %s;
            '''
            cursor.execute(sql,(sarea,))
            return cursor.fetchall()

    conn.close()

col1, col2 = st.columns([1,2])


data = [tuple1[0] for tuple1 in get_sarea()]
st.radio(
    "選擇行政區:",
    data,
    key='sarea',
    horizontal=True
)
#st.write(st.session_state.sarea)


data = info_sarea(st.session_state.sarea)
pprint(data)

data1 = [{'日期':item[0],'站點':item[1],'總車輛':item[6],'可借':item[7],'可還':item[8],'活動':item[9]}for item in data]

st.dataframe(data1)