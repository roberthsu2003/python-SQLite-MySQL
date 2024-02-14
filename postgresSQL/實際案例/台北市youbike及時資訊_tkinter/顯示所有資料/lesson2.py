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

        def update_button_click():
            youbikeInfo = dataSource.loadDataFraomYouBikeTP()
            dataSource.update_data(youbikeInfo)
            self.display_treeView()

        tk.Button(topFrame, text="更新及時資料", padx=40, pady=20, command=update_button_click).pack(pady=20)
        topFrame.pack(padx=20, pady=20)
        # topFrame ========== 結束

        #bottomFrame ==========開始
        bottomFrame = tk.Frame(self, relief=tk.GROOVE, borderwidth=1, width=300, height=200)
        self.tree = ttk.Treeview(bottomFrame, columns=('id', 'sno', 'sna', 'tot', 'sbi', 'sarea','mday','lat','lng','ar','bemp','act'), show='headings')
        self.tree.heading('id',text="編號")
        self.tree.heading('sno',text='站點編號')
        self.tree.heading('sna',text='站點名稱')
        self.tree.heading('tot', text='總停車格')
        self.tree.heading('sbi', text='可借車輛數量')
        self.tree.heading('sarea',text= '場站區域')
        self.tree.heading('mday', text='資料更新時間')
        self.tree.heading('lat', text='緯度')
        self.tree.heading('lng',text='經度')
        self.tree.heading('ar', text='地點')
        self.tree.heading('bemp',text='空位數量')
        self.tree.heading('act', text='狀態')

        self.tree.column('id',width=50)
        self.tree.column('sno', width=50)
        self.tree.column('sna', width=120)
        self.tree.column('tot', width=50,anchor=tk.CENTER)
        self.tree.column('sbi', width=100,anchor=tk.CENTER)
        self.tree.column('sarea', width=50)
        self.tree.column('mday', width=150)
        self.tree.column('lat', width=50)
        self.tree.column('lng', width=50)
        self.tree.column('ar', width=250)
        self.tree.column('bemp', width=50,anchor=tk.CENTER)
        self.tree.column('act', width=50,anchor=tk.CENTER)
        self.tree.pack(side=tk.TOP)

        bottomFrame.pack(padx=20, pady=20)
        #bottomFrame ==========結束
        self.display_treeView()

    def display_treeView(self):
        #清除tree內容
        for i in self.tree.get_children():
            self.tree.delete(i)

        all_siteInfos = dataSource.get_siteInfo()
        #all_siteInfos[{}]
        for one_site in all_siteInfos:
            id = one_site['id']
            sno = one_site['sno']
            sna = one_site['sna']
            tot = one_site['tot']
            sbi = one_site['sbi']
            sarea = one_site['sarea']
            mday = one_site['mday']
            #轉換mday為字串格式
            mday = mday.strftime('%Y-%m-%d %H:%M:%S')
            lat = one_site['lat']
            lng = one_site['lng']
            ar = one_site['ar']
            bemp = one_site['bemp']
            act = one_site['act']
            siteInfo = (id,sno,sna,tot,sbi,sarea,mday,lat,lng,ar,bemp,act)
            self.tree.insert('', tk.END, values=siteInfo)









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