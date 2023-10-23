import tkinter as tk
from tkinter import messagebox
from packaging import version
import requests
from version_info import __version__
from version_info import __AppName__
from update_manager import UpdateManager

def update_using_manager(parent):
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
            mb2 = messagebox.askyesno(
                'Update!', f'{__AppName__} {__version__} needs to update to version {online_version_str}')
            if mb2:
                update_url = 'https://github.com/barremans/cgk-tools/blob/main/updates/setup%20CGK%20TOOLS.msi?raw=true'
                updater = UpdateManager(parent)
                updater.download_and_install_update(update_url)
        else:
            messagebox.showinfo('Software Update', 'No Updates are Available')
    except Exception as e:
        print('The Error is here!')
        messagebox.showinfo(
            'Software Update', 'Unable to Check for Update, Error: ' + str(e))
