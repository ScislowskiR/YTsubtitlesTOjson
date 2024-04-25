import sys
from tkinter import Tk, Label, Button, simpledialog
import tkinter as tk
from download_subtitles import *

class VerticalScrolledFrame:
    def __init__(self, master=None, width=100):
        self.outer = tk.Frame(master, background='pink')

        self.canvas = tk.Canvas(self.outer, highlightthickness=0, bg='lightyellow')
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        # self.canvas.grid(column=0, row=0)


        self.vsb = tk.Scrollbar(self.outer, orient=tk.VERTICAL)
        self.vsb.pack(fill=tk.Y, side=tk.RIGHT)
        # self.vsb.grid(column=1, row=0, sticky='ns')

        self.canvas['yscrollcommand'] = self.vsb.set
        self.canvas.bind("<Enter>", self._mouse_binding)
        self.canvas.bind("<Leave>", self._mouse_unbinding)
        self.vsb['command'] = self.canvas.yview


        self.frame1 = tk.Frame(self.canvas, bg='white')
        self.canvas.create_window(10, 10, window=self.frame1, anchor='nw')
        self.frame1.bind("<Configure>", self._on_frame_configure)
        # self.frame1.grid(column=0, row=0)
        # self.frame1.grid_rowconfigure(0, weight=1)

        self.frame2 = tk.Frame(self.canvas, bg='lightblue')
        self.canvas.create_window(60, 10, window=self.frame2, anchor='nw', width=width)
        self.frame2.bind("<Configure>", self._on_frame_configure)
        # self.frame2.grid(column=1, row=0)
        # self.frame2.grid_rowconfigure(0, weight=1)

        self.frame3 = tk.Frame(self.canvas, bg='pink')
        self.canvas.create_window(100+width, 10, window=self.frame3, anchor='nw', width=width)
        self.frame3.bind("<Configure>", self._on_frame_configure)
        # self.frame3.grid(column=2, row=0)
        # self.frame3.grid_rowconfigure(0, weight=1)

        self.outer_attr = set(dir(tk.Widget))


    def slave_time_labels(self, json_file):
        with open(json_file, 'r', encoding='utf-8') as j:
            data = json.loads(j.read())
        # data = json.loads(json_file)
        slave_time_labels_list = []
        row = 0
        for line in data:
            # print(line)
            start=float(line['start'])/60
            start = '{0:02.0f}:{1:02.0f}'.format(*divmod(start * 60, 60))
            # print(start)
            slave_time_labels_list.append(tk.Label(master=self.frame1, text=str(start)))
            # print(slave_time_labels_list[row])
            slave_time_labels_list[row].grid(column=0, row=row)
            row+=1


    def slave_buttonlines(self, json_file):
        with open(json_file, 'r', encoding='utf-8') as j:
            data = json.loads(j.read())
        self.frames4buttons2 = []
        self.buttons2 = []
        self.frames4buttons3 = []
        self.buttons3 = []
        row = 0
        for line in data:
            self.frames4buttons2.append(tk.Frame(master=self.frame2))
            self.frames4buttons2[row].grid(column=0, row=row)
            self.frames4buttons3.append(tk.Frame(master=self.frame3))
            self.frames4buttons3[row].grid(column=0, row=row)
            # print(self.frames4buttons2[row])
            line_text = line['text']
            buttons_in_line2 = []
            buttons_in_line3 = []
            start=float(line['start'])/60
            start = '{0:02.0f}:{1:02.0f}'.format(*divmod(start * 60, 60))
            print(start)
            for i, (k, v) in enumerate(line_text.items()):
                # print(i, k, v)
                # print(v[2])
                buttons_in_line2.append(ChangeValue(master=self.frames4buttons2[v[1]], text=k))
                buttons_in_line2[v[2]].grid(row=0, column=v[2])


                if v[0]==1:
                    pass
            self.buttons2.append(buttons_in_line2)
            row+=1


    def __getattr__(self, item):
        return getattr(self.outer, item) if item in self.outer_attr else getattr(self.frame1, item)

    def _on_frame_configure(self, event=None):
        x1, y1, x2, y2 = self.canvas.bbox("all")
        height = self.canvas.winfo_height()
        self.canvas.config(scrollregion=(0, 0, x2, max(y2, height)))

    def _on_mousewheel(self, event):
        if event.num == 4 or event.delta > 0:
            self.canvas.yview_scroll(-1, "units")
        elif event.num == 5 or event.delta < 0:
            self.canvas.yview_scroll(1, "units")

    def _mouse_binding(self, event=None):
        self.canvas.bind_all("<4>", self._on_mousewheel)
        self.canvas.bind_all("<5>", self._on_mousewheel)
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _mouse_unbinding(self, event=None):
        self.canvas.unbind_all("<4>")
        self.canvas.unbind_all("<5>")
        self.canvas.unbind_all("<MouseWheel>")

    def __str__(self):
        return str(self.outer)


class KamikazeButton(tk.Button):
    def __init__(self, master, text):
        super().__init__(master, text=text, bg="green", command=self.functions)

    def functions(self, function):
        pass


class ChangeValue(tk.Button):
    def __init__(self, master, text):
        super().__init__(master, text=text, bg="green", command=self.clicked)

    def clicked(self):
        if self['bg'] == "green":
            self.configure(bg="red")
            return -1
        else:
            self.configure(bg="green")
            return 1

    def __int__(self):
        if self['bg'] == "green":
            return -1
        if self['text'] == "red":
            return 1


class ButtonsFunctions():

    def new_folder(self):
        newfolder = simpledialog.askstring(title="Create folder", prompt="Folder name:")
        path = r'D:\pythonProject\YTsubtitlesTOlearningWORDS\YTsubtitlesTOjson\folders'
        newpath = path\
                  +'\\'\
                  +newfolder
        # print(newpath)
        if not os.path.exists(newpath):
            os.makedirs(newpath)

    def new_json(self, folder):
        video_link = simpledialog.askstring(title="Create text", prompt="Youtube video number:")
        name = simpledialog.askstring(title="File name", prompt="Name")
        language = simpledialog.askstring(title="Subtitles language", prompt="Language")
        language = [language]
        siema = DownloadSubtitles(category=folder, video_link=video_link, languages=language, name=name)
        siema.subtitles_to_json()


class MainWindow:
    def __init__(self, master=None):
        self.master = master
        self.master.grid()
        self.settings_frame()
        self.scrolled_frame()

    def new_folder_exec(self):
        ButtonsFunctions().new_folder()

        self.category_button()

    def new_json_exec(self, folder):
        ButtonsFunctions().new_json(folder)

        self.category_button()

    def settings_frame(self):
        self.settings = tk.Frame(self.master, width = 1500, height=100, borderwidth=2,
                                 relief=tk.SUNKEN, background="grey")
        self.settings.grid(column=0, row=0, sticky='EW')
        self.category_button()

    def category_button(self):
        self.category_settings = tk.Menubutton(self.settings, text='Text settings')
        self.category_settings.grid(column=0, row=0)
        self.edit_category_settings = tk.Menu(self.category_settings, tearoff=False)
        self.path_folders = r'D:\pythonProject\YTsubtitlesTOlearningWORDS\YTsubtitlesTOjson\folders'
        self.folders = os.listdir(self.path_folders)
        for folder in self.folders:
            #self.edit_category_settings.add_cascade(label=folder, command=lambda folder=folder: print(folder))
            self.edit_subcategory_settings = tk.Menu(self.edit_category_settings, tearoff=False)
            self.edit_category_settings.add_cascade(label=folder, menu=self.edit_subcategory_settings)
            self.path_texts = self.path_folders+'\\'+folder
            self.texts = os.listdir(self.path_texts)
            for text in self.texts:
                text_no_ext=os.path.splitext(text)[0]
                self.edit_subcategory_settings.add_command(label=text_no_ext,
                    command=lambda text=text:self.scrolled_frame(json_file=self.path_texts+'\\'+text))
            self.edit_subcategory_settings.add_command(label='New Text', background='green',
                                                       command=lambda:self.new_json_exec(folder=folder))

            # self.folders_menus.append(tk.Menubutton(self.edit_category_settings, tearoff=False))

        self.edit_category_settings.add_command(label='New Folder', background='green',
                                                command=lambda: self.new_folder_exec())
        self.category_settings.config(menu=self.edit_category_settings)
        self.master.bind('f', lambda e: self.category_settings.event_generate('<<Invoke>>'))

    def scrolled_frame(self, json_file=None):
        longest_line = 100
        if json_file is not None:
            with open(json_file, 'r', encoding='utf-8') as j:
                data = json.loads(j.read())
            letters_in_line = [sum(len(key) for key in line['text'].keys()) for line in data]
            longest_line = max(letters_in_line)
            longest_line = longest_line*10

        self.scrollable = VerticalScrolledFrame(self.master, width=longest_line)
        self.scrollable.grid(column=0, row=1, sticky='nsew')
        if json_file is not None:
            self.scrollable.slave_time_labels(json_file=json_file)
            self.scrollable.slave_buttonlines(json_file=json_file)


class Main():
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
        """
        with open(json_file, 'r', encoding='utf-8') as j:
            data = json.loads(j.read())
        for line in data:
            total_length = sum(len(key) for key in line.keys())
            print(total_length)
        """


if __name__ == "__main__":
    Main()
