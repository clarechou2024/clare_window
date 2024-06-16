from tkinter import Tk, Canvas, Frame, BOTH

class Example(Frame):

    def __init__(self,master):
        super().__init__()
        master.title("Shapes-03")
        self.pack(fill=BOTH, expand=1)
        self.initUI()


    def initUI(self):

        canvas = Canvas(self,width=400,height=400)
        canvas.create_oval(10, 10, 80, 80, outline="#f11",
            fill="#1f1", width=2)
        canvas.create_oval(5, 5, 30, 30, outline="blue",
            fill="green", width=3,dash=(5,5))
        canvas.create_oval(60, 60, 50, 50, outline="blue",
            fill="green", width=3,dash=(5,5))
        
        canvas.create_oval(110, 10, 210, 80, outline="#f11",
            fill="#1f1", width=2)
        canvas.create_oval(115, 15, 200, 75, outline="blue",
            fill="yellow", width=2, dash=(5,5))
        
        canvas.create_rectangle(230, 10, 290, 60,
            outline="#f11", fill="#1f1", width=2)
        canvas.create_rectangle(230, 65, 290, 115,
            outline="pink", fill="yellow", width=2,dash=(5,5))

        canvas.create_rectangle(30, 200, 90, 100,
                                outline="#f11", fill="#1f1", width=2)
        canvas.create_rectangle(5, 200, 25, 100,
                                outline="green", fill="yellow", width=2)

        canvas.create_arc(30, 200, 90, 100, start=0,
            extent=180, outline="#f11", fill="#1f1", width=2)



        points = [150, 100, 200, 120, 240, 180, 210,
            200, 150, 150, 100, 200]
        canvas.create_polygon(points, outline='#f11',
            fill='#1f1', width=2)
        points = [160, 90, 210, 110, 250, 190, 220,
            190, 160, 140, 110, 190]
        canvas.create_polygon(points, outline='blue',
            fill='red', width=2,dash=(5,5))

        canvas.pack(fill=BOTH, expand=1)


def main():

    root = Tk()
    ex = Example(root)
    root.geometry("330x220+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()