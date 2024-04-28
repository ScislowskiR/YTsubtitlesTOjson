"""from tkinter import *
root = Tk()
root.geometry("500x500")
mainmenu = Menu(root)
root.config(menu = mainmenu)
test_menu = Menu(mainmenu , tearoff = False)
mainmenu.add_cascade(label = "Test Menu" , menu = test_menu)
#############################################
sub_menu = Menu(test_menu, tearoff=False)
test_menu.add_cascade(label = 'Sub menu', menu=sub_menu)

sub_menu.add_command(label='Submenu item 1')
sub_menu.add_command(label='Submenu item 2')
sub_sub_menu = Menu(sub_menu, tearoff=False)
sub_menu.add_cascade(label='Sub-sub menu', menu=sub_sub_menu)

sub_sub_menu.add_command(label='Sub-submenu item 1')
sub_sub_menu.add_command(label='Sub-submenu item 2')

mainloop()"""
"""from deep_translator import GoogleTranslator
translated = GoogleTranslator(source='auto', target='de').translate("praca")  # output -> Weiter so, du bist großartig
print(translated)"""

"""import tkinter as tk
class Example(tk.Frame):
    def __init__(self, parent):

        tk.Frame.__init__(self, parent)
        self.canvas = tk.Canvas(self, borderwidth=0, background="#ffffff")
        self.frame = tk.Frame(self.canvas, background="#ffffff")
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4,4), window=self.frame, anchor="nw",
                                  tags="self.frame")

        self.frame.bind("<Configure>", self.onFrameConfigure)

        self.populate()

    def populate(self):
        '''Put in some fake data'''
        for row in range(100):
            tk.Label(self.frame, text="%s" % row, width=3, borderwidth="1",
                     relief="solid").grid(row=row, column=0)
            t="this is the second column for row %s" %row
            tk.Label(self.frame, text=t).grid(row=row, column=1)

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

if __name__ == "__main__":
    root=tk.Tk()
    example = Example(root)
    example.pack(side="top", fill="both", expand=True)
    root.mainloop()"""

"""import tkinter as tk
from tkinter import ttk
import random
import string


class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Using grid with two frames")

        # Lay out two frames on the root window
        ## first frame will contain two rows of control widgets
        ## this frame will be able to resize horizontally
        frame_controls = tk.Frame(master=self.root, padx=10, pady=10)
        frame_controls.grid(row=0,
                            column=0, sticky="ew")

        ## second frame will contain a treeview
        ## this frame will be able to resize vertically and horizontally
        frame_treeview = tk.LabelFrame(master=self.root, padx=10, pady=10,
                                       text="Image files")
        frame_treeview.grid(row=2,
                            column=0, padx=5, pady=5,
                            sticky="nsew")

        # Create widgets in the appropriate frames
        ## first frame, first row: a button, an entry box, and another button
        self.button_dest = ttk.Button(master=frame_controls, text="Dest dir")
        self.entry = ttk.Entry(master=frame_controls)
        self.button_clear = ttk.Button(master=frame_controls, text="Clear")

        ## first frame, second row: two buttons
        self.button_scale = ttk.Button(master=frame_controls, text="Scale")
        self.button_upload = ttk.Button(master=frame_controls, text="Upload")

        ## second frame, third row: the treeview
        self.tree = ttk.Treeview(master=frame_treeview,
                                 columns=("original", "scaled", "status"),
                                 show="headings")
        self.tree.heading("original", text="Original")
        self.tree.heading("scaled", text="Scaled")
        self.tree.heading("status", text="Status")

        ## add a vertical scroll bar to the containing frame and configure to the treeview
        self.vsb = ttk.Scrollbar(master=frame_treeview,
                                 orient="vertical",
                                 command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.vsb.set)

        ## add rows of random string values to the treeview (dummy data)
        for _ in range(20):
            self.tree.insert("",
                             tk.END,
                             values=("".join(random.choices(string.ascii_letters, k=8)),
                                     "".join(random.choices(string.ascii_letters, k=8)),
                                     "".join(random.choices(string.ascii_letters, k=8))))

        # Lay out the widgets in the grid
        pad = 5  # uniform padding
        self.button_dest.grid(row=0,
                              column=0, padx=pad, pady=pad)

        self.entry.grid(row=0,
                        column=1, padx=pad, pady=pad, sticky=tk.EW,
                        columnspan=2)

        self.button_clear.grid(row=0,
                               column=3, padx=pad, pady=pad)

        self.button_scale.grid(row=1,
                               column=0, padx=pad, pady=pad)
        self.button_upload.grid(row=1,
                                column=1, padx=pad, pady=pad)

        self.tree.grid(row=2,
                       column=0, padx=pad, pady=pad, sticky=tk.NSEW)
        self.vsb.grid(row=2,
                      column=1, sticky=tk.NS)

        # Configure resizing behavior
        self.root.grid_rowconfigure(2, weight=1)  # the frame-containing window must resize
        self.root.grid_columnconfigure(0, weight=1)  # otherwise the contained frames will not

        frame_controls.grid_columnconfigure(2, weight=1)  # make contained entry resize with window

        frame_treeview.grid_rowconfigure(2, weight=1)  # make the contained treeview resize vertically,
        frame_treeview.grid_columnconfigure(0, weight=1)  # and horizontally


if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()"""
"""import tkinter as tk
root = tk.Tk()

# create button
# assign button text along
# with background color
myButton = tk.Button(root,
                  text="On Hover - Background Change",
                  bg="yellow")
myButton.pack()

# call function with background
# colors as argument
# function to change properties of button on hover
def changeOnHover(button, colorOnHover, colorOnLeave):

	# adjusting background of the widget
	# background on entering widget
	button.bind("<Enter>", func=lambda e: button.config(
		background=colorOnHover))

	# background color on leving widget
	button.bind("<Leave>", func=lambda e: button.config(
		background=colorOnLeave))

changeOnHover(myButton, "red", "yellow")

root.mainloop()
"""
"""from tkinter import *

class ToolTip(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 57
        y = y + cy + self.widget.winfo_rooty() + 27
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(tw, text=self.text, justify=LEFT,
                      background="#ffffe0", relief=SOLID, borderwidth=1,
                      font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

def CreateToolTip(widget, text):
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)

# Create a Tkinter window
root = Tk()

# Create a Button
button = Button(root, text="Hover Me")

# Pack the Button
button.pack()

# Create a tooltip for the Button
CreateToolTip(button, "This is a tooltip")

# Run the Tkinter event loop
root.mainloop()
"""
import re


def get_video_id(url):
    # Regular expression pattern to match YouTube video URLs
    pattern = r'(?:https?://)?(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/)([a-zA-Z0-9_-]{11})'

    # Search for the video ID in the URL using the pattern
    match = re.search(pattern, url)

    # If a match is found, return the video ID, otherwise return None
    if match:
        return match.group(1)
    else:
        return None


# Example usage:
url = "https://www.youtube.com/watch?v=wP7s-aiCjRw"
video_id = get_video_id(url)
print("Video ID:", video_id)
