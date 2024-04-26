'''
只顯示不同市場
和
不同日期的專案
'''

import psycopg2
import os
import streamlit as st
import pandas as pd
import numpy as np
from datetime import date

@st.cache_data
def getData(country:list[str],min,max):
    conn = psycopg2.connect(host="localhost",database='stock_market',user=os.environ["POSTGRES_USER"],password=os.environ["POSTGRES_PASSWORD"])

    with conn:
        with conn.cursor() as cursor:
            sql = '''
            SELECT date,adj_close,volume,股市.name,country
            FROM 股市 JOIN 市場 ON 股市.name = 市場.name
            WHERE 市場.country IN %s AND (股市.date BETWEEN %s AND %s);
            '''
            cursor.execute(sql,(country,min,max))
            all_data = cursor.fetchall()
            return all_data
    
    conn.close()

@st.cache_data
def get_country():
    conn = psycopg2.connect(host="localhost",database='stock_market',user=os.environ["POSTGRES_USER"],password=os.environ["POSTGRES_PASSWORD"])

    with conn:
        with conn.cursor() as cursor:
            sql = '''
            SELECT * FROM "市場"
            '''
            cursor.execute(sql)
            all_country = cursor.fetchall()
            return all_country
    
    conn.close()

@st.cache_data
def get_max_min_Date():
    conn = psycopg2.connect(host="localhost",database='stock_market',user=os.environ["POSTGRES_USER"],password=os.environ["POSTGRES_PASSWORD"])

    with conn:
        with conn.cursor() as cursor:
            sql = '''
            SELECT MAX(date),MIN(date) FROM 股市
            '''
            cursor.execute(sql)
            date = cursor.fetchone()
            return date
    
    conn.close()



st.title("大盤分析")
with st.sidebar:
    st.title("請選擇股票市場:")
    input_dict = dict(get_country()) #將list(tuple)轉為dict
    options:list[str] = st.multiselect("請選擇",input_dict.values(),default='台灣',placeholder="請選擇市場",label_visibility="hidden",key="markets")

#先建立一個session_state,因為key appointment要在後面才會建立   
max_date, min_date = get_max_min_Date()
if "appointment" not in st.session_state:
     st.session_state["appointment"] = [min_date, max_date]


all_data = getData(tuple(options),st.session_state["appointment"][0],  st.session_state["appointment"][1]) #傳入必需使用tuple
dataFrame = pd.DataFrame(all_data,columns=['日期','收盤','成交量','代號','國家'])
dataFrame['收盤'] = dataFrame['收盤'].astype('int')
#st.dataframe(dataFrame)
st.line_chart(data=dataFrame,x='日期',y='收盤',color='國家')


appointment = st.slider("請選擇一段時間:",
                        value=(min_date,max_date),key="appointment")

#st.write("your're scheduled for:",appointment)
#print(st.session_state["markets"])
#print(st.session_state["appointment"])