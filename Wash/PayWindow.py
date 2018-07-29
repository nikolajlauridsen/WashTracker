from tkinter import *


class PayWindow(Frame):
    def __init__(self, history, db, master=None, root=None):
        Frame.__init__(self, master)
        self.master = master
        self.root = root
        self.history = history
        self.db = db

        self.small_pad = 10
        self.large_pad = 45

        self.overview_frame = Frame(self.master)
        self.create_widgets()

    def create_widgets(self):
        # TODO: Don't hardcode the price values or currencies (use a config file)
        Label(self.master, text='Payment overview').pack()
        Label(self.overview_frame, text='Units: ').grid(column=0, row=0, sticky=W)
        Label(self.overview_frame, text=len(self.history)).grid(column=1, row=0,
                                                                padx=self.small_pad, sticky=E)

        Label(self.overview_frame, text='Price pr. unit: ').grid(column=0, row=1, sticky=W)
        Label(self.overview_frame, text='10 kr').grid(column=1, row=1,
                                                      padx=self.small_pad, sticky=E)

        Label(self.overview_frame, text='Total: ').grid(column=0, row=2, sticky=W)
        Label(self.overview_frame, text=str(len(self.history)*10)+" kr").grid(column=1, row=2,
                                                                              padx=self.small_pad, sticky=E)
        self.overview_frame.pack(padx=self.large_pad)

        Button(self.master, text="Mark as paid", command=self.pay).pack(pady=self.small_pad//2)

    def pay(self):
        # Todo: prompt user to dissuade missclicks and allow for a receipt to be saved.
        self.db.mark_all_as_paid()
        self.root.populate_table()
