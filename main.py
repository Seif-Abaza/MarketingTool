import asyncio
import importlib.util
import logging
import os
import shutil
import socket
import subprocess
import sys
import threading

import requests
from nacl.public import Box, PrivateKey, PublicKey
from PySide6.QtCore import QSettings, QStringListModel, Qt, QTranslator
from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QMainWindow,
    QMessageBox,
    QSizePolicy,
    QVBoxLayout,
)

from Classes.about import about
from Classes.Keygen import Keygen
from Classes.MailGenerator import MailGenerator
from Classes.PhoneGenerator import PhoneGenerator
from Classes.PopupDialog import PopupDialog
from Classes.Settings import SETTINGS_KEYS_TO_ELEMENT_KEYS, Settings
from Facebook.Facebook import Facebook
from Interface.mainwindow_ui import Ui_MainWindow
from Telegram.sTelegram import sTelegram
from utils.DBManager import DBManager
from utils.helper import helper
from utils.Security import Security
from utils.systeminfo import hash_computer
from utils.Updater import Updater
from WhatsApp.WhatsApp import WhatsApp

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "Classes")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "Interface")))

IS_DEBUG = bool(os.getenv("MT_DEBUG", False))

if IS_DEBUG:
    API_URL = "http://127.0.0.1:23004"
else:
    API_URL = "http://172.86.114.80:23004"

CURRENT_VERSION = "2.0.1"

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "./Interface/"))
)


class MainWindw(QMainWindow, Ui_MainWindow):
    def __init__(
        self, parent=None, databasemode: str = None, database=None, settings=None
    ):
        super().__init__(parent)
        self.setupUi(self)
        self.database = database
        self.settings = settings
        self.helper = helper()
        self.setWindowTitle(f"MarketMiner v{CURRENT_VERSION}")

        self.centralLayout = QVBoxLayout(self.centralwidget)
        self.centralLayout.setContentsMargins(10, 10, 10, 10)
        self.centralLayout.addWidget(self.splitter)
        self.setMinimumSize(800, 600)
        self.groupBox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.groupBox_2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.listView.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.model = QStringListModel()
        self.Output_Item = []
        self.listView.setModel(self.model)
        self.btnClear.clicked.connect(self.ClearOutput)
        self.workSetting = self.WorkingSettings()

        # Media Button
        self.pushButton.setEnabled(False)
        self.pushButton_2.setEnabled(False)
        self.pushButton_3.setEnabled(False)

        self.label_4.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.label_4.setOpenExternalLinks(True)

        for media in self.settings.value("can_use"):
            match media.lower():
                case "telegram":
                    dir1_path = os.path.join(
                        os.getcwd(), "Sessions/teleSession.session"
                    )
                    if os.path.exists(dir1_path):
                        self.pushButton.clicked.connect(
                            lambda: self.on_dialog_order("Telegram")
                        )
                        self.pushButton.setEnabled(True)
                    else:
                        self.pushButton.setEnabled(False)
                case "whatsapp":
                    dir1_path = os.path.join(os.getcwd(), "Sessions/whatsapp")
                    if os.path.exists(dir1_path):
                        self.pushButton_2.clicked.connect(
                            lambda: self.on_dialog_order("WhatsApp")
                        )
                        self.pushButton_2.setEnabled(True)
                    else:
                        self.pushButton_2.setEnabled(False)
                case "facebook":
                    dir1_path = os.path.join(os.getcwd(), "Sessions/facebook")
                    if os.path.exists(dir1_path):
                        self.pushButton_3.clicked.connect(
                            lambda: self.on_dialog_order("Facebook")
                        )
                        self.pushButton_3.setEnabled(True)
                    else:
                        self.pushButton_3.setEnabled(False)
        self.UpDateOutput("....")
        # Menus

        self.menuDatabase.setEnabled(self.settings.value("can_access_numbers"))
        self.menuNetwork.setEnabled(self.settings.value("can_network"))
        self.action_Settings.triggered.connect(self.on_settings_click)
        self.actionGet_Mobile_Number.setEnabled(self.settings.value("can_sms"))
        self.actionGet_Mobile_Number.triggered.connect(self.on_get_mobile_number)
        self.actionGet_Temp_Mail.setEnabled(self.settings.value("can_tmp_mail"))
        self.actionGet_Temp_Mail.triggered.connect(self.on_get_temp_mail)

        self.actionCreator.triggered.connect(self.show_about)
        self.actionCheck_Update.triggered.connect(self.checkUpdate)

        self.actionTelegram.triggered.connect(self.reset_telegram)
        self.actionWhatsApp.triggered.connect(self.reset_whatsapp)
        self.actionFacebook.triggered.connect(self.reset_facebook)

        # StatusBar
        self.statusBar().showMessage(databasemode)
        self.show()

    def reset_telegram(self):
        dir1_path = os.path.join(os.getcwd(), "Sessions/teleSession.session")
        if os.path.exists(dir1_path):
            os.remove(dir1_path)
        sTelegram(settings=self.settings, needReset=True)
        QMessageBox.information(
            self,
            "Telegram",
            "Telegram is Reset",
            QMessageBox.StandardButton.Ok,
        )

    def reset_whatsapp(self):
        dir1_path = os.path.join(os.getcwd(), "Sessions/whatsapp")
        if os.path.exists(dir1_path):
            shutil.rmtree(dir1_path, ignore_errors=True)

        if WhatsApp(runReset=True).reLogin(userdata=dir1_path):
            QMessageBox.information(
                self,
                "WhatsApp",
                "WhatsApp is Reset",
                QMessageBox.StandardButton.Ok,
            )

    def reset_facebook(self):
        dir1_path = os.path.join(os.getcwd(), "Sessions/facebook")
        if os.path.exists(dir1_path):
            shutil.rmtree(dir1_path, ignore_errors=True)
        if Facebook(reset=True).reset(dir1_path, self.settings):
            QMessageBox.information(
                self,
                "Facebook",
                "Facebook is Reset",
                QMessageBox.StandardButton.Ok,
            )

    def show_about(self):
        about(self).exec()

    def checkUpdate(self):
        try:
            self.UpDateOutput(f"Check Update , current version {CURRENT_VERSION}")
            Updater(server_url=API_URL, version=CURRENT_VERSION, OutList=self.listView)
        except Exception:
            pass

    def WorkingSettings(self):
        return {
            "default_output": self.settings.value(SETTINGS_KEYS_TO_ELEMENT_KEYS[0]),
            "chrom_driver_path": self.settings.value(SETTINGS_KEYS_TO_ELEMENT_KEYS[1]),
            "tg_api_id": self.settings.value(SETTINGS_KEYS_TO_ELEMENT_KEYS[2]),
            "tg_api_hash": self.settings.value(SETTINGS_KEYS_TO_ELEMENT_KEYS[3]),
            "tg_phone": self.settings.value(SETTINGS_KEYS_TO_ELEMENT_KEYS[4]),
            "fb_username": self.settings.value(SETTINGS_KEYS_TO_ELEMENT_KEYS[5]),
            "fb_password": self.settings.value(SETTINGS_KEYS_TO_ELEMENT_KEYS[6]),
        }

    def on_dialog_order(self, service):
        dialog = PopupDialog(
            self,
            settings=self.workSetting,
            database=self.database,
            output=self.listView,
            gSettings=self.settings,
        )
        self._initWidget(dialog)

        match service:
            case "Telegram":
                dialog.setWindowTitle("Telegram")
                dialog.tabTelegram.setVisible(True)
                dialog.tabWhatsApp.setVisible(False)
                dialog.tabFacebook.setVisible(False)
            case "WhatsApp":
                dialog.setWindowTitle("WhatsApp")
                dialog.tabTelegram.setVisible(False)
                dialog.tabWhatsApp.setVisible(True)
                dialog.tabFacebook.setVisible(False)
            case "Facebook":
                dialog.setWindowTitle("Facebook")
                dialog.tabTelegram.setVisible(False)
                dialog.tabWhatsApp.setVisible(False)
                dialog.tabFacebook.setVisible(True)
        dialog.progress_signal.connect(self.update_progress)
        dialog.exec()

    def on_get_mobile_number(self):
        dialog = PhoneGenerator(
            self, database=self.database, settings=self.settings, server_url=API_URL
        )
        dialog.setWindowTitle("Get Mobile Number")
        dialog.exec()

    def on_get_temp_mail(self):
        dialog = MailGenerator(self)
        dialog.setWindowTitle("Get Temp Mail")
        dialog.exec()

    def on_settings_click(self):
        settings = Settings(self, self.settings)
        settings.setWindowTitle("Settings")
        if settings.exec() == QDialog.Accepted:
            QMessageBox.information(self, "Settings", "Setting is Saved.")

    def ClearOutput(self):
        self.Output_Item = []
        self.model.setStringList(self.Output_Item)
        self.listView.setModel(self.model)

    def UpDateOutput(self, String: str):
        String = String.strip()
        if String:
            self.Output_Item.append(String)
            self.model.setStringList(self.Output_Item)

    def update_progress(self, message: str, update: bool):
        self.lblStatus.setText(message)
        if update:
            self.reCalculateAll()

    def reCalculateAll(self):
        self.UpDateOutput("Please Wait...")
        try:
            if IS_DEBUG:
                logging.warning(f"Calculate Database")
            # self.window.groupBox.setEnabled(False)
            CountTelegram = self.database.get_count_of_table("Telegram")
            CountFacebook = self.database.get_count_of_table("facebook")
            CountWhatsApp = self.database.get_count_of_table("phone_numbers")
            CountOfUsers = int(CountTelegram + CountFacebook + CountWhatsApp)
            # MessagePostToday = int(self.database.get_count_of_table("facebook_group_message_sended", True))
            MessageSendToday = int(
                self.database.get_count_of_table("total_msg_post", True)
            )
            self.window.lblusers.setText(str(CountOfUsers))
            self.window.lblmsg.setText(str(MessageSendToday))
            # self.window.lblpost.setText(str(MessagePostToday))
            # self.window.groupBox.setEnabled(True)
        except Exception as e:
            logging.error(f"Error : {e}")

    def _initWidget(self, dialog: PopupDialog):
        dialog.groupBox_5.setVisible(False)
        dialog.frame_3.setVisible(False)
        dialog.frmFileList1.setVisible(False)
        dialog.frmFileList4.setVisible(False)
        dialog.frm_wp_1.setVisible(False)
        dialog.frm_wp_3.setVisible(False)


class main_class:
    connect_database = ""

    def __init__(self):
        self.SMSActivate = None
        self.settings = QSettings(str(hash_computer()), "MarketingTool")
        if self._check_keys():
            if IS_DEBUG:
                logging.warning(f"Check Key is Done")
            if self._check_update() is None:
                if IS_DEBUG:
                    logging.warning(f"Check Update is Done")
                UserAccountName = self._get_account_informations()
                if IS_DEBUG:
                    logging.warning(
                        f"Get Account Information is Done {UserAccountName}"
                    )
                if UserAccountName is None:
                    if IS_DEBUG:
                        logging.warning(f"User Account is None , Reset Regestration")
                    self._check_keys(reset=True)
                elif not UserAccountName is None:
                    if IS_DEBUG:
                        logging.warning(f"User Account is Not None")
                    try:
                        if not self.settings.value("default_output"):
                            self.ensure_playwright_installed()
                            settings = Settings()
                            settings.setWindowTitle("Settings")
                            if settings.exec() == QDialog.Accepted:
                                QMessageBox.information(
                                    self,
                                    "Settings",
                                    "Must restart MarketMiner Now.",
                                    QMessageBox.StandardButton.Ok,
                                )
                            sys.exit()
                        else:
                            self.database = DBManager(
                                settings=self.settings,
                            )

                            if IS_DEBUG:
                                logging.warning(f"Run Database in Debug Mode")
                            self.connect_database = f"Database is Connect | Account Name : {UserAccountName}"
                            self.database.create_table("total_msg_post")
                            self.database.create_table("message_history")
                    except Exception:
                        self.connect_database = (
                            f"Database not Connect | Account Name : {UserAccountName}"
                        )
                    if IS_DEBUG:
                        logging.warning(
                            f"Calculation is Done and I will open Main Window"
                        )
                    self.window = MainWindw(
                        databasemode=self.connect_database,
                        database=self.database,
                        settings=self.settings,
                    )
                    print("Calculation")
                    self.calculation()
                    # self.window.exec()
                    # thread.join()

                    # if self.window is None:
                    #     self.database.close_connection()
                    #     self.window.close()
                else:
                    sys.exit()
        else:
            if IS_DEBUG:
                logging.warning(f"Check Key Retern With False")
            QMessageBox.information(
                None, f"MarketMiner {CURRENT_VERSION}", "Try Later", QMessageBox.Ok
            )
            sys.exit()

    def calculation(self):
        try:
            if IS_DEBUG:
                logging.warning(f"Calculate Database")
            # self.window.groupBox.setEnabled(False)
            CountTelegram = self.database.get_count_of_table("Telegram")
            CountFacebook = self.database.get_count_of_table("facebook")
            CountWhatsApp = self.database.get_count_of_table("phone_numbers")
            CountOfUsers = int(CountTelegram + CountFacebook + CountWhatsApp)
            # MessagePostToday = int(self.database.get_count_of_table("facebook_group_message_sended", True))
            MessageSendToday = int(
                self.database.get_count_of_table("total_msg_post", True)
            )
            self.window.lblusers.setText(str(CountOfUsers))
            self.window.lblmsg.setText(str(MessageSendToday))
            # self.window.lblpost.setText(str(MessagePostToday))
            # self.window.groupBox.setEnabled(True)
        except Exception as e:
            logging.error(f"Error : {e}")

    def ensure_playwright_installed(self):
        package_name = "playwright"
        # Check if Playwright is installed
        if importlib.util.find_spec(package_name) is None:
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", package_name]
            )

        # Run Playwright install command
        subprocess.check_call(
            [sys.executable, "-m", "playwright", "install"], stderr=None
        )

    def is_connected(self):
        try:
            socket.create_connection(("8.8.8.8", 53), timeout=5)
            return True
        except OSError:
            return False

    def _check_update(self):
        try:
            Updater(server_url=API_URL, version=CURRENT_VERSION)
        except Exception:
            pass

    def _get_account_informations(self) -> str:
        keydialog = Keygen()
        hashkey = keydialog.get_user_key()
        try:
            get_account = requests.post(
                f"{API_URL}/get_account",
                json={
                    "hash": str(hashkey),
                    "com_hash": str(hash_computer()),
                },
            )
        except Exception:
            QMessageBox.information(
                None, "Account Holding", "Wait and try Later Please.", QMessageBox.Ok
            )
            sys.exit()

        if get_account.status_code == 200 and get_account.json().get("success"):
            KeyList = [
                "sms_key",
                "can_sms",
                "can_sms_service",
                "can_tmp_mail",
                "can_super_fast",
                "can_access_numbers",
                "can_export_data",
                "can_network",
                "can_scrip",
                "can_send",
                "can_use_ai",
                "can_use_database_offline",
                "can_use_database_online",
                "can_use",
            ]

            username = get_account.json().get("user_name")
            allow_user = get_account.json().get("user_allow")

            for Key in KeyList:
                if Key == "can_use":
                    self.settings.setValue(Key, allow_user[Key].split(","))
                elif Key == "can_sms_service":
                    self.settings.setValue(Key, allow_user[Key].split(","))
                else:
                    self.settings.setValue(Key, allow_user[Key])

            # if IS_DEBUG:
            #     self.SMSActivate.debug_mode = IS_DEBUG

        elif get_account.status_code == 600 and get_account.json().get("success"):
            QMessageBox.information(
                None, "Account Holding", get_account.json().get("msg"), QMessageBox.Ok
            )
            sys.exit()
        else:
            return None
        return username

    def _check_keys(self, reset: bool = False):
        keyappObj = Keygen(reset=reset)
        if keyappObj.get_user_key() is None:
            if IS_DEBUG:
                logging.warning(f"User Key is None and i will Open Keys Dialog")
            if keyappObj.exec() == QDialog.Accepted:
                Username = keyappObj.txtAppID.text()
                Phone = keyappObj.txtKey.text()
                Mail = keyappObj.txtMail.text()
                Txid = keyappObj.txtTxid.text()
                if Username == "" or Phone == "" or Mail == "" or Txid == "":
                    QMessageBox.critical(
                        None, "Error", "You must add all input", QMessageBox.Ok
                    )
                    if IS_DEBUG:
                        logging.warning(f"Input is Nothing")
                else:
                    if IS_DEBUG:
                        logging.warning(f"Check Internet Connection")
                    if self.is_connected():
                        if IS_DEBUG:
                            logging.warning(f"Connect to Server {API_URL}")
                        return self._connect_to_server(
                            keyappObj, Username, Phone, Mail, Txid
                        )
                    else:
                        if IS_DEBUG:
                            logging.warning(f"Internet Not Working")
                        QMessageBox.critical(
                            None, "Error", "Internet Not Connected", QMessageBox.Ok
                        )
                        return False
            else:
                sys.exit(0)
        else:
            if keyappObj.get_user_hash() == hash_computer():
                return True
            else:
                self._check_keys(True)
            return False

    def _connect_to_server(self, window_dialog, Username, Phone, Mail, Txid):
        try:
            Server_Url = f"{API_URL}/get_public_key"
            response = requests.get(Server_Url)
            if IS_DEBUG:
                logging.warning(f"Connect to Server {Server_Url}")
            if response.status_code == 200:
                if IS_DEBUG:
                    logging.warning(f"Server Anssering with Code 200")
                server_public_key = PublicKey(
                    bytes.fromhex(response.json().get("public_key"))
                )
                if IS_DEBUG:
                    logging.warning(
                        f"Get Public Key {server_public_key.encode().hex()}"
                    )
            else:
                if IS_DEBUG:
                    logging.warning(f"Can't Get Public Key")
                QMessageBox.critical(
                    None, "Error", "Server Not Connected", QMessageBox.Ok
                )
                sys.exit()

            client_private_key = PrivateKey.generate()
            client_public_key = client_private_key.public_key
            if IS_DEBUG:
                logging.warning(f"Generate Application Public and Private Keys")
            if window_dialog.get_user_key() == client_private_key:
                if IS_DEBUG:
                    logging.warning(f"This User is Not New")
                is_new_user = False
            else:
                if IS_DEBUG:
                    logging.warning(f"This User is New")
                is_new_user = True

            computer_hash = hash_computer()
            user_data = f"Name:{Username},Email:{Mail},Phone:{Phone},Txid:{Txid},isNew:{is_new_user},computer:{computer_hash}".encode()
            if IS_DEBUG:
                logging.warning(
                    f"Computer Hash is {computer_hash} and User Data is {user_data}"
                )

            box = Box(client_private_key, server_public_key)
            encrypted_data = box.encrypt(user_data)
            if IS_DEBUG:
                logging.warning(f"Encryption Data for Send it to the Server")

            verify_response = requests.post(
                f"{API_URL}/verify_data",
                json={
                    "encrypted_data": encrypted_data.hex(),
                    "client_public_key": client_public_key.encode().hex(),
                },
            )

            # معالجة الرد
            if verify_response.status_code == 200 and verify_response.json().get(
                "success"
            ):
                if IS_DEBUG:
                    logging.warning(f"Server Ansser with {verify_response.status_code}")
                Data = verify_response.json().get("hash")
                window_dialog.save_user_in_setting(Data, computer_hash)
                return True
            elif verify_response.status_code == 600 and verify_response.json().get(
                "success"
            ):
                if IS_DEBUG:
                    logging.warning(f"Server Ansser with {verify_response.status_code}")
                Data = verify_response.json().get("msg")
                hashuser = verify_response.json().get("hash")

                window_dialog.save_user_in_setting(hashuser, computer_hash)
                QMessageBox.information(None, "Information", Data, QMessageBox.Ok)
                return False
        except Exception:
            QMessageBox.critical(
                None, "Error", "Internet Not Connected", QMessageBox.Ok
            )


if __name__ == "__main__":
    project_dir = os.getcwd()
    ImportantDirs = ["Sessions", "Log"]
    for mDir in ImportantDirs:
        dir1_path = os.path.join(project_dir, mDir)
        if not os.path.exists(dir1_path):
            os.makedirs(dir1_path)

    app = QApplication(sys.argv)
    translator = QTranslator()
    if os.path.exists("setup"):
        helping = Security("MarketingTools")
        lang = helping.read_and_decrypt_data_from_file("setup")
        if not lang is None:
            if lang != "en":
                langfile = f"locat/{lang}.qm"
                if not os.path.exists(langfile):
                    langfile = f"_internal/{langfile}"

                if translator.load(langfile):
                    app.installTranslator(translator)
        else:
            app.removeTranslator(translator)
    else:
        app.removeTranslator(translator)

    # AppArgs = sys.argv[1:]
    # for item in AppArgs:
    #     Keys = item.split('=')
    #     print(Keys[0])
    #     print(Keys[1])
    #     if Keys[0].startswith('--'):
    #         match Keys[0]:
    #             case ['--debug']:
    #                 print(f'Application in Debug Mode {bool(Keys[1])}')
    #                 IS_DEBUG = bool(Keys[1])
    #             case ['--cronjob']:
    #                 print(f'Application in CronJob Mode {Keys[1]}')
    #             case _:
    #                 pass

    if IS_DEBUG:
        print("Application in Debug Mode")
        logging.basicConfig(filename="Log/debug.log", level=logging.WARNING)
    else:
        print("Application in Live Mode")
        logging.basicConfig(filename="Log/error.log", level=logging.ERROR)

    main_class()
    sys.exit(app.exec())
