import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from source import *

window = tk.Tk()

# 修改視窗大小
window.geometry('300x200')
window.resizable(False, False)
window.title('選擇世界洲名')

# label顯示標題
label = ttk.Label(window,text="請選擇洲名")
label.pack(fill=tk.X, padx=5, pady=5)


# 建立下拉式表單
selected_continent = tk.StringVar()
selected_continent.set('請選擇')
combobox = ttk.Combobox(window, textvariable=selected_continent)
combobox.pack()

#提供資料
combobox['values'] = get_continent()

#預防使用者打字
combobox['state'] = 'readonly'

#使用者選擇的動作

def user_change(event):
    showinfo(
        title='結果',
        message=f'您的選擇:{selected_continent.get()}!'
    )
#綁定事件
combobox.bind('<<ComboboxSelected>>', user_change)


tk.mainloop()