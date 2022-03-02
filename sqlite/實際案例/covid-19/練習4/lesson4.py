import tkinter as tk
from tkinter import ttk
from tkinter import font
from source import *

window = tk.Tk()

# 修改視窗大小
#window.geometry('300x200')
window.resizable(False, False)
window.title('練習4')

#建立字型和大小
print(font.families())
highlightFont = font.Font(family='Helvetica', size=20, weight='bold')

#建立labelFrame
titleLable = ttk.Label(window,text="全球確診和死亡排名搜尋",font=highlightFont,anchor=tk.CENTER)
titleLable.pack(fill=tk.X,padx=10,pady=10)

#建立全球總確診數
case_title = ttk.Label(window,text="全球各國確診排名",anchor=tk.E)
case_title.pack(padx=10,pady=(10,5))

#建立spinbox
case_spinval = tk.StringVar()
case_spin = ttk.Spinbox(window, from_=1.0, to=100.0, textvariable=case_spinval)
case_spin.state(['readonly'])
case_spin.pack()

#建立全球總死亡排名
death_title = ttk.Label(window,text="全球各國死亡人數排名",anchor=tk.E)
death_title.pack(padx=10,pady=(10,5))

#建立spinbox
death_spinval = tk.StringVar()
death_spin = ttk.Spinbox(window, from_=1.0, to=100.0, textvariable=death_spinval)
death_spin.state(['readonly'])
death_spin.pack()


#建立treeView
columns = ('國家','日期','總確診數','總死亡數',)
tree = ttk.Treeview(window, columns=columns, show='headings')
tree.heading('國家', text='國家')
tree.column('國家', minwidth=0, width=150, stretch=tk.NO)
tree.heading('日期', text='日期')
tree.column('日期', minwidth=0, width=100, stretch=tk.NO)
tree.heading('總確診數', text='總確診數')
tree.column('總確診數', minwidth=0, width=100, stretch=tk.NO)
tree.heading('總死亡數',text='總死亡數')
tree.column('總死亡數', minwidth=0, width=100, stretch=tk.NO)
tree.pack(padx=10,pady=10)






















tk.mainloop()