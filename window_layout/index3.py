import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title('pack1')
        self.geometry('300x200')                #設定視窗大小

        ttk.Button(self,text='Top').pack(fill='x')     #填滿x軸
       
        ttk.Button(self,text='Middle').pack(fill='x')
       
        ttk.Button(self,text='Bottom').pack(fill='x')
     
if __name__=='__main__':
    window:Window = Window()
    window.mainloop()