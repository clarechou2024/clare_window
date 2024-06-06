import tkinter as tk
from tkinter import ttk

# root window
root = tk.Tk()
root.geometry("240x150")
root.title('BMI計算器')
root.resizable(0, 0)

# configure the grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)

# username
username_label = ttk.Label(root, text="姓名:")
username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

username_entry = ttk.Entry(root)
username_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

# height
height_label = ttk.Label(root, text="身高(cm):")
height_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

height_entry = ttk.Entry(root,  show="*")
height_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

# weight
weight_label = ttk.Label(root, text="體重(kg):")
weight_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)

weight_entry = ttk.Entry(root)
weight_entry.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)

# calculate button
calculate_button = ttk.Button(root, text="計算")
calculate_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)


root.mainloop()
