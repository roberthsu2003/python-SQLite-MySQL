import dataSource
import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        # topFrame ========== 開始
        topFrame = tk.Frame(self, relief=tk.GROOVE, borderwidth=1, width=300, height=200)
        tk.Label(topFrame, text="台灣股市交易歷史資料查詢", font=("arial", 20), bg="#333333", fg='#ffffff', padx=10, pady=10).pack(
            pady=20,padx=20)
        self.entryContent = tk.StringVar(value='請輸入股票編號')  # 控制使用者輸入內容的實體
        tk.Entry(topFrame, textvariable=self.entryContent, font=("arial", 20), width=15).pack()

        tk.Button(topFrame, text="更新及時資料", padx=40, pady=20).pack(pady=20)
        topFrame.pack(padx=20, pady=20)
        # topFrame ========== 結束

        #bottomFrame ==========開始
        bottomFrame = tk.Frame(self, relief=tk.GROOVE, borderwidth=1, width=300, height=200)
        self.tree = ttk.Treeview(bottomFrame, columns=('name','date', 'hight', 'low', 'open', 'close','volume','adj_close'), show='headings')
        self.tree.heading('name',text="編號")
        self.tree.heading('date',text='日期')
        self.tree.heading('hight',text='最高')
        self.tree.heading('low', text='最低')
        self.tree.heading('open', text='開盤')
        self.tree.heading('close',text= '收盤')
        self.tree.heading('volume', text='成交量')
        self.tree.heading('adj_close', text='最終收盤價')
        self.tree.column('name',width=100,anchor=tk.CENTER)
        self.tree.column('date', width=120,anchor=tk.CENTER)
        self.tree.column('hight', width=50,anchor=tk.CENTER)
        self.tree.column('low', width=50,anchor=tk.CENTER)
        self.tree.column('open', width=50,anchor=tk.CENTER)
        self.tree.column('close', width=50,anchor=tk.CENTER)
        self.tree.column('volume', width=150,anchor=tk.CENTER)
        self.tree.column('adj_close', width=150,anchor=tk.CENTER)
        self.tree.pack(side=tk.TOP)
        bottomFrame.pack(padx=20, pady=20)
        #bottomFrame ==========結束


    def display_treeView(self):
        #清除tree內容
        for i in self.tree.get_children():
            self.tree.delete(i)

if __name__ == "__main__":
    #視窗介面
    window = Window()
    window.resizable(0, 0) #無法改變視窗大小
    window.geometry("+300+300")
    window.title("台灣股市交易歷史資料查詢")
    window.mainloop()




