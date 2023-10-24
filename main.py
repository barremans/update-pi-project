# main.py
import os
import tkinter as tk
from main_window import Main
from version_info import __version__
from version_info import __AppName__

def set_window_icon(root):
    icon_path = os.path.join(os.path.dirname(__file__), 'images', 'Graphicloads-Android-Settings-Contact.ico')
    if os.path.exists(icon_path):
        root.wm_iconbitmap(icon_path)

def main():
    root = tk.Tk()
    root.title(f"{__AppName__} {__version__}")
    root.geometry("650x400")
    root.resizable(width=False, height=False)

    set_window_icon(root)  # Set the window icon

    Main(root)
    root.mainloop()

if __name__ == '__main__':
    main()
