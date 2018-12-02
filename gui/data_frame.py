import tkinter
from datetime import datetime


class Data_frame(tkinter.Frame):
    def __init__(self, parent, colors, data_names):
        self.colors = colors
        self.data_names = data_names

        self.data = []
        self.time = []
        self.radio = 0.3
        self.minimun_propo = 0.65
        self.display_value = 1000

        self.size_x = 450
        self.size_y = 350
        self.padding_left = 50
        self.padding_bottom = 60
        self.padding_right = 30
        self.com_size = 2
        self.frame_border = 1

        super().__init__(parent, height=self.size_y+self.frame_border,
                         width=self.size_x+self.frame_border, bg="black")
        self.canvas = tkinter.Canvas(
            self, height=self.size_y, width=self.size_x)
        self.canvas.pack(fill=tkinter.BOTH,
                         padx=self.frame_border, pady=self.frame_border)

    def insert_data(self, inserted_data):
        temp = 0
        trans_data = []
        for data_ele in inserted_data:
            temp += data_ele
            trans_data.append(temp)
        self.data.append(trans_data)
        self.time.append(str(datetime.now().time())[0:8])
        self.update_frame()

    def update_frame(self):
        if len(self.data) < 2:
            return
        self.__update_radio()
        self.canvas.delete("all")
        self.__create_data_table()
        self.__create_data_collumn()
        self.__create_ruler()
        self.__create_time_ax()

    def __create_data_table(self):
        data_table_y = self.size_y-self.padding_bottom
        self.canvas.create_rectangle(
            self.padding_left, 0, self.size_x-self.padding_right, data_table_y, fill="grey")
        vertival_lap = 20
        padding_notice = 40
        color_square_size = 10
        for i in range(len(self.colors)):
            vertival_pos = (i+1)*vertival_lap
            self.canvas.create_rectangle(
                self.padding_left + padding_notice, data_table_y + vertival_pos,
                self.padding_left+color_square_size +
                padding_notice, data_table_y+vertival_pos+color_square_size,
                fill=self.colors[i])
            self.canvas.create_text(
                self.padding_left+padding_notice+20, data_table_y+vertival_pos+color_square_size/2,
                text=self.data_names[i], anchor="w")

    def __create_data_collumn(self):
        column_lap = (self.size_x-self.padding_left -
                      self.padding_right) / (len(self.data)-1)
        base_lay = [(column_lap * i + self.padding_left)
                    for i in range(len(self.data))]
        point_lays = []
        point_lays.append(
            [self.size_y-self.padding_bottom for i in range(len(self.data))])
        for i in range(len(self.data[0])):
            lay = []
            for j in range(len(self.data)):
                lay.append(self.size_y-self.padding_bottom -
                           self.data[j][i]*self.radio)
            point_lays.append(lay)
        for i in range(len(self.data[0])):
            points_for_canvas = []
            for j in range(len(self.data)):
                points_for_canvas.append(base_lay[j])
                points_for_canvas.append(point_lays[i+1][j])
            for j in range(len(self.data))[::-1]:
                points_for_canvas.append(base_lay[j])
                points_for_canvas.append(point_lays[i][j])
            self.canvas.create_polygon(points_for_canvas, fill=self.colors[i])

    def __create_ruler(self):
        com_y = self.size_y-self.padding_bottom - self.display_value*self.radio
        self.canvas.create_line(
            self.padding_left + self.com_size, com_y, self.padding_left - self.com_size, com_y)
        self.canvas.create_text(
            self.padding_left-self.com_size, com_y, anchor="e", text=self.__get_display_ruler_value())

    def __create_time_ax(self):
        self.__create_time_comb(0)
        self.__create_time_comb(len(self.data)-1)
        if len(self.data) > 2:
            self.__create_time_comb(int(len(self.data)/2))

    def __create_time_comb(self, position):
        display_time = self.time[position]
        column_lap = (self.size_x-self.padding_left -
                      self.padding_right) / (len(self.data)-1)
        data_table_y = self.size_y-self.padding_bottom
        com_x = position*column_lap + self.padding_left
        self.canvas.create_line(
            com_x, data_table_y + self.com_size, com_x, data_table_y - self.com_size)
        self.canvas.create_text(
            com_x, data_table_y+self.com_size, anchor="n", text=display_time)

    def __get_display_ruler_value(self):
        if self.display_value < 1000:
            return str(self.display_value)
        else:
            return "{0:2.1f}k".format(self.display_value/1000)

    def __update_radio(self):
        max_collumn_value = self.__get_max_value()
        if not self.__check_radio(max_collumn_value):
            self.radio, self.display_value = self. __get_new_radio(
                max_collumn_value)

    def __get_max_value(self):
        result = 0
        for data_collumn in self.data:
            max_in_collumn = max(data_collumn)
            if max_in_collumn > result:
                result = max_in_collumn
        return result

    def __check_radio(self, max_collumn_value):
        max_height_propo = self.radio * max_collumn_value / self.size_y
        return self.minimun_propo < max_height_propo and max_height_propo < 1

    def __get_new_radio(self, max_collumn_value):
        step = 1
        radio = (self.size_y-self.padding_bottom)*0.8/max_collumn_value
        while max_collumn_value > 100:
            max_collumn_value /= 10
            step *= 10
        return radio, round(max_collumn_value)*step
