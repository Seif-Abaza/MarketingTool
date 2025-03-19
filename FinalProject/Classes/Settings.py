from PySide6.QtWidgets import QDialog, QFileDialog, QMessageBox

from Interface.settings_ui import Ui_Dialog as SettingsDialog
from utils.helper import helper
from utils.Security import Security
import os

SETTINGS_KEYS_TO_ELEMENT_KEYS = [
    "default_output",
    "chrom_driver_path",
    "tg_api_id",
    "tg_api_hash",
    "tg_phone",
    "fb_username",
    "fb_password",
    "app_language",
]

Language = [
    "English",  # en
    "العربية",  # ar
    "Русский",  # ru
    "Français",  # fr
    "Español",  # es
    "German",  # ge
    "Italiano",  # it
    "Português",  # pt
    "Türkçe",  # tr
    "فارسي",  # fa
    "ქართული ენა",  # ge
]


class Settings(SettingsDialog, QDialog):

    def __init__(self, parent=None, Setting=None):
        super().__init__(parent)
        self.setupUi(self)
        self.settings = Setting
        self.helper = helper()
        self.buttonBox.accepted.connect(self.dialog_modeless_close)
        self.buttonBox.rejected.connect(self.reject)
        self.btnOutput.clicked.connect(self.browse_folder)
        self.btnChrom.clicked.connect(self.on_file_open)
        self.comLang.addItems(Language)
        if self.settings.value(SETTINGS_KEYS_TO_ELEMENT_KEYS[7]):
            self.comLang.setCurrentText(
                self.settings.value(SETTINGS_KEYS_TO_ELEMENT_KEYS[7])
            )
        else:
            self.comLang.setCurrentText(Language[0])

        self.comLang.currentIndexChanged.connect(self.on_change_language)

        self.txtOutput.setText(self.settings.value(SETTINGS_KEYS_TO_ELEMENT_KEYS[0]))
        self.txtChromDriver.setText(
            self.settings.value(SETTINGS_KEYS_TO_ELEMENT_KEYS[1])
        )
        self.txtTG_ID.setText(self.settings.value(SETTINGS_KEYS_TO_ELEMENT_KEYS[2]))
        self.txtTG_Hash.setText(self.settings.value(SETTINGS_KEYS_TO_ELEMENT_KEYS[3]))
        self.txtTG_Phone.setText(self.settings.value(SETTINGS_KEYS_TO_ELEMENT_KEYS[4]))
        self.txtFB_User.setText(self.settings.value(SETTINGS_KEYS_TO_ELEMENT_KEYS[5]))
        self.txtFB_Pass.setText(self.settings.value(SETTINGS_KEYS_TO_ELEMENT_KEYS[6]))

    def dialog_modeless_close(self):
        self.settings.setValue(SETTINGS_KEYS_TO_ELEMENT_KEYS[0], self.txtOutput.text())
        self.settings.setValue(
            SETTINGS_KEYS_TO_ELEMENT_KEYS[1], self.txtChromDriver.text()
        )
        self.settings.setValue(SETTINGS_KEYS_TO_ELEMENT_KEYS[2], self.txtTG_ID.text())
        self.settings.setValue(SETTINGS_KEYS_TO_ELEMENT_KEYS[3], self.txtTG_Hash.text())
        self.settings.setValue(
            SETTINGS_KEYS_TO_ELEMENT_KEYS[4], self.txtTG_Phone.text()
        )
        self.settings.setValue(SETTINGS_KEYS_TO_ELEMENT_KEYS[5], self.txtFB_User.text())
        self.settings.setValue(SETTINGS_KEYS_TO_ELEMENT_KEYS[6], self.txtFB_Pass.text())
        self.accept()

    def on_change_language(self):
        language = self.comLang.currentText()
        self.settings.setValue(SETTINGS_KEYS_TO_ELEMENT_KEYS[7], language)
        helping = Security("MarketingTools")
        match self.comLang.currentText():
            case "English":
                lang = "en"
            case "العربية":
                lang = "ar"
            case "Русский":
                lang = "ru"
            case "Français":
                lang = "fr"
            case "Español":
                lang = "es"
            case "German":
                lang = "ge"
            case "Italiano":
                lang = "it"
            case "Português":
                lang = "pt"
            case "Türkçe":
                lang = "tr"
            case "فارسي":
                lang = "fa"
            case "ქართული ენა":
                lang = "ge"
        if lang == 'en':
            if os.path.exists("setup"):
                os.remove("setup")
        else:
            helping.write_encrypted_data_to_file("setup", lang)
        
        QMessageBox.information(
            self, "Language", "Language is changed, Please restart the application."
        )

    def browse_folder(self):
        """Open a folder selection dialog and update label"""
        folder_path = QFileDialog.getExistingDirectory(self, "Select a Folder")
        if folder_path:  # If a folder is selected
            self.txtOutput.setText(folder_path)

    def on_file_open(self):
        path, _ = QFileDialog.getOpenFileName(self, "Select Chrom Driver", "/")
        if path:
            self.txtChromDriver.setText(path)
