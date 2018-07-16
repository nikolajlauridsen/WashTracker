from tkinter import *


class PayWindow(Frame):
    def __init__(self, db, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.db = db
        self.create_widgets()

    def create_widgets(self):
        Label(self.master, text='Amount due').pack()
