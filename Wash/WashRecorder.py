from tkinter import *
import tkinter.font as font
from .db_handler import DbHandler
from .PayWindow import PayWindow
from . import COLORS
import datetime


class WashRecorder(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.db = DbHandler()
        self.del_font = font.Font(size=7)
        self.history = list

        self.table_area = Frame(self.master)
        self.canvas = Canvas(self.table_area, borderwidth=0,
                             background=COLORS['grey'],
                             width=610, height=400)
        self.table = Frame(self.canvas)
        self.pay_window = None

        self.master.protocol("WM_DELETE_WINDOW", self.onClose)
        self.create_widgets()
        self.populate_table()

    def create_widgets(self):
        title_label = Label(self.master, text='WashRecorder', font=16)
        title_label.pack()

        # Scrollbar for washing table
        scrollbar = Scrollbar(self.table_area, orient='vertical',
                              command=self.canvas.yview)

        # Configure, create & pack canvas
        self.canvas.configure(yscrollcommand=scrollbar.set)
        self.canvas.create_window((4, 4), window=self.table,
                                  anchor="n", tags='self.table')
        self.canvas.pack(side=LEFT)
        scrollbar.pack(side=RIGHT, fill=Y)

        self.table_area.pack()

        btn_frame = Frame(self.master)
        Button(btn_frame, text='Add wash', command=self.insert_on_click).grid(column=0, row=0)
        Button(btn_frame, text="Pay dues", command=self.open_pay).grid(padx=10, column=1, row=0)
        btn_frame.pack(pady=5)

        # Bind scrolling
        self.table.bind("<Configure>", self.onFrameConfigure)
        self.table.bind('<Enter>', self._bound_to_mousewheel)
        self.table.bind('<Leave>', self._unbound_to_mousewheel)

    @staticmethod
    def format_time(time):
        return datetime.datetime.fromtimestamp(int(time)).strftime('%d/%m/%y %H:%M')

    def insert_on_click(self):
        self.db.insert_wash()
        self.populate_table()

    def open_pay(self):
        if not self.pay_window or not self.pay_window.winfo_exists():
            self.pay_window = Toplevel(master=self)
            self.pay_window.wm_title("Payment")
            PayWindow(self.history, self.db, master=self.pay_window, root=self)
        else:
            self.pay_window.lift(self.master)

    def clear_download_frame(self):
        """Clears file_frame"""
        for widget in self.table.winfo_children():
            widget.destroy()

    def delete_entry(self, timestamp):
        """
        Delete an entry in the database (in case of a missclick)
        Utilizes the time stamp since it should be unique in this application
        :param timestamp: the timestamp of the entry to delete
        """
        self.db.remove_entry(timestamp)
        self.populate_table()

    def populate_table(self):
        # Clear everything and recreate title labels.
        self.clear_download_frame()

        Label(self.table, text="Date", width=60,
              borderwidth="1", relief="solid").grid(row=0, column=0, padx=(5, 0), pady=4)
        Label(self.table, text="Paid", width=14,
              borderwidth="1", relief="solid").grid(row=0, column=1, pady=4)
        Label(self.table, text="Delete", width=10,
              borderwidth="1", relief="solid").grid(row=0, column=2, pady=4)

        # Fetch washing history from database and add them to table
        # TODO: fetch paid entries if requested.
        self.history = self.db.get_history()
        for i, file in enumerate(self.history):
            Label(self.table, text=self.format_time(file[0]), width=60,
                  borderwidth="1", relief="solid").grid(row=i+1, column=0, padx=(5, 0))

            text = "Yes" if file[1] == 1 else "No"
            color = COLORS['green'] if file[1] == 1 else COLORS['red']
            Label(self.table, text=text, width=14, bg=color,
                  borderwidth="1", relief="solid").grid(row=i+1, column=1)

            Button(self.table, text="Delete", command=lambda: self.delete_entry(file[0]),
                   width=10, font=self.del_font).grid(row=i + 1, column=2)

    def onClose(self):
        self.db.save_changes()
        self.master.destroy()
        print('Changes saved.')

    def onFrameConfigure(self, event):
        """Reset the scroll region to encompass the inner file_frame"""
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def _bound_to_mousewheel(self, event):
        """Bind mousewheel to scroll function"""
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _unbound_to_mousewheel(self, event):
        """Unbind mousewheel"""
        self.canvas.unbind_all("<MouseWheel>")

    def _on_mousewheel(self, event):
        """Scrolling function"""
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
