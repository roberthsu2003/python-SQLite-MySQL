# 選擇洲名後再選擇國家名稱,顯示出國家最新的確診數和死亡率
1. 主程式 - lesson3.py
2. 資料庫操作 - source.py
3. 現成資料庫 - world.db

![](./images/pic1.png)

## lesson3.py

```python
import tkinter as tk
from tkinter import ttk
from source import *

window = tk.Tk()

# 修改視窗大小
#window.geometry('300x200')
window.resizable(False, False)
window.title('練習3')

#建立labelFrame
leftFrame = ttk.LabelFrame(window,text='洲名')
leftFrame.grid(column=0,row=0,padx=20,pady=20,sticky="N")



# label顯示標題
leftlabel = ttk.Label(leftFrame,text="請選擇洲名")
leftlabel.pack(fill=tk.X, padx=5, pady=5)


# 建立下拉式表單
selected_continent = tk.StringVar()
selected_continent.set('請選擇')
combobox = ttk.Combobox(leftFrame, textvariable=selected_continent)
combobox.pack()

#建立rightFrame
rightFrame = ttk.LabelFrame(window,text='國家名')
rightFrame.grid(column=1,row=0,padx=20,pady=20)

# rightlabel顯示標題
rightlabel = ttk.Label(rightFrame,text="請選擇國家名稱")
rightlabel.pack(fill=tk.X, padx=5, pady=5)





#提供洲資料
combobox['values'] = get_continent()

#預防使用者打字
combobox['state'] = 'readonly'

#使用者選擇洲的動作
def user_change(event):
    listbox.configure(state=tk.NORMAL)
    continent = selected_continent.get()
    print(get_country_by_continent(continent))
    choicesvar.set(get_country_by_continent(continent))

#綁定事件
combobox.bind('<<ComboboxSelected>>', user_change)

#建立listbox
choices = ["先選取洲"]
choicesvar = tk.StringVar(value=choices)
listbox = tk.Listbox(rightFrame, height=10,listvariable=choicesvar,state=tk.DISABLED)
listbox.pack(padx=10,pady=10)

#使用者選擇國家的動作
def select_country(event):
    # 換洲名稱時，會執行listbox的select_country()事件,會產生錯誤,因為country_index的內容是(),所以要檢查是不是空的
    country_index = listbox.curselection()
    if not country_index:
        return

    selected_country = listbox.get(country_index)
    country_details = get_country_detailData(selected_country) #取得國家資料
    #清除所有資料
    for i in tree.get_children():
        tree.delete(i)

    #顯示國家資料至tree
    for country in country_details:
        tree.insert('', tk.END, values=country)



#綁定事件
listbox.bind("<<ListboxSelect>>",select_country)



#建立treeView
columns = ('國家','日期','總確診數','新增確診數','總死亡數','新增死亡數')
tree = ttk.Treeview(window, columns=columns, show='headings')
tree.heading('國家', text='國家')
tree.column('國家', minwidth=0, width=150, stretch=tk.NO)
tree.heading('日期', text='日期')
tree.column('日期', minwidth=0, width=100, stretch=tk.NO)
tree.heading('總確診數', text='總確診數')
tree.column('總確診數', minwidth=0, width=100, stretch=tk.NO)
tree.heading('新增確診數', text='新增確診數')
tree.column('新增確診數', minwidth=0, width=100, stretch=tk.NO)
tree.heading('總死亡數',text='總死亡數')
tree.column('總死亡數', minwidth=0, width=100, stretch=tk.NO)
tree.heading('新增死亡數',text='新增死亡數')
tree.column('新增死亡數', minwidth=0, width=100, stretch=tk.NO)
tree.grid(column=0,row=1,padx=20,pady=20,columnspan=2)
tk.mainloop()
```

## soruce.py

```python
import sqlite3
from sqlite3 import Error

def __create_connection(db_file):
    """
    建立資料庫和連線至資料庫
    :param db_file: 資料庫的檔案名稱
    :return: Connection物件
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)

    return conn


def __select_continent(conn):
    """
    選取world資料表
    :param conn:Connection物件
    :return:list
    """
    cursor = conn.cursor()
    sql = '''
    SELECT DISTINCT 洲名
    FROM world
    WHERE 洲名 IS NOT NULL
    '''
    cursor.execute(sql)
    rows = cursor.fetchall()
    continents = [row for row in rows if row is not None]
    return continents

def __selected_country_by_continent(conn, continent):
    cursor = conn.cursor()
    sql = '''
        SELECT DISTINCT 國家
        FROM world
        WHERE 洲名 = ?
        '''
    cursor.execute(sql,(continent,))
    rows = cursor.fetchall()
    selected_country = [row[0] for row in rows]
    return selected_country

def __selected_country_detail(conn,country_name):
    cursor = conn.cursor()
    sql = '''
    SELECT 國家,日期,總確診數,新增確診數,總死亡數,新增死亡數
    FROM world
    WHERE 國家 = ?
    ORDER BY 日期 DESC
    '''
    cursor.execute(sql, (country_name,))
    rows = cursor.fetchall()
    country_details = [row for row in rows]
    return country_details

def get_continent():
    database = "world.db"
    #建立資料庫和Connection物件
    conn = __create_connection(database)
    with conn:
        continents = __select_continent(conn)
        return continents
    return []

def get_country_by_continent(continent):
    database = "world.db"
    # 建立資料庫和Connection物件
    conn = __create_connection(database)
    with conn:
        countries = __selected_country_by_continent(conn,continent)
        return countries
    return []

def get_country_detailData(country):
    database = "world.db"
    # 建立資料庫和Connection物件
    conn = __create_connection(database)
    with conn:
        country_details =  __selected_country_detail(conn, country)
        return country_details
    return []

```