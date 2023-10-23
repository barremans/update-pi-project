# update_manager.py
import os
import subprocess
import requests
from version_info import __version__
from version_info import __AppName__

class UpdateManager:
    def __init__(self, parent):
        self.parent = parent

    def download_and_install_update(self, update_url):
        try:
            # Download the update file from the URL
            update_filename = "update_file.msi"
            with open(update_filename, 'wb') as update_file:
                response = requests.get(update_url)
                update_file.write(response.content)

            # Execute the update file using subprocess
            subprocess.Popen(["msiexec", "/i", update_filename, "/qn"])
            
            # Close the application (optional)
            self.parent.destroy()
        except Exception as e:
            print('Error during update:', str(e))
