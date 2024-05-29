import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title('pack1')
        self.geometry('300x200')                #設定視窗大小

        ttk.Button(self,text='Top').pack()      #版面管理<由上到下/左至右>:pack()
       
        ttk.Button(self,text='Middle').pack()
       
        ttk.Button(self,text='Bottom').pack()
     
if __name__=='__main__':
    window:Window = Window()
    window.mainloop()