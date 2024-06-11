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


def main():
    window = Window(theme='arc')
    window.mainloop()
    
if __name__=='__main__':
    main()