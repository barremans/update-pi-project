# about_dialog.py
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image, ImageOps
import webbrowser
from tkinter import font
from version_info import __version__
from version_info import __AppName__
from version_info import  __copyright__
from version_info import __license__


class DisplayAboutMe(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)

        self.transient(parent)
        self.result = None
        self.grab_set()
        w = 285
        h = 273
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.geometry('{0}x{1}+{2}+{3}'.format(w, h, int(x), int(y)))
        self.resizable(width=False, height=False)
        self.title('About')
        self.wm_iconbitmap('images/Graphicloads-Android-Settings-Contact.ico')

        self.image = Image.open('images/vs.png')
        self.size = (100, 100)
        self.thumb = ImageOps.fit(self.image, self.size, Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(self.thumb)
        logo_label = tk.Label(self, image=self.photo)
        logo_label.pack(side=tk.TOP, pady=10)

        f1 = tk.Frame(self)
        f1.pack()
        f2 = tk.Frame(self)
        f2.pack(pady=10)
        f3 = tk.Frame(f2)
        f3.pack()

        def call_link(*args):
            webbrowser.open_new_tab('https://github.com/barremans')

        tk.Label(f1, text=__AppName__ + ' ' + str(__version__)).pack()
        tk.Label(f1, text=__copyright__).pack()
        tk.Label(f1, text= __license__).pack()

        f = font.Font(size=10, slant='italic', underline=True)
        label1 = tk.Label(f3, text='TheRealBarremans', font=f, cursor='hand2')
        label1['foreground'] = 'blue'
        label1.pack(side=tk.LEFT)
        label1.bind('<Button-1>', call_link)
        ttk.Button(self, text='OK', command=self.destroy).pack(pady=5)
