import tkinter


class StartScreen(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("200x300+50+50")

        self.lable_intro = tkinter.Label(
            self, text="choose the interface", padx="20", pady="20")
        self.text_input = tkinter.Text(
            self, bg="white", fg="black", height="3")
        self.list_interface = self.create_drop_down(["a", "b", "c"])
        self.button_connect = tkinter.Button(
            self, text="connect", command=self.add_handle)

        self.lable_intro.pack()
        self.text_input.pack()
        self.list_interface.pack(pady="10")
        self.button_connect.pack()

    def add_handle(self):
        input_name = self.text_input.get(1.0, tkinter.END)
        print("hello "+input_name)

    def create_drop_down(self, choises: list):
        default_value = tkinter.StringVar(self)
        default_value.set(choises[0])
        return tkinter.OptionMenu(self, default_value, *choises)


if __name__ == "__main__":
    StartScreen().mainloop()
