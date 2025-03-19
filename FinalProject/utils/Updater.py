import requests
import os
import sys
import platform
import hashlib
import shutil
import subprocess
import logging
from utils.helper import helper


class Updater:

    def __init__(self, server_url, version,OutList=None):
        self.is_debug = bool(os.getenv("MT_DEBUG", False))
        if self.is_debug:
            logging.basicConfig(filename="Log/debug.log", level=logging.DEBUG)
        else:
            logging.basicConfig(filename="Log/error.log", level=logging.ERROR)
        
        if not OutList is None:
            self.helper = helper(output=OutList)
        else:
            self.helper = None
        self.server_url = server_url + "/check_update"
        self.version = version
        self.latest_version = ''
        self.os_type = self.detect_os()
        self.check_for_updates()

    def detect_os(self):
        system = platform.system().lower()
        if self.is_debug:
            logging.debug(f"Check OS and it's {system}")
        else:
            if not self.helper is None: self.helper.UpDateOutput(f'Check Update for System {system}')
        return {"windows": "windows", "linux": "linux", "darwin": "macos"}.get(system, "unknown")

    def check_for_updates(self):
        try:
            if self.is_debug:
                logging.debug(f"Check if there is New Update")
            response = requests.get(self.server_url, params={"os": self.os_type})
            if response.status_code == 200:
                if self.is_debug:
                    logging.debug(f"Server is 200")
                data = response.json()
                if not self.helper is None: self.helper.UpDateOutput(f"Check Upgrade version Sha256")
                latest_version = data["latest_version"]
                download_url = data["download_url"]
                # patch_url = data["patch_url"]
                expected_sha256 = data["sha256"]

                if self.is_new_version(latest_version):
                    self.latest_version = latest_version
                    logging.info(f"A new update is available {latest_version}, downloading...")
                    if not self.helper is None: self.helper.UpDateOutput(f"A new update is available {latest_version}, downloading...")
                    update_file = self.download_update(download_url)
                    if not self.helper is None: self.helper.UpDateOutput(f"Downloading...")
                    if self.verify_file(update_file, expected_sha256):
                        logging.debug(f"The update file is valid, applying the update...")
                        if not self.helper is None: self.helper.UpDateOutput(f"The update file is valid, applying the update...")
                        self.apply_update(update_file)
                    else:
                        logging.debug(f"Update verification failed! The file may be corrupted.")
                        if not self.helper is None: self.helper.UpDateOutput(f"Update verification failed! The file may be corrupted.")
                        os.remove(update_file)
                else:
                    logging.debug(f"The application is already up to date.")
                    if not self.helper is None: self.helper.UpDateOutput(f"The application is already up to date.")
            else:
                logging.debug(f"Failed to fetch update data from the server.")
                if not self.helper is None: self.helper.UpDateOutput(f"Failed to fetch update data from the server.")
        except Exception as e:
            logging.info(f"Error while checking for updates: {e}")
            if not self.helper is None: self.helper.UpDateOutput(f"Error while checking for updates")

    def is_new_version(self, latest_version):
        if self.is_debug:
            logging.debug(f"Last Version is {latest_version}")
        return latest_version > self.version

    def download_update(self, url):
        try:
            if self.is_debug:
                logging.debug(f"Download Update")
            response = requests.get(url, stream=True)
            update_file = os.path.join(os.getcwd(), f"marketingtool_{self.latest_version}")

            # Determine file extension based on OS
            if self.os_type == "windows":
                update_file += ".exe"
            elif self.os_type == "macos":
                update_file += ".dmg"
            else:
                update_file += ".AppImage"

            with open(update_file, "wb") as file:
                shutil.copyfileobj(response.raw, file)
            
            if self.is_debug:
                logging.debug(f"Copyed")

            logging.info(f"Update downloaded successfully: {update_file}")
            return update_file
        except Exception as e:
            logging.info(f"Error while downloading the update: {e}")
            return None

    def verify_file(self, file_path, expected_hash):
        """ Verify file integrity using SHA-256 """
        sha256_hash = hashlib.sha256()
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        file_hash = sha256_hash.hexdigest()
        if file_hash == expected_hash:
            logging.debug(f"✅ The update is secure and has been verified.")
            if not self.helper is None: self.helper.UpDateOutput(f"✅ The update is secure and has been verified.")
            return True
        else:
            logging.debug(f"❌ Warning: Update verification failed! The file does not match.")
            if not self.helper is None: self.helper.UpDateOutput(f"❌ Warning: Update verification failed! The file does not match.")
            return False

    def apply_update(self, update_file):
        """ Run the update file and restart the application """
        try:
            logging.debug(f"🔄 Installing the update...")
            if not self.helper is None: self.helper.UpDateOutput(f"🔄 Installing the update...")

            if self.os_type == "windows":
                subprocess.Popen(update_file, shell=True)
            elif self.os_type == "macos":
                subprocess.Popen(["open", update_file])
            elif self.os_type == "linux":
                subprocess.Popen(["chmod", "+x", update_file])
                subprocess.Popen(["python3", update_file])
                # os.remove(os.path.join(os.getcwd(), f"marketingtool_{self.version}"))
            logging.debug(f"✅ Update applied successfully!")
            if not self.helper is None: self.helper.UpDateOutput(f"✅ Update applied successfully!")
            
            sys.exit(0)  # Close the application to restart after the update
        except Exception as e:
            logging.info(f"Error while installing the update: {e}")
            if not self.helper is None: self.helper.UpDateOutput(f"Error while installing the update")

    def download_patch(self, url):
        try:
            response = requests.get(url, stream=True)
            patch_file = "update.patch"

            with open(patch_file, "wb") as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)

            logging.debug(f"✅ The differential update file has been downloaded successfully.")
            if not self.helper is None: self.helper.UpDateOutput(f"✅ The differential update file has been downloaded successfully.")
            return patch_file
        except Exception as e:
            logging.info(f"❌ Error while downloading the update: {e}")
            if not self.helper is None: self.helper.UpDateOutput(f"❌ Error while downloading the update: {e}")
            return None

    def apply_patch(self, patch_file):
        try:
            if self.os_type == "windows":
                subprocess.run(["bspatch", "current_version.exe", "new_version.exe", patch_file])
            else:
                subprocess.run(["bspatch", "current_version", "new_version", patch_file])

            logging.debug(f"✅ The update has been applied successfully!")
            if not self.helper is None: self.helper.UpDateOutput(f"✅ The update has been applied successfully!")
        except Exception as e:
            logging.info(f"❌ Error while applying the update: {e}")
            if not self.helper is None: self.helper.UpDateOutput(f"❌ Error while applying the update: {e}")
