import tkinter
from gui.data_frame import Data_frame
class Main_screen(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("700x300+60+60")
        self.frame_connection = Data_frame()
        self.frame_data = Data_frame()
        self.frame_connection.pack(side=tkinter.LEFT)
        self.frame_data.pack(side=tkinter.RIGHT)

if __name__ == "__main__":
    Main_screen().mainloop()
