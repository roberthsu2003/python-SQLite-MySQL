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