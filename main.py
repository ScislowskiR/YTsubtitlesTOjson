from app_gui import *


class Main:
    def __init__(self):
        root = tk.Tk()
        root.title("WordAPP of YT Videos")
        root.configure(background="pink")
        root.geometry('1350x800+150+0')
        scrollable = MainWindow
        scrollable(root)
        root.grid_columnconfigure(0, weight=1)
        root.grid_rowconfigure(1, weight=1)
        root.mainloop()


if __name__ == "__main__":
    Main()
