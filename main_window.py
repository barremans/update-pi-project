# main_window.py
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import ImageTk, Image, ImageOps
from tkinter import font
import webbrowser
import requests
import win32api
import threading
from packaging import version
import os
from update_manager import UpdateManager
from about_dialog import DisplayAboutMe
from version_info import __version__
from version_info import __AppName__


class Main:
    def __init__(self, parent):
        def check_updates():
            try:
                # Online Version File URL
                online_version_url = 'https://raw.githubusercontent.com/barremans/cgk-tools/main/version.txt'
                # Get the online version as a string
                response = requests.get(online_version_url)
                online_version_str = response.text.strip()

                # Parse the version strings
                current_version = version.parse(__version__)
                online_version = version.parse(online_version_str)

                if current_version < online_version:
                    messagebox.showinfo('Software Update', 'Update Available!')
                    mb1 = messagebox.askyesno(
                        'Update!', f'{__AppName__} {__version__} needs to update to version {online_version_str}')
                    if mb1 is True:
                        # Replace the URL with the actual update file URL
                        update_file_url = 'https://github.com/barremans/cgk-tools/blob/main/updates/setup%20CGK%20TOOLS.msi?raw=true'
                        webbrowser.open_new_tab(update_file_url)
                        parent.destroy()
                else:
                    messagebox.showinfo('Software Update',
                                        'No Updates are Available.')
            except Exception as e:
                messagebox.showinfo(
                    'Software Update', 'Unable to Check for Update, Error: ' + str(e))

        def about_me():
            DisplayAboutMe(parent)
        """
        def run_binary():
            win32api.ShellExecute(
                0, 'open', 'binaries\\TestBinary.exe', None, None, 10)
        """
        """
        def run_cmd():
            win32api.ShellExecute(0, 'open', 'cmd.exe',
                                  '/k ipconfig', None, 10)
        """
        def update_using_manager():
            try:
                # Online Version File URL
                online_version_url = 'https://raw.githubusercontent.com/barremans/cgk-tools/main/version.txt'
                # Get the online version as a string
                response = requests.get(online_version_url)
                online_version_str = response.text.strip()
                # Parse the version strings
                current_version = version.parse(__version__)
                online_version = version.parse(online_version_str)

                # if float(data) > float(__version__):
                if current_version < online_version:
                    messagebox.showinfo('Software Update', 'Update Available!')
                    mb2 = messagebox.askyesno(
                        'Update!', f'{__AppName__} {__version__} needs to update to version {online_version_str}')
                    if mb2 is True:
                        UpdateManager(parent)
                    elif mb2 == 'No':
                        pass
                else:
                    messagebox.showinfo('Software Update',
                                        'No Updates are Available.')
            except Exception as e:
                print('The Error is here!')
                messagebox.showinfo(
                    'Software Update', 'Unable to Check for Update, Error:' + str(e))

        menu_bar = tk.Menu(parent)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label='Exit', command=parent.destroy)
        menu_bar.add_cascade(label='File', menu=file_menu)
        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label='Check for update', command=update_using_manager)
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
        parent, text='Check for Updates', command=check_updates)
        button1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        #button3 = ttk.Button(parent, text='Run CMD', command=run_cmd)
        #button3.place(x=20, y=100)

        button4 = ttk.Button(parent, text='Check + Install',
                             command=update_using_manager)
        button4.place(x=-200, relx=1.0, y=60)
