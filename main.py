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
    root.title(__AppName__ + ' ' + str(__version__))
    w = 650
    h = 400
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sw - w) / 2
    y = (sh - h) / 2
    root.geometry('{0}x{1}+{2}+{3}'.format(w, h, int(x), int(y)))
    root.resizable(width=False, height=False)

    set_window_icon(root)  # Call the function to set the window icon dynamically

    Main(root)
    root.mainloop()

if __name__ == '__main__':
    main()
