import tkinter
from gui.data_frame import Data_frame
from gui.log_canvas import Log_canvas
from datetime import datetime
import time
import threading


class Main_screen(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x600")
        self.title = "DDos detecter"
        self.frame_log = Log_canvas(self)
        self.frame_statistic = self.__create_statistic_frame()
        self.frame_statistic.pack(fill=tkinter.X, pady=20)
        self.frame_log.pack(side=tkinter.BOTTOM, fill=tkinter.X)

    def update(self, statistic_result, warning_results):
        self.frame_conn.insert_data([statistic_result[0]])
        self.frame_data.insert_data([statistic_result[1], statistic_result[2]])
        for warning, warning_type in warning_results:
            self.frame_log.add_log(warning, warning_type)

    def __create_statistic_frame(self):
        frame_statistic = tkinter.Frame()
        self.frame_data = Data_frame(
            frame_statistic, ["red", "yellow"], ["Udp data", "Tcp data"])
        self.frame_conn = Data_frame(
            frame_statistic, ["red"], ["number of packets"])
        self.frame_data.pack(side=tkinter.RIGHT, padx=30)
        self.frame_conn.pack(side=tkinter.LEFT, padx=30)
        return frame_statistic
