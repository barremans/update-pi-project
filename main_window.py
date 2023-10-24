# main_window.py
"""
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import ImageTk, Image, ImageOps
from tkinter import font
from packaging import version
import os
from update_using_manager import update_using_manager
from update_check import check_updates
from about_dialog import DisplayAboutMe
from version_info import __version__
from version_info import __AppName__


class Main:
    def __init__(self, parent):
        def about_me():
            DisplayAboutMe(parent)
            
        menu_bar = tk.Menu(parent)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label='Exit', command=parent.destroy)
        menu_bar.add_cascade(label='File', menu=file_menu)
        
        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label='Check for update', command=lambda: update_using_manager(parent))
        help_menu.add_command(label='About', command=about_me)
        menu_bar.add_cascade(label='Help', menu=help_menu)
        
        parent.config(menu=menu_bar)

        buttons_frame = tk.Frame(parent, bg='#FFFFFF')
        buttons_frame.pack(side='top', fill='x')

        self._exit = ImageTk.PhotoImage(Image.open('images/exit.png'))

        exit_button = ttk.Button(
        buttons_frame, image=self._exit, command=parent.destroy)
        exit_button.pack(side=tk.LEFT, padx=1, pady=1)
        exit_button.image = self._exit

        button1 = ttk.Button(
        parent, text='Check for Updates', command=lambda: check_updates(parent))
        button1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        button4 = ttk.Button(parent, text='Check + Install',
                             command=lambda: update_using_manager(parent))
        button4.place(x=-200, relx=1.0, y=60)
"""
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
from about_dialog import DisplayAboutMe
from update_using_manager import update_using_manager
from update_check import check_updates
from version_info import __version__, __AppName__

class Main:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title(__AppName__)

        # Create the menu bar
        self.create_menu_bar()

        # Create the exit button
        self.create_exit_button()

        # Create "Check for Updates" and "Check + Install" buttons
        self.create_buttons()

    def create_menu_bar(self):
        menu_bar = tk.Menu(self.parent)

        # File menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label='Exit', command=self.parent.destroy)
        menu_bar.add_cascade(label='File', menu=file_menu)

        # Help menu
        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label='Check for update', command=lambda: update_using_manager(self.parent))
        help_menu.add_command(label='About', command=self.about_me)
        menu_bar.add_cascade(label='Help', menu=help_menu)

        self.parent.config(menu=menu_bar)

    def about_me(self):
        DisplayAboutMe(self.parent)

    def create_exit_button(self):
        exit_image = ImageTk.PhotoImage(Image.open('images/exit.png'))
        exit_button = ttk.Button(self.parent, image=exit_image, command=self.parent.destroy)
        exit_button.image = exit_image
        exit_button.pack(side=tk.LEFT, padx=1, pady=1)

    def create_buttons(self):
        button1 = ttk.Button(self.parent, text='Check for Updates', command=lambda: check_updates(self.parent))
        button1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        button2 = ttk.Button(self.parent, text='Check + Install', command=lambda: update_using_manager(self.parent))
        button2.place(x=-200, relx=1.0, y=60)

if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    root.mainloop()
