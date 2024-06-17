from ttkthemes import ThemedTk
import tkinter as tk
from tkinter import ttk,messagebox,Misc
import data
from data import FilterData,Info
from tools import CustomMessagebox

class Window(ThemedTk):
    def __init__(self,theme:str='arc',**kwargs):     #建立->參數-有default value ; 呼叫->引數:引數值呼叫、引數名稱呼叫(沒有限定的呼叫:**kwargs)
        super(). __init__(theme=theme,**kwargs)
        self.title('台北市Youbike2.0即時資料')
        try:
            self. __data = data.load_data()  #+self.變實體->不會被消滅
            
        except Exception as e :     #下載失敗產生警告對話框(showwarning)
            messagebox.showwarning(title='警告',message=str(e))

        self._display_interface()    #呼叫


    @property
    def data(self)->list[dict]:              #每呼叫一次就執行一次(即時更新)
        return self.__data


    #顯示介面建立實體method
    def _display_interface(self):    #定義
        mainFrame = ttk.Frame(borderwidth=1,relief='groove')
        ttk.Label(mainFrame,text='台北市Youbike2.0即時資料',font=('arial',25)).pack(pady=(20,10))
        #====================================
        tableFrame = ttk.Frame(mainFrame)
        
        # define columns
        columns = ('sna', 'sarea', 'mday', 'ar', 'total', 'rent_bikes', 'retuen_bikes')

        tree = ttk.Treeview(tableFrame, columns=columns, show='headings',selectmode='browse')

        # define headings
        tree.heading('sna', text='站點')
        tree.heading('sarea', text='行政區')
        tree.heading('mday', text='時間')
        tree.heading('ar', text='地址')
        tree.heading('total', text='總數')
        tree.heading('rent_bikes', text='可借')
        tree.heading('retuen_bikes', text='可還')

        #定義欄位寬度
        tree.column('sarea',width=70,anchor=tk.CENTER)
        tree.column('mday',width=150,anchor=tk.CENTER)
        tree.column('ar',minwidth=100)
        tree.column('total',width=50,anchor=tk.CENTER)
        tree.column('rent_bikes',width=50,anchor=tk.CENTER)
        tree.column('retuen_bikes',width=50,anchor=tk.CENTER)
        
        #bind使用者的事件
        tree.bind('<<TreeviewSelect>>', self.item_selected)




        # add data to the treeview
        for site in self.data:
            tree.insert('', tk.END, 
                        values=(site['sna'],site['sarea'],site['mday'],site['ar'],site['total'],site['rent_bikes'],site['retuen_bikes']) )          #增加欄位

        tree.grid(row=0, column=0, sticky='nsew')

        # add a scrollbar
        scrollbar = ttk.Scrollbar(tableFrame, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')
        tableFrame.pack(expand=True,fill=tk.BOTH,padx=20,pady=20)
        #=====================================
        pieChartFrame = PieChartFrame(mainFrame)
        pieChartFrame.pack(expand=True,fill='both')
        mainFrame.pack(expand=True,fill=tk.BOTH,padx=10,pady=10)
        
    def item_selected(self,event):
        tree = event.widget
        #print(isinstance(tree,ttk.Treeview))   #isinstance: is 實體
        for selected_item in tree.selection():
            item = tree.item(selected_item)
            record:list = item['values']
            print(record)
            

class PieChartFrame(ttk.Frame):
    def __init__(self,master:Misc,**kwargs):
        super().__init__(master=master,**kwargs)

        self.configure(borderwidth=2,relief='groove')
        #self.configure({'borderwidth':2,'relief':'groove'})  #寫法2
        #self.config({'borderwidth':2,'relief':'groove'})    #寫法3   
        #self['borderwidth'] = 2                             #寫法4
        #self['relief'] = 'groove'   
        canvas = tk.Canvas(self)
        canvas.create_line(15,30,200,30)                 #畫線(x1,y1,x2,y2)
        canvas.create_line(300,35,300,200,dash=(8,2))    #虛線(線長,線距)
        canvas.create_line(55,85,155,85,105,180,55,85)   #三角形
        canvas.pack(expand=True,fill='both')
        self.pack(expand=True,fill='both')




def main():
    window = Window(theme='breeze')   #引數名稱的呼叫
    window.mainloop()   

if __name__ == '__main__':
    main()