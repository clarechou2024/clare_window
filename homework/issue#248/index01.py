from tkinter import Tk, Canvas, Frame, BOTH

class Example(Frame):

    def __init__(self,master):
        super().__init__(master)
        self.initUI()
        self.master.title("Lines-01")
        self.pack(fill=BOTH, expand=1)


    def initUI(self):
        canvas = Canvas(self)
        canvas.create_line(15, 30, 200, 30)
        canvas.create_line(15, 50, 200, 50, width=10,fill='green', dash=(10,2))
        canvas.create_line(300, 35, 300, 200, dash=(4, 2))
        canvas.create_line(350, 35, 350, 200,fill='red', dash=(4, 2))
        canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85)
        canvas.create_line(100, 85, 200, 85, 150, 180, 100, 85,fill='blue')
        canvas.pack(fill=BOTH, expand=1)


def main():

    root = Tk()
    ex = Example(root)
    root.geometry("400x250")
    root.mainloop()


if __name__ == '__main__':
    main()