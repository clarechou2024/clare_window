#只有主執行檔,tools是function,裡面放class

from pprint import pprint
import tkinter as tk
from tkinter import ttk 
from ttkthemes import ThemedTk     #ThemedTk==>外部套件(美化主題),需先安裝
from tkinter import messagebox
from tkinter.simpledialog import Dialog
import tools

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
       func_frame = title_frame = ttk.Frame(self,style='Top.TFrame',borderwidth=1,relief='groove')
       ttk.Button(func_frame,text="AQI品質最好的5個",command=self.click1).pack(side='left',expand=True)   #command=self.click :註冊,可以點選到內容(要先建立class:def click)
       ttk.Button(func_frame,text="AQI品質最差的5個",command=self.click2).pack(side='left',expand=True)
       ttk.Button(func_frame,text="pm2.5品質最好的5個",command=self.click3).pack(side='left',expand=True)
       ttk.Button(func_frame,text="pm2.5品質最差的5個",command=self.click4).pack(side='left',expand=True)
       func_frame.pack(ipadx=100,ipady=30,padx=10,pady=10)

    def click1(self):
        messagebox.showinfo("information","Infomative message")
        #print("click1")

    def click2(self):
        messagebox.showerror("Error","Error message")
        #print("click2")

    def click3(self):
        messagebox.showwarning("Warning","Warning message")
        #print("click3")

    def click4(self):
        ShowInfo(parent=self,title="這是Dialog")    #自訂title內容

        #answer:bool = messagebox.askyesno("還要嗎?")
        #print(answer)
        
class ShowInfo(Dialog):
    def __init__(self,**kwargs):    #用**kwargs的話,要用引述名稱的呼叫:ShowInfo(**parent**=self,title="這是Dialog")
        super().__init__(**kwargs)    #繼承父類別用:super()

    def body(self,master):
        text = tk.Text(self,height=8,font=('Helvetica',25),width=40)  
        text.pack(padx=10,pady=10)
        text.insert(tk.INSERT,"測試的文字")
        text.config(state='disabled')      #disabled:別人無法修改文字,內文要先放進去,再放disabled
        return None

def main():
    '''
    try:
        all_data:dict[any] = tools.download_json()
    except Exception as error:
        print(error)
    else:
       data:list[dict] = tools.get_data(all_data)
       pprint(data)
    '''
    window = Window(theme="radiance")   #theme(主題);"arc"->白色//"radiance"->主題的一種,List of ttk Themes可以找主題套用
    window.mainloop()

if __name__=='__main__':
    main()