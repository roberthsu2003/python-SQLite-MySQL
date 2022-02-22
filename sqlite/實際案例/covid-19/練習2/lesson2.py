import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from source import *

window = tk.Tk()

# 修改視窗大小
#window.geometry('300x200')
window.resizable(False, False)
window.title('練習2')

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
    print(selected_country)



#綁定事件
listbox.bind("<<ListboxSelect>>",select_country)


#提供資料
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




tk.mainloop()