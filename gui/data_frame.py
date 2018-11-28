import tkinter


class Data_frame(tkinter.Frame):
    def __init__(self):
        self.size_x = 300
        self.size_y = 250
        self.padding_left = 10
        self.padding_bottom = 20
        self.com_size = 2
        self.time_com_distance = 30
        self.data_com_distance = 25
        self.table_name = "abcd xyzr"

        super().__init__(heigh=self.size_x, width=self.size_y)

        self.canvas = tkinter.Canvas(self)
        self._create_data_table()

        self.canvas.pack(fill=tkinter.BOTH, padx="10", pady="10")

    def _create_data_table(self):
        data_table_y = self.size_y-self.padding_bottom
        data_table_x = self.size_x-self.padding_left
        self.canvas.create_rectangle(
            self.padding_left, 0, data_table_x, data_table_y, fill="grey")
        for i in range(1, 10):
            com_x = i * self.time_com_distance + self.padding_left
            self.canvas.create_line(
                com_x, data_table_y + self.com_size, com_x, data_table_y - self.com_size)
            self.canvas.create_text(
                com_x, data_table_y+self.com_size, anchor="n", text=i)
        for i in range(1, 8):
            com_y = data_table_y-i * self.data_com_distance
            self.canvas.create_line(
                self.padding_left + self.com_size, com_y, self.padding_left - self.com_size, com_y)
            self.canvas.create_text(
                self.padding_left-self.com_size, com_y, anchor="e", text=i)
        self.canvas.create_text(
            self.padding_left, data_table_y+30, text=self.table_name, anchor="w")
