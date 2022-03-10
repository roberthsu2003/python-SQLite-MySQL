import dataSource
import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        # topFrame ========== 開始
        topFrame = tk.Frame(self, relief=tk.GROOVE, borderwidth=1, width=300, height=200)
        tk.Label(topFrame, text="台北市youbike及時資訊", font=("arial", 20), bg="#333333", fg='#ffffff', padx=10, pady=10).pack(
            pady=20,padx=20)

        def buttonClick():
            youbikeInfo = dataSource.loadDataFraomYouBikeTP()
            dataSource.update_data(youbikeInfo)

        tk.Button(topFrame, text="更新及時資料", padx=40, pady=20, command=buttonClick).pack(pady=20)
        topFrame.pack(padx=20, pady=20)
        # topFrame ========== 結束






if __name__ == "__main__":
    #下載資料和顯示資料
    youbikeInfo = dataSource.loadDataFraomYouBikeTP()
    dataSource.update_data(youbikeInfo)

    #視窗介面
    window = Window()
    window.resizable(0, 0) #無法改變視窗大小
    window.geometry("+300+300")
    window.title("台北市youbike及時資訊")
    window.mainloop()