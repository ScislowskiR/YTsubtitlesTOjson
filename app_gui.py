import sys
from tkinter import Tk, Label, Button, simpledialog
import tkinter as tk
from download_subtitles import *

class VerticalScrolledFrame:
    def __init__(self, master=None, **kwargs):
        width = kwargs.pop('width', None)
        height = kwargs.pop('height', None)
        bg = kwargs.pop('bg', kwargs.pop('background', None))
        self.outer = tk.Frame(master, **kwargs)

        self.canvas = tk.Canvas(self.outer, highlightthickness=0, bg='yellow')
        # self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.canvas.grid(column=0, row=0, sticky='nsew')


        self.vsb = tk.Scrollbar(self.outer, orient=tk.VERTICAL)
        # self.vsb.pack(fill=tk.Y, side=tk.RIGHT)
        # self.vsb.grid(column=1, row=0, sticky='nsew')

        self.canvas['yscrollcommand'] = self.vsb.set
        self.canvas.bind("<Enter>", self._mouse_binding)
        self.canvas.bind("<Leave>", self._mouse_unbinding)
        self.vsb['command'] = self.canvas.yview


        self.frame1 = tk.Frame(self.canvas, bg='green')
        self.canvas.create_window(10, 10, window=self.frame1, anchor='nw')
        self.frame1.bind("<Configure>", self._on_frame_configure)
        # self.frame1.grid(column=0, row=0)
        # self.frame1.grid_rowconfigure(0, weight=1)

        self.outer_attr = set(dir(tk.Widget))

    def slave_time_labels(self, json_file):
        with open(json_file, 'r', encoding='utf-8') as j:
            data = json.loads(j.read())
        # data = json.loads(json_file)
        slave_time_labels_list = []
        number = 0
        for line in data:
            print(line)
            start=float(line['start'])/60
            start = '{0:02.0f}:{1:02.0f}'.format(*divmod(start * 60, 60))
            print(start)
            slave_time_labels_list.append(tk.Label(master=self.frame1, text=str(start)))
            print(slave_time_labels_list[number])
            slave_time_labels_list[number].grid(column=0, row=number)
            number+=1


    def slave_buttons(self, json_file):
        pass

    def __getattr__(self, item):
        return getattr(self.outer, item) if item in self.outer_attr else getattr(self.inner1, item)

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


class EntryWithPlaceholder(tk.Entry):
    def __init__(self, master, placeholder="PLACEHOLDER", color='grey', variabletext=None):
        super().__init__(master, textvariable=variabletext)
        self.variabletext = variabletext
        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']
        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)
        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def foc_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()


class ChangeValue(tk.Button):
    def __init__(self, master):
        super().__init__(master, text="fill", bg="green", command=self.clicked)

    def clicked(self):
        if self['text'] == "fill":
            self.configure(text="unfill", bg="red")
            return -1
        else:
            self.configure(text="fill", bg="green")
            return 1

    def __int__(self):
        if self['text'] == "unfill":
            return -1
        if self['text'] == "fill":
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
        self.scrollable = VerticalScrolledFrame(self.master, borderwidth=2,
                                               relief=tk.SUNKEN, background="#2ff584")
        self.scrollable.grid(column=0, row=1, sticky='NSEW')
        if json_file is not None:
            self.scrollable.slave_time_labels(json_file=json_file)


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


if __name__ == "__main__":
    Main()
