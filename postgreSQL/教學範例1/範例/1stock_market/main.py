import psycopg2
import os
import streamlit as st
import pandas as pd
import numpy as np

def getData(country):
    conn = psycopg2.connect(host="localhost",database='stock_market',user=os.environ["POSTGRES_USER"],password=os.environ["POSTGRES_PASSWORD"])

    with conn:
        with conn.cursor() as cursor:
            sql = '''
            SELECT date,adj_close,volume,股市.name,country
            FROM 股市 JOIN 市場 ON 股市.name = 市場.name
            WHERE 市場.country = %s
            '''
            cursor.execute(sql,[country])
            all_data = cursor.fetchall()
            return all_data

st.title("大盤分析")
all_data = getData('台灣')
dataFrame = pd.DataFrame(all_data,columns=['日期','收盤','成交量','代號','國家'])
dataFrame['收盤'] = dataFrame['收盤'].astype('int')
st.dataframe(dataFrame)
st.line_chart(data=dataFrame,x='日期',y='收盤')