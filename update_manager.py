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
            update_filename = "update_file.msi"
            self.download_update(update_url, update_filename)
            self.install_update(update_filename)
        except Exception as e:
            print(f'Error during update: {e}')

    def download_update(self, update_url, update_filename):
        try:
            response = requests.get(update_url)
            response.raise_for_status()  # Raise an exception for bad responses
            with open(update_filename, 'wb') as update_file:
                update_file.write(response.content)
        except requests.exceptions.RequestException as e:
            print(f'Failed to download the update: {e}')
        except Exception as e:
            print(f'Error during download: {e}')

    def install_update(self, update_filename):
        try:
            subprocess.Popen(["msiexec", "/i", update_filename, "/qn"])
            # Close the application (optional)
            self.parent.destroy()
        except subprocess.CalledProcessError as e:
            print(f'Error during installation: {e}')
        except Exception as e:
            print(f'Error during installation: {e}')

