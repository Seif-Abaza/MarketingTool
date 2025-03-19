import logging
import os
import sys

from PySide6.QtCore import QSettings, Qt , QUrl
from PySide6.QtWidgets import QApplication, QDialog
from PySide6.QtGui import QDesktopServices

from Interface.keyapp_ui import Ui_Dialog as KeyApp
from utils.Security import Security
from utils.systeminfo import hash_computer
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
IS_DEBUG = bool(os.getenv("MT_DEBUG", False))

class Keygen(KeyApp, QDialog):
    SETTING_KEY = f"MT-{hash_computer()}"
    def __init__(self, parent=None, reset: bool = False):
        super().__init__(parent)
        if IS_DEBUG:
            logging.warning(f"Run KeyGen Class")

        self.security_file = "../reg.bin"
        self.security = Security(self.SETTING_KEY)
        self.setupUi(self)
        self.setWindowTitle("Key for Application")
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint & ~Qt.WindowMinimizeButtonHint)
        self.setFixedSize(self.size())
        self.setWindowFlags(Qt.Window | Qt.WindowCloseButtonHint)

        self.label_10.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.label_10.setOpenExternalLinks(True)
        
        self.label_13.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.label_13.setOpenExternalLinks(True)
        
        self.label_14.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.label_14.setOpenExternalLinks(True)
        
        self.label_4.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.label_4.setOpenExternalLinks(True)
        
        # Get the screen geometry
        screen_geometry = QApplication.primaryScreen().geometry()

        # Get the dialog's size
        dialog_size = self.geometry()

        # Calculate center position
        x = (screen_geometry.width() - dialog_size.width()) // 2
        y = (screen_geometry.height() - dialog_size.height()) // 2

        # Move the dialog to the center
        self.move(x, y)
        self.buttonBox.rejected.connect(self.reject)
        reg_settings = QSettings(self.SETTING_KEY, "MarketMiner")

        if reset:
            if IS_DEBUG:
                logging.warning(f"Remove Old Save File")
            reg_settings.remove("reg_key")
            os.remove(self.security_file)
            

    def save_user_in_setting(self, key: str, hash: str):
        if not key is None:
            reg_settings = QSettings(self.SETTING_KEY, "MarketMiner")
            if IS_DEBUG:
                logging.warning(f"Save Key {key} and Hash {hash}")
            reg_settings.setValue("reg_key", key)
            reg_settings.setValue("reg_hash", hash)
            if IS_DEBUG:
                logging.warning(f"Save in Binary File {self.security_file}")
            self.security.save_to_binary_file([key, hash], self.security_file)

    def get_user_key(self):
        reg_settings = QSettings(self.SETTING_KEY, "MarketMiner")
        Key = reg_settings.value("reg_key")
        if IS_DEBUG:
            logging.warning(f"Get Key from Regester {Key}")
        if Key == None:
            if os.path.exists(self.security_file):
                Key = self.security.read_from_binary_file(self.security_file)[0]
                if IS_DEBUG:
                    logging.warning(f"Get Key from Binary {Key}")
            else:
                return None
        # logging.warning(f"Key : {Key}")
        return Key

    def get_user_hash(self):
        reg_settings = QSettings(self.SETTING_KEY, "MarketMiner")
        Hashing = reg_settings.value("reg_hash")
        if IS_DEBUG:
            logging.warning(f"Get Hash from Regester {Hashing}")
        if Hashing == None:
            if os.path.exists(self.security_file):
                Hashing = self.security.read_from_binary_file(self.security_file)[1]
                if IS_DEBUG:
                    logging.warning(f"Get Hash from Binary {Hashing}")
            else:
                if IS_DEBUG:
                    logging.warning(f"Nothing In Regeter and Binary")
                return None
        return Hashing
