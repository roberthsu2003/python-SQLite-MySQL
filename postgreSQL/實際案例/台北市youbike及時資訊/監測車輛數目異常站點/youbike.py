import dataSource
import tkinter as tk
from datetime import datetime
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        #上方的Frame=========start
        topFrame = tk.Frame(self)
        tk.Label(topFrame,text="台北市youbike即時監測系統",font=("arial",20)).pack()
        tk.Label(topFrame,text="(每隔1分鐘更新)",font=("arial",16)).pack()
        topFrame.grid(column=0,row=0,columnspan=3,padx=20,pady=20)
        #上方的Frame=========end
        self.leftLabelFrame =LeftLabelFrame(self,text="左邊的")
        self.leftLabelFrame.grid(column=0,row=1,padx=20,pady=20)
        self.centerLabelFrame = CenterLabelFrame(self,text="中間的")
        self.centerLabelFrame.grid(column=1,row=1,padx=20,pady=20)
        self.rightLabelFrame = RightLabelFrame(self,text="右邊的")
        self.rightLabelFrame.grid(column=2, row=1, padx=20, pady=20)
        self.update_data()


    def update_data(self):
        nowString = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.leftLabelFrame.configure(text=nowString)
        self.centerLabelFrame.configure(text=nowString)
        self.rightLabelFrame.configure(text=nowString)
        dataSource.update_youbike_data()
        self.leftLabelFrame.clear_treeView()
        self.leftLabelFrame.display_treeView()
        self.centerLabelFrame.clear_treeView()
        self.centerLabelFrame.display_treeView()
        self.rightLabelFrame.clear_treeView()
        self.rightLabelFrame.display_treeView()
        print("update")
        self.updateId = self.after(1000 * 60, self.update_data)

class LeftLabelFrame(tk.LabelFrame):
    def __init__(self, *args , **kwargs):
        super().__init__(*args, **kwargs)
        topFrame = tk.Frame(self,background='gray')
        tk.Label(topFrame, text="正常租借站點", font=("arial", 20),background='gray',fg="white").pack(padx=10,pady=10)
        normal_count = dataSource.get_count_of_normal()
        tk.Label(topFrame, text=f"數量:{normal_count}",background='gray',fg='#ffffff', font=("arial",20)).pack(padx=10,pady=10)
        topFrame.pack(pady=20)
        self.treeView = ttk.Treeview(self,columns=('sna','tot','sbi','bemp'),show="headings")
        self.treeView.heading('sna',text='名稱')
        self.treeView.heading('tot', text='總數')
        self.treeView.heading('sbi', text='可借')
        self.treeView.heading('bemp', text='可還')

        self.treeView.column('sna',width=200)
        self.treeView.column('tot',width=50)
        self.treeView.column('sbi',width=50)
        self.treeView.column('bemp',width=50)
        self.treeView.pack()
        self.display_treeView()

    def clear_treeView(self):
        # 清除tree內容
        for i in self.treeView.get_children():
            self.treeView.delete(i)

    def display_treeView(self):
        normal_list = dataSource.get_list_of_normal()
        for item in normal_list:
            itemList = list(item.values())
            self.treeView.insert('', 'end', values=itemList)

class CenterLabelFrame(tk.LabelFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        topFrame = tk.Frame(self, background='gray')
        tk.Label(topFrame, text="可租用少於3台", font=("arial", 20), background='gray', fg="white").pack(padx=10, pady=10)
        normal_count = dataSource.get_count_of_less_bike()
        tk.Label(topFrame, text=f"數量:{normal_count}", background='gray', fg='#ffffff', font=("arial", 20)).pack(padx=10,
                                                                                                                pady=10)
        topFrame.pack(pady=20)
        self.treeView = ttk.Treeview(self, columns=('sna', 'tot', 'sbi', 'bemp'), show="headings")
        self.treeView.heading('sna', text='名稱')
        self.treeView.heading('tot', text='總數')
        self.treeView.heading('sbi', text='可借')
        self.treeView.heading('bemp', text='可還')

        self.treeView.column('sna', width=200)
        self.treeView.column('tot', width=50)
        self.treeView.column('sbi', width=50)
        self.treeView.column('bemp', width=50)
        self.treeView.pack()
        self.display_treeView()

    def clear_treeView(self):
        # 清除tree內容
        for i in self.treeView.get_children():
            self.treeView.delete(i)

    def display_treeView(self):
        less_list = dataSource.get_list_of_less_bike()
        for item in less_list:
            itemList = list(item.values())
            self.treeView.insert('', 'end', values=itemList)

class RightLabelFrame(tk.LabelFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        topFrame = tk.Frame(self, background='gray')
        tk.Label(topFrame, text="可還車量少於3台", font=("arial", 20), background='gray', fg="white").pack(padx=10, pady=10)
        normal_count = dataSource.get_count_of_less_stop()
        tk.Label(topFrame, text=f"數量:{normal_count}", background='gray', fg='#ffffff', font=("arial", 20)).pack(padx=10,
                                                                                                                pady=10)
        topFrame.pack(pady=20)
        self.treeView = ttk.Treeview(self, columns=('sna', 'tot', 'sbi', 'bemp'), show="headings")
        self.treeView.heading('sna', text='名稱')
        self.treeView.heading('tot', text='總數')
        self.treeView.heading('sbi', text='可借')
        self.treeView.heading('bemp', text='可還')

        self.treeView.column('sna', width=200)
        self.treeView.column('tot', width=50)
        self.treeView.column('sbi', width=50)
        self.treeView.column('bemp', width=50)
        self.treeView.pack()
        self.display_treeView()

    def clear_treeView(self):
        # 清除tree內容
        for i in self.treeView.get_children():
            self.treeView.delete(i)

    def display_treeView(self):
        less_stop_list = dataSource.get_list_of_less_stop()
        for item in less_stop_list:
            itemList = list(item.values())
            self.treeView.insert('', 'end', values=itemList)

if __name__=="__main__":
    dataSource.update_youbike_data()
    window = Window()
    window.title("台北市youbike及時監測資料")
    window.mainloop()
