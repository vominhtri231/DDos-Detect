import tkinter


class Data_screen(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("200x300+60+60")
        self.frame_data = tkinter.Frame(self)
        self.frame_data.title = "data"
        self.canvas = tkinter.Canvas(self.frame_data)

        self.canvas.create_line(0, 250, 0, 0, width="5", fill="black")
        self.canvas.create_line(0, 250, 200, 250, width="2", fill="black")

        self.canvas.create_line(0, 250, 100, 100, width="5", fill="red")

        self.canvas.create_text(30, 260, anchor="w", text="10")
        self.canvas.create_line(35, 255, 35, 245)

        self.canvas.pack(fill=tkinter.BOTH)
        self.frame_data.pack(fill=tkinter.BOTH, padx="10", pady="10")


if __name__ == "__main__":
    Data_screen().mainloop()
