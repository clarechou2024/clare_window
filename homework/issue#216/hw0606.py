import tkinter as tk
from tkinter import ttk,Tk,Frame,Text,Misc,messagebox
from tkinter.simpledialog import Dialog
from ttkthemes import ThemedTk         #ThemedTk==>外部套件(美化主題)

class BMICalculator:
    def __init__(self,name,height_cm,weigh_kg):
        self.username = name
        self.height = height_cm
        self.weight = weigh_kg
    
   
    def calculate_bmi(self):
        try:
            height_m =self.height_cm / 100
            bmi = self.weight_kg / (height_m**2)
            return bmi
        except Exception as error:
            print(error)

class App(ThemedTk):
    def __init__(self,root):
        self.root = root
        self.root.title('BMI計算器')
        
        # configure the grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        
        self.create_widgets()
       

    def create_widgets(self):
        # username
        self.username_label = ttk.Label(self, text="姓名:")
        self.username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

        self.username_entry = ttk.Entry(self.root)
        self.username_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)
        

        # height
        self.height_label = ttk.Label(self, text="身高(cm):")
        self.height_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
        #self.height_label.pack()

        self.height_entry = ttk.Entry(self,show="*")
        self.height_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)
        #self.height_entry.pack()
        
        # weight
        self.weight_label = ttk.Label(self, text="體重(kg):")
        self.weight_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)

        self.weight_entry = ttk.Entry(self, show="*")
        self.weight_entry.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)

        # calculate button
        self.calculate_button = ttk.Button(self, text="計算",command=self.calculate_bmi)
        self.calculate_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

        #BMI
        self.result_label = ttk.Label(self,text="BMI:")
        self.result_label.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

    def calculate_bmi(self):
        try:
            name = self.name_entry.get()
            height_cm = float(self.height_entry.get())
            weight_kg = float(self.weight_entry.get())

            bmi_calculator = BMICalculator(name, height_cm, weight_kg)
            bmi = bmi_calculator.calculate_bmi()

            if bmi:
                self.result_label.config(text=f"BMI: {bmi}")
                self.show_bmi_category(bmi)
            else:
                self.result_label.config(text="BMI: 計算錯誤")
        except ValueError:
            messagebox.showerror("輸入錯誤", "請輸入有效的數字")

    def show_bmi_category(self, bmi):
        if bmi < 18.5:
            extra_weight = round(18.6 - bmi , 2)
            category = f" 都不吃飯是不是想修仙阿....? [過輕] 再增重{extra_weight}公斤就到正常體重了。"
            messagebox.showinfo(f"{self.name_entry.get()} 的BMI說明", f"{self.name_entry.get()}您好，{category}")
        elif 18.5 <= bmi < 24.9:
            category = " hell good'ya!!! [正常] "
            messagebox.showinfo(f"{self.name_entry.get()} 的BMI說明", f"{self.name_entry.get()}您好，{category}")
        elif 25 <= bmi < 29.9:
            extra_weight = round(bmi - 24.9, 2)
            category = f" 該...減..月巴...了。 [過胖] 再減{extra_weight}公斤就回到正常體重了。 "
            messagebox.showinfo(f"{self.name_entry.get()} 的BMI說明", f"{self.name_entry.get()}您好，{category}")
        else:
            category = " 您是不是想在地球上，引發人類歷史真正意義上的第一次完美核融合?????? [肥胖] "
            messagebox.showinfo(f"{self.name_entry.get()} 的BMI說明", f"{self.name_entry.get()}您好，{category}")




if __name__ == "__main__":
    app = App()
    app.mainloop()

    dialog = App(ThemedTk, title="自定義對話框")
    if dialog.result is not None:
        print("用戶的名字:", dialog.result)
    else:
        print("對話框已取消")
