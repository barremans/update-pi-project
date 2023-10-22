# update_manager.py
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image, ImageOps
import win32api
import threading
import os
import requests
from version_info import __AppName__

class UpdateManager(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)

        self.transient(parent)
        self.result = None
        self.grab_set()
        w = 350
        h = 200
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.geometry('{0}x{1}+{2}+{3}'.format(w, h, int(x), int(y)))
        self.resizable(width=False, height=False)
        self.title('Update Manager')
        self.wm_iconbitmap('images/Graphicloads-Android-Settings-Contact.ico')

        image = Image.open('images/updatemanager.jpg')
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.pack()

        def install_update():
            """
            win32api.ShellExecute(
                0, 'open', f'tmp\\{_AppName_}.msi', None, None, 10)
            parent.destroy()
            """
            win32api.ShellExecute(0, 'open', self.install_path, None, None, 10)
            self.parent.destroy()
# updates/setup CGK TOOLS.msi

        def start_update_manager():
            """
            with requests.get('https://github.com/barremans/cgk-tools/blob/main/updates/setup%20CGK%20TOOLS.msi?raw=true', stream=True) as r:
                self.progressbar['maximum'] = int(
                    r.headers.get('Content-Length'))
                r.raise_for_status()
                with open(f'./tmp/{_AppName_}.msi', 'wb') as f:
                    for chunk in r.iter_content(chunk_size=4096):
                        if chunk:  # filter out keep-alive new chunks
                            f.write(chunk)
                            self.progressbar['value'] += 4096
            self.button1.config(text='Install', state=tk.NORMAL)
            """
            try:
                download_folder = os.path.expanduser(
                    "~\\Downloads")  # Get the user's download folder
                file_path = os.path.join(download_folder, f'{__AppName__}.msi')
                with requests.get('https://github.com/barremans/cgk-tools/blob/main/updates/setup%20CGK%20TOOLS.msi?raw=true', stream=True) as r:
                    self.progressbar['maximum'] = int(
                        r.headers.get('Content-Length'))
                    r.raise_for_status()
                    with open(file_path, 'wb') as f:
                        for chunk in r.iter_content(chunk_size=4096):
                            if chunk:
                                f.write(chunk)
                                self.progressbar['value'] += 4096
                self.button1.config(text='Install', state=tk.NORMAL)
                self.install_path = file_path  # Store the path for later use
            except Exception as e:
                # Handle exceptions here
                print('Error:', str(e))
        self.progressbar = ttk.Progressbar(self,
                                           orient='horizontal',
                                           length=200,
                                           mode='determinate',
                                           value=0,
                                           maximum=0)
        self.progressbar.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.button1 = ttk.Button(
            self, text='Wait!', state=tk.DISABLED, command=install_update)
        self.button1.place(x=-83, relx=1.0, y=-33, rely=1.0)

        self.t1 = threading.Thread(target=start_update_manager)
        self.t1.start()