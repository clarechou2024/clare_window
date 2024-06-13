import data
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk


class Window(ThemedTk):       ##建立Window視窗
    def __init__(self,theme:str|None,**kwargs):    #**kwargs:沒有限定名稱的呼叫
        super().__init__(**kwargs)
        try:
            ubike:list[dict] = data.load_data()
        except Exception as error:
            print(error)
        else:
            print(ubike)
        self.title("YouBike2.0 臺北市公共自行車即時資訊")
        self.geometry('500x200')
        self.resizable(False, False)

        #建立treeveiw
        treeview_frame = ttk.Frame(self)
        treeview_frame.pack()

        # 設定欄位
        columns = ('sna', 'sarea', 'mday', 'ar', 'act', 'updateTime', 'total', 'rent_bikes', 'lat', 'lng', 'retuen_bikes')
        self.treeview = ttk.Treeview(treeview_frame, columns=columns, show='headings')

        # 設定欄位名稱
        self.treeview.heading('sna', text='站名')
        self.treeview.heading('sarea', text='行政區')
        self.treeview.heading('mday', text='資料更新時間')
        self.treeview.heading('ar', text='地址')
        self.treeview.heading('act', text='車輛狀態')
        self.treeview.heading('updateTime', text='及時更新時間')
        self.treeview.heading('total', text='車輛總數')
        self.treeview.heading('rent_bikes', text='可租借車輛數量')
        self.treeview.heading('lat', text='緯度')
        self.treeview.heading('lng', text='經度')
        self.treeview.heading('retuen_bikes', text='可歸還車柱數量')
        
       # 垂直和水平滾動條
        verticalsb = ttk.Scrollbar(treeview_frame, orient="vertical", command=self.treeview.yview)
        verticalsb.pack(side='right', fill='y')
        horizontalsb = ttk.Scrollbar(treeview_frame, orient="horizontal", command=self.treeview.xview)
        horizontalsb.pack(side='bottom', fill='x')

        # 配置 Treeview 滾動條
        self.treeview.configure(xscroll=horizontalsb.set, yscroll=verticalsb.set)
        self.treeview.pack(fill=tk.BOTH, expand=True)
        


        # 將資料寫入到 Treeview
    def show_data(self):
        try:
            ubike:list[dict] = data.load_data()
            
        except Exception as error:
            print(error)
        else:
            for data in ubike:
                sna_value = data['sna'].split("_")[1]
                if data['act'] == '1':
                    act_value = "營業中" 
                else:
                    act_value = "維護中"
                    self.treeview.insert('', 'end', values=(sna_value, data['sarea'], data['mday'], data['ar'], act_value, data['updateTime'], data['total'], data['rent_bikes'], data['lat'], data['lng'], data['retuen_bikes']))
        
        
def main():
    window = Window(theme='arc')
    window.mainloop()
    
if __name__=='__main__':
    main()