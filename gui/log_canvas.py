import tkinter
import tkinter.ttk
import ml.const
from datetime import datetime


class Log_canvas(tkinter.Canvas):
    def __init__(self, parent):
        super().__init__(parent, height=100)
        self.index = 0

        self.__create_table()
        self.vertical_scroll_bar = tkinter.ttk.Scrollbar(
            self, orient="vertical", command=self.tree.yview)
        self.configure(yscrollcommand=self.vertical_scroll_bar.set)

        self.vertical_scroll_bar.pack(side='right', fill='y')
        self.tree.pack(fill=tkinter.X)

    def add_log(self, log, is_attack):
        padd_tag = 0
        if is_attack:
            padd_tag = 2
        self.tree.insert('', 'end', tags=self.index + padd_tag,
                         text=str(datetime.now().time())[0:8], values=log)
        self.index += 1
        self.index %= 2

    def __create_table(self):
        self.tree = tkinter.ttk.Treeview(self, selectmode='browse', columns=(
            "Address", "Type", "Probability"))
        self.tree.column("Address", anchor="c")
        self.tree.column("Type", anchor="c")
        self.tree.column("Probability", anchor="c")
        self.tree.heading('#0', text='Time')
        self.tree.heading('#1', text='Address')
        self.tree.heading('#2', text='Type')
        self.tree.heading('#3', text='Probability')
        self.tree.column('#0', stretch=tkinter.YES)
        self.tree.column('#1', stretch=tkinter.YES)
        self.tree.column('#2', stretch=tkinter.YES)
        self.tree.column('#3', stretch=tkinter.YES)
        self.tree.tag_configure(1, background="#CCFFFF")
        self.tree.tag_configure(2, background="#d15a42")
        self.tree.tag_configure(3, background="#ed040c")
