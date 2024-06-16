from tkinter import Tk, Canvas, Frame, BOTH


class Example(Frame):

    def __init__(self,master):
        super().__init__(master)
        self.master.title("Colours-02")
        self.pack(fill=BOTH, expand=1)
        self.initUI()


    def initUI(self):
        canvas = Canvas(self)
        canvas.create_rectangle(30, 10, 120, 80,
            outline="red", fill="red")
        canvas.create_rectangle(150, 10, 240, 80,
            outline="yellow", fill="yellow")
        canvas.create_rectangle(270, 10, 370, 80,
            outline="green", fill="green")
        canvas.create_rectangle(400, 10, 500, 80,
            outline="blue", fill="blue")
        canvas.pack(fill=BOTH, expand=1)
def main():

    root = Tk()
    ex = Example(root)
    root.geometry("550x100")
    root.mainloop()


if __name__ == '__main__':
    main()