#只有主執行檔,tools是function,裡面放class

from pprint import pprint
import tkinter as tk
from tkinter import ttk,Misc,Frame,Event
from ttkthemes import ThemedTk     #ThemedTk==>外部套件(美化主題),需先安裝
import tools
from tkinter import messagebox
from tkinter.simpledialog import Dialog
from datetime import datetime

#window介面設計
class Window(ThemedTk):
    def __init__(self,**kwargs):
       super().__init__(**kwargs)
       self.title("全台空氣品質指標(AQI)")
       #self.option_add("*Font","微軟整黑體 40")
       #定義style的名稱
       style = ttk.Style()
       #style.configure('Top.TFrame',background='#D7C4BB')  #背景色是使用日本色票
       style.configure('Top.TFrame')
       style.configure('Top.TLabel',font=('Helvetica',25,'bold'))

       title_frame = ttk.Frame(self,style='Top.TFrame',borderwidth=2,relief='groove')
       ttk.Label(title_frame,text='全台空氣品質指標(AQI)',style='Top.TLabel').pack(expand=True,fill='y')
       title_frame.pack(ipadx=100,ipady=30,padx=10,pady=10)  #ipad/pad:padding
       #ttk.Button(self,text="Quit",command=self.destroy).pack()

#按鈕區
       func_frame = ttk.Frame(self,style='Top.TFrame',borderwidth=1,relief='groove')
       ttk.Button(func_frame,text="AQI品質最好的5個",command=self.click1).pack(side='left',expand=True)   #command=self.click :註冊,可以點選到內容(要先建立class:def click)
       ttk.Button(func_frame,text="AQI品質最差的5個",command=self.click2).pack(side='left',expand=True)
       ttk.Button(func_frame,text="pm2.5品質最好的5個",command=self.click3).pack(side='left',expand=True)
       ttk.Button(func_frame,text="pm2.5品質最差的5個",command=self.click4).pack(side='left',expand=True)
       func_frame.pack(ipadx=100,ipady=30,padx=10,pady=10)

    def download_parse_data(self)->list[dict] | None:
        try:
            all_data:dict[any] = tools.download_json()
        except Exception as error:
            messagebox.showwarning("輸入錯誤","請輸入正確的身高(cm)和體重(kg)。")
            return
        else:
            data:list[dict] = tools.get_data(all_data)
            return data
             #pprint(data)
             #return  #最後一行本來就return了

    def update_data(self):
        if (tools.AQI.aqi_records is None) or(tools.AQI.update_time is None): 
            #先檢查:tool裡的AQI若有None就先下載
            tools.AQI.aqi_records = self.download_parse_data()
            tools.AQI.update_time = datetime.now()
        elif((datetime.now()-tools.AQI.update_time).seconds >= 60 * 60):   #classmethod:datetime.now()
            tools.AQI.aqi_records = self.download_parse_data()
            tools.AQI.update_time = datetime.now()
            

    def click1(self):
        self.update_data()
        data:list[dict] = tools.AQI.aqi_records
        sorted_data:list[dict] = sorted(data,key=lambda value:value['aqi'])
        best_aqi:list[dict] = sorted_data[:5]   #傳出前5個
        def abc(value:dict)->str:
            return f"{value['county']} - {value['site_name']} - aqi:{value['aqi']} - 狀態:{value['status']} - {value['date']}"
        message_data:list[str] = list(map(abc,best_aqi))
        message = "\n".join(message_data)
        print(message)
        ShowInfo(parent=self,title="全台AQI最佳前5個區域",message=message)
        
    def click2(self):
        self.update_data()
        data:list[dict] = tools.AQI.aqi_records
        sorted_data:list[dict] = sorted(data,key=lambda value:value['aqi'],reverse=True)   #reverse=True->反序
        best_aqi:list[dict] = sorted_data[:5] 
        def abc(value:dict)->str:
            return f"{value['county']} - {value['site_name']} - aqi:{value['aqi']} - 狀態:{value['status']} - {value['date']}"
        message_data:list[str] = list(map(abc,best_aqi))
        message = "\n".join(message_data)
        print(message)
        ShowInfo(parent=self,title="全台AQI最差5個區域",message=message)

    def click3(self):
        self.update_data()
        data:list[dict] = tools.AQI.aqi_records
        sorted_data:list[dict] = sorted(data,key=lambda value:value['pm25'])
        best_aqi:list[dict] = sorted_data[:5]   #傳出前5個
        def abc(value:dict)->str:
            return f"{value['county']} - {value['site_name']} - pm25:{value['pm25']} - 狀態:{value['status']} - {value['date']}"
        message_data:list[str] = list(map(abc,best_aqi))
        message = "\n".join(message_data)
        print(message)
        ShowInfo(parent=self,title="全台pm2.5最佳前5個區域",message=message)

    def click4(self):
        self.update_data()
        data:list[dict] = tools.AQI.aqi_records
        sorted_data:list[dict] = sorted(data,key=lambda value:value['pm25'],reverse=True)      #reverse=True->反序
        best_aqi:list[dict] = sorted_data[:5] 
        def abc(value:dict)->str:
            return f"{value['county']} - {value['site_name']} - pm25:{value['pm25']} - 狀態:{value['status']} - {value['date']}"
        message_data:list[str] = list(map(abc,best_aqi))
        message = "\n".join(message_data)
        print(message)
        ShowInfo(parent=self,title="全台pm2.5最差5個區域",message=message)

class ShowInfo(Dialog):
    def __init__(self,parent:Misc,title:str | None = None,message:str=""):
        self.message = message
        super().__init__(parent=parent,title=title)    #繼承父類別用:super()!!最後才執行!!
        

    def body(self,master:Frame)->Misc | None:        #建立對話框主體
        text = tk.Text(self,height=8,font=('Helvetica',15),width=60)  
        text.pack(padx=10,pady=10)
        text.insert(tk.INSERT,self.message)
        text.config(state='disabled')      #disabled:別人無法修改文字,內文要先放進去,再放disabled
        return None
    
    def apply(self) -> None:
        '''
        使用者按下內建的ok button,會執行的內容
        '''
        print("使用者按下ok了")

    def buttonbox(self) -> None:
        '''
        自訂button
        '''
        box = tk.Frame(self)
        self.ok_button = tk.Button(box, text="確定", width=10, command=self.ok, default=tk.ACTIVE)  #default可不寫，預設是normal->:hover
        self.ok_button.pack(pady=(20,30),ipady=10)
        box.pack()
    
    def ok(self) -> None:
        print("OK button was clicked!")
        super().ok()



def main():
    #window = Window(theme="radiance")   #theme(主題);"arc"->白色//"radiance"->主題的一種,List of ttk Themes可以找主題套用
    window = Window()   #theme(主題);"arc"->白色//"radiance"->主題的一種,List of ttk Themes可以找主題套用
    window.mainloop()

if __name__=='__main__':
    main()