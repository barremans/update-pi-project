# update_check.py
import requests
from packaging import version
from tkinter import messagebox
import webbrowser
from version_info import __version__
from version_info import __AppName__

def check_updates(parent):
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
                #parent.destroy() //dont close the app
        else:
            messagebox.showinfo('Software Update', 'No Updates are Available.')
    except Exception as e:
        messagebox.showinfo(
            'Software Update', 'Unable to Check for Update, Error: ' + str(e))

