# main_window.py
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import ImageTk, Image, ImageOps
from tkinter import font
from packaging import version
import os
#from update_manager import UpdateManager
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