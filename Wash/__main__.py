from .WashRecorder import WashRecorder
from tkinter import Tk


def main():
    root = Tk()
    root.title('WashRecorder')
    app = WashRecorder(master=root)
    app.mainloop()


if __name__ == '__main__':
    main()
