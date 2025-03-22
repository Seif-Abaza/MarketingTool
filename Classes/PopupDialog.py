import asyncio
import inspect
import logging
import os
import sys
import traceback
import uuid

from PySide6.QtCore import QThread, Signal, Slot
from PySide6.QtWidgets import (
    QComboBox,
    QDialog,
    QFileDialog,
    QLineEdit,
    QListView,
    QListWidget,
    QMessageBox,
    QProgressDialog,
)

from Classes.ComboBoxDialog import ComboBoxDialog as InputComboBox
from Classes.ExcelTable import ExcelTable as ET
from Interface.tab_media_ui import Ui_Dialog
from marketing import marketing
from utils.helper import AI_Window, AiWorker, helper
from utils.PhoneParsing import PhoneParsing

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class Worker(QThread):
    progress = Signal(str, bool)

    def __init__(self, service, action, *args, **kwargs):
        super().__init__()
        self.service = service
        self.action = action
        self.args = args
        self.kwargs = kwargs

    def run(self):
        try:
            self.progress.emit(f"{self.service} is working...", False)
            match self.service:
                case "Telegram":
                    match self.action:
                        case 0:
                            if self.kwargs["SettingCanSend"]:
                                asyncio.run(
                                    self.run_async_task(
                                        self.kwargs[
                                            "marketing"
                                        ].parse_telegram_send_to_member(
                                            message=self.kwargs["message"],
                                            file_send=self.kwargs["file_send"],
                                            file_list=self.kwargs["file_list"],
                                            category=self.kwargs["category"],
                                            slogin=self.kwargs["slogin"],
                                            msg_img=self.kwargs["msg_img"],
                                            compan=self.kwargs["compan"],
                                            translat=self.kwargs["translat"],
                                        )
                                    )
                                )
                                self.progress.emit(
                                    "Telegram : Send Message is Done", True
                                )
                            else:
                                self.progress.emit(
                                    "Telegram : you can't use this function", False
                                )
                        case 1:
                            if self.kwargs["SettingCanScrip"]:
                                FileList = self.kwargs["filelist"]
                                Category = self.kwargs["category"]
                                asyncio.run(
                                    self.run_async_task(
                                        self.kwargs["marketing"].parse_telegram_group(
                                            pathfile=FileList, category=Category
                                        )
                                    )
                                )
                                self.progress.emit(
                                    "Telegram : Parsing Groups is Done", False
                                )
                            else:
                                self.progress.emit(
                                    "Telegram : you can't use this function", False
                                )
                        case 2:
                            if self.kwargs["SettingCanSend"]:
                                main_group = self.kwargs["main_group"]
                                target_group = self.kwargs["target_group"]
                                max_data = self.kwargs["max_date"]
                                list1 = self.kwargs["list1"]
                                list2 = self.kwargs["list2"]
                                msgs_type = self.kwargs["mode"]
                                asyncio.run(
                                    self.run_async_task(
                                        self.kwargs[
                                            "marketing"
                                        ].parse_telegram_message_group(
                                            mode=msgs_type,
                                            max_date=max_data,
                                            target_channel=target_group,
                                            main_channel=main_group,
                                            list1=list1,
                                            list2=list2,
                                        )
                                    )
                                )
                                self.progress.emit(
                                    "Telegram : Parsing Messages in the Groups and Copy it is Done",
                                    False,
                                )
                            else:
                                self.progress.emit(
                                    "Telegram : you can't use this function", False
                                )
                        case 3:
                            if self.kwargs["SettingCanSend"]:
                                GroupName = self.kwargs["target_group"]
                                Category = self.kwargs["category"]
                                ListGroup = self.kwargs["list_group"]
                                asyncio.run(
                                    self.run_async_task(
                                        self.kwargs[
                                            "marketing"
                                        ].parse_add_members_to_channel(
                                            channel_name=GroupName,
                                            category=Category,
                                            member_list=ListGroup,
                                        )
                                    )
                                )

                                self.progress.emit(
                                    f"Telegram : Add new members to {GroupName} is Done.",
                                    True,
                                )
                            else:
                                self.progress.emit(
                                    f"Telegram : you can't use this function.", False
                                )

                case "WhatsApp":
                    match self.action:
                        case 0:
                            if self.kwargs["SettingCanSend"]:
                                message = self.kwargs["message"]
                                slogin = self.kwargs["slogin"] or None
                                category = self.kwargs["category"] or None
                                file_send = self.kwargs["file_send"] or None
                                country = self.kwargs["country"] or None
                                timezone = self.kwargs["timezone"] or None
                                list_file = self.kwargs["list_file"]
                                comoan_name = self.kwargs["compan"]
                                translation = self.kwargs["translation"]
                                asyncio.run(
                                    self.run_async_task(
                                        self.kwargs[
                                            "marketing"
                                        ].send_message_to_whatsapp(
                                            message=message,
                                            slogin=slogin,
                                            category=category,
                                            file_send=file_send,
                                            country=country,
                                            timezone=timezone,
                                            list_file=list_file,
                                            compan=comoan_name,
                                            translation=translation,
                                        )
                                    )
                                )
                                self.progress.emit(
                                    f"WhatsApp : Send Message is Done", True
                                )
                            else:
                                self.progress.emit(
                                    f"WhatsApp : you can't use this function", False
                                )

                        case 1:
                            if self.kwargs["SettingCanScrip"]:
                                Category = self.kwargs["Category"]
                                asyncio.run(
                                    self.run_async_task(
                                        self.kwargs["marketing"].parse_whatsapp_contact(
                                            category=Category
                                        )
                                    )
                                )
                                self.progress.emit(
                                    "WhatsApp : Get your Contact is Done.", True
                                )
                            else:
                                self.progress.emit(
                                    "WhatsApp : you can't use this function.", False
                                )

                        case 2:
                            if self.kwargs["SettingCanScrip"]:
                                Group_Category = self.kwargs["Group_Category"]
                                Group_Name = self.kwargs["Group_Name"]
                                asyncio.run(
                                    self.run_async_task(
                                        self.kwargs["marketing"].parse_whatsapp_group(
                                            group_name=Group_Name,
                                            category=Group_Category,
                                        )
                                    )
                                )
                                if len(Group_Name) > 0:
                                    self.progress.emit(
                                        f"WhatsApp : Scan Group {Group_Name} is Done.",
                                        True,
                                    )
                                else:
                                    self.progress.emit(
                                        f"WhatsApp : Group List is Updated.", True
                                    )
                            else:
                                self.progress.emit(
                                    f"WhatsApp : you can't use this function.", False
                                )

                case "Facebook":
                    # self.kwargs["marketing"].facebook_function()
                    match self.action:
                        case 0:
                            if self.kwargs["SettingCanSend"]:
                                Mem_Message = self.kwargs["Mem_Message"]
                                Mem_FilePath = self.kwargs["Mem_FilePath"]
                                Mem_Categorys = self.kwargs["Mem_Categorys"]
                                Mem_AI = self.kwargs["Mem_AI"]
                                Mem_CompanID = self.kwargs["CompanName"]
                                Mem_Slogin = self.kwargs["Mem_Slogin"]
                                asyncio.run(
                                    self.run_async_task(
                                        self.kwargs[
                                            "marketing"
                                        ].send_message_to_memebers(
                                            message=Mem_Message,
                                            filePath=Mem_FilePath,
                                            category=Mem_Categorys,
                                            use_AI=Mem_AI,
                                            CompanName=Mem_CompanID,
                                            Slogin=Mem_Slogin,
                                        )
                                    )
                                )
                                self.progress.emit(
                                    f"Facebook : Send To facebook is Done", True
                                )
                            else:
                                self.progress.emit(
                                    f"Facebook : you can't use this function", False
                                )
                        case 1:
                            if self.kwargs["SettingCanSend"]:
                                Group_Message = self.kwargs["Group_Message"]
                                Group_Category = self.kwargs["Group_Category"]
                                Group_FileGroupPath = self.kwargs["Group_FileGroupPath"]
                                Group_AI = self.kwargs["Group_AI"]
                                Group_CompanID = self.kwargs["CompanName"]
                                Group_Slogin = self.kwargs["Group_Slogin"]
                                asyncio.run(
                                    self.run_async_task(
                                        self.kwargs["marketing"].post_facebook_group,
                                        group_post=Group_Message,
                                        category=Group_Category,
                                        group_list=Group_FileGroupPath,
                                        use_AI=Group_AI,
                                        CompanName=Group_CompanID,
                                        Slogin=Group_Slogin,
                                    )
                                )
                                self.progress.emit(
                                    f"Facebook : Post On the Groups is Done", True
                                )
                            else:
                                self.progress.emit(
                                    f"Facebook : you can't use this function", False
                                )
                        case 2:
                            if self.kwargs["SettingCanScrip"]:
                                Group_Name = self.kwargs["Group_Name"]
                                Member_Category = self.kwargs["Member_Category"]
                                asyncio.run(
                                    self.run_async_task(
                                        self.kwargs[
                                            "marketing"
                                        ].get_members_facebook_group(
                                            category=Member_Category,
                                            group_name=Group_Name,
                                        )
                                    )
                                )
                                self.progress.emit(
                                    f"Facebook : Send To facebook groups is Done", True
                                )
                            else:
                                self.progress.emit(
                                    f"Facebook : you can't use this function", False
                                )

            self.progress.emit("Init and Run Proccessing", False)

        except Exception:
            logging.error("Popup Error : \n" + traceback.format_exc())
            self.progress.emit("Error occurred in Proccessing", False)
            return None

    async def run_async_task(self, func, *args, **kwargs):
        """Runs an async function inside the Worker thread."""
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        if inspect.iscoroutinefunction(func):
            await func(*args, **kwargs)  # إذا كانت دالة غير متزامنة
        elif inspect.iscoroutine(func):
            await func  # إذا كان كائن coroutine
        else:
            func(*args, **kwargs)

        loop.close()


class PopupDialog(Ui_Dialog, QDialog):
    progress_signal = Signal(str, bool)
    TABLE_IMPORT = "import_data"

    def __init__(
        self,
        parent=None,
        settings=None,
        gSettings=None,
        database=None,
        output: QListView = None,
    ):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.helper = helper(output)
        self.gsettings = gSettings
        self.settings = settings
        self.database = database
        self.output = output
        self.marketing = marketing(self.settings, self.database, self.output)
        self.threads = []  # Store threads
        self.gSlogin.setEnabled(False)
        self.gSlogin_2.setEnabled(False)
        self.gSlogin_3.setEnabled(False)
        self.gSlogin_4.setEnabled(False)
        # self.setWindowFlags(self.windowFlags() & Qt.CustomizeWindowHint)
        # self.setWindowFlags(self.windowFlags() & ~Qt.WindowMinMaxButtonsHint)

        self.buttonBox.accepted.connect(self.ok_clicked)
        self.buttonBox.rejected.connect(self.reject)

        self.txtCompName1.setEnabled(False)
        self.txtCompName2.setEnabled(False)

        if self.gsettings.value("can_use_ai"):
            self.useFPAI_1.setEnabled(True)
            self.useFPAI_2.setEnabled(True)
            self.useTGAI.setEnabled(True)  # Telegram AI
            self.useWPAI_1.setEnabled(True)  # WhatsApp AI
        else:
            self.useFPAI_1.setEnabled(False)
            self.useFPAI_2.setEnabled(False)
            self.useTGAI.setEnabled(False)  # Telegram AI
            self.useWPAI_1.setEnabled(False)  # WhatsApp AI

        if self.gsettings.value("can_send"):
            self.tab_tg_1.setEnabled(True)
            self.tab_tg_3.setEnabled(True)
            self.tab_tg_4.setEnabled(True)
            self.tab_wp_1.setEnabled(True)
            self.tab_fb_1.setEnabled(True)
            self.tab_fb_2.setEnabled(True)
        else:
            self.tab_tg_1.setEnabled(False)
            self.tab_tg_3.setEnabled(False)
            self.tab_tg_4.setEnabled(False)
            self.tab_wp_1.setEnabled(False)
            self.tab_fb_1.setEnabled(False)
            self.tab_fb_2.setEnabled(False)

        if self.gsettings.value("can_scrip"):
            self.tab_tg_2.setEnabled(True)
            self.tab_wp_2.setEnabled(True)
            self.tab_wp_3.setEnabled(True)
            self.tab_fb_3.setEnabled(True)
        else:
            self.tab_tg_2.setEnabled(False)
            self.tab_wp_2.setEnabled(False)
            self.tab_wp_3.setEnabled(False)
            self.tab_fb_3.setEnabled(False)

        # Telegram Side
        self.init_telegram()

        # WhatsApp Side
        self.init_whatsApp()

        # Facebook
        self.init_facebook()

    def init_facebook(self):
        self.radioButton_12.toggled.connect(self._FacebookFrames_2)
        self.radioButton_14.toggled.connect(self._FacebookFrames_3)

        # Facebook Options
        self.useFPAI_1.clicked.connect(
            lambda: self.on_compan("FP1", self.txtCompName1, Source="facebook")
        )
        self.useCompan_1.clicked.connect(
            lambda: self.on_compan("FPComp1", self.txtCompName1, Source="facebook")
        )
        self.useFP_Nothing_1.clicked.connect(
            lambda: self.on_compan("FPNone2", self.txtCompName1, Source="facebook")
        )

        self.useFPAI_2.clicked.connect(
            lambda: self.on_compan("FP2", self.txtCompName2, Source="facebook")
        )
        self.useCompan_2.clicked.connect(
            lambda: self.on_compan("FPComp2", self.txtCompName2, Source="facebook")
        )
        self.useFP_Nothing_2.clicked.connect(
            lambda: self.on_compan("FPNone2", self.txtCompName2)
        )

        self.gSlogin.setEnabled(False)
        self.gSlogin_2.setEnabled(False)
        self.txtCompName1.clear()
        self.txtCompName2.clear()

        self.ckBoth1.setCheckable(True)

        self.toolButton_10.clicked.connect(lambda: self.on_file_open(self.lineEdit_14))
        self.toolButton_11.clicked.connect(lambda: self.on_file_open(self.lineEdit_15))
        self.toolButton_15.clicked.connect(lambda: self.on_file_open(self.lineEdit_16))
        self.toolButton_12.clicked.connect(lambda: self.on_file_open(self.lineEdit_19))
        self.toolButton_13.clicked.connect(lambda: self.on_file_open(self.lineEdit_4))
        self.toolButton_14.clicked.connect(lambda: self.on_file_open(self.lineEdit_18))

        self.populate_combo_boxes_facebook()

    def init_whatsApp(self):
        self.radioButton_6.toggled.connect(self._WhatsAppFrames_1)
        self.radioButton_7.toggled.connect(self._WhatsAppFrames_3)
        self.pushButton_2.clicked.connect(self.getExceData)
        # WhatsApp Options
        self.useWPAI_1.clicked.connect(
            lambda: self.on_compan("WP", self.txtWPCompName_1, Source="whatsapp")
        )
        self.useWPCompan_1.clicked.connect(
            lambda: self.on_compan("WPComp1", self.txtWPCompName_1, Source="whatsapp")
        )
        self.useFP_Nothing_3.clicked.connect(
            lambda: self.on_compan("WPNone", self.txtWPCompName_1, Source="whatsapp")
        )
        self.comboBox_12.addItems(["Before Text", "After Text"])

        self.toolButton_6.clicked.connect(lambda: self.on_file_open(self.lineEdit_8))
        self.toolButton_8.clicked.connect(lambda: self.on_file_open(self.lineEdit_10))
        self.toolButton_7.clicked.connect(
            lambda: self.on_file_open(self.lineEdit_9, True)
        )
        self.toolButton_9.clicked.connect(
            lambda: self.on_file_open(self.lineEdit_11, True)
        )

        self.pushButton.clicked.connect(self.ok_clicked)

        self.populate_combo_boxes_whatsapp()

    def init_telegram(self):
        self.radFileList1.toggled.connect(self._TelegramFrames_1)
        self.radFileList4.toggled.connect(self._TelegramFrames_4)

        self.useTGAI.clicked.connect(
            lambda: self.on_compan("TG", self.txtCompName1_2, Source="telegram")
        )
        self.useTGCompan.clicked.connect(
            lambda: self.on_compan("TGComp", self.txtCompName1_2, Source="telegram")
        )
        self.useFP_Nothing_4.clicked.connect(
            lambda: self.on_compan("WPNone", self.txtCompName1_2, Source="telegram")
        )
        self.comboBox_11.addItems(["Before Text", "After Text"])

        self.toolButton_3.clicked.connect(
            lambda: self.on_file_open(self.lineEdit_3, True)
        )
        self.toolButton_5.clicked.connect(
            lambda: self.on_file_open(self.lineEdit_7, True)
        )

        self.txtfromlist.returnPressed.connect(
            lambda: self.add_to_list(self.txtfromlist, self.listWFrom)
        )
        self.txtTolist.returnPressed.connect(
            lambda: self.add_to_list(self.txtTolist, self.listWTo)
        )

        self.toolButton.clicked.connect(lambda: self.on_file_open(self.lineEdit))
        self.toolButton_2.clicked.connect(lambda: self.on_file_open(self.lineEdit_2))
        self.btnBrowser2.clicked.connect(
            lambda: self.on_file_open(self.txtListOfGroup2, True)
        )

        self.populate_combo_boxes_telegram()

    def populate_combo_boxes_telegram(self):
        """Fetch categories and channels from database"""
        ListOfCategorysMember = self.database.select_column("Telegram", "category")
        ListOfCategorysMemberExternal = self.database.select_column(
            self.TABLE_IMPORT, "category", {"source": "telegram"}
        )
        ListOfCategorysMember.extend(ListOfCategorysMemberExternal)

        ListOfChannels = self.database.select_column("channel", "title")
        ListOfChannelsExternal = self.database.select_column(
            self.TABLE_IMPORT, "title", {"source": "telegram"}
        )
        ListOfChannels.extend(ListOfChannelsExternal)

        ListOfCategorysMember.sort()
        ListOfChannels.sort()

        self.comboBox.addItems(ListOfCategorysMember)
        self.cmdMemCategory2.addItems(ListOfCategorysMember)
        self.cmdMemCategory4.addItems(ListOfCategorysMember)
        self.cmbCpyFrom.addItems(ListOfChannels)

    def populate_combo_boxes_whatsapp(self):
        """Fetch categories and country..etc from database"""
        Country = self.database.select_column("phone_numbers", "country")
        TimeZone = self.database.select_column("phone_numbers", "timezone")
        Category = self.database.select_column("phone_numbers", "category")
        Country.sort()
        TimeZone.sort()
        Category.sort()
        self.cmbBCountry.addItems(Country)
        self.combTimeZone.addItems(TimeZone)
        self.comboBox_5.addItems(Category)
        self.comboBox_6.addItems(Category)
        self.comContactCategory.addItems(Category)

    def populate_combo_boxes_facebook(self):
        Categorys = self.database.select_column("facebook", "category")
        Group_Categorys = self.database.select_column("facebook_groups", "category")
        if len(Group_Categorys) == 0:
            Group_Categorys = self.database.select_column(
                "facebook_group_message_sended", "category"
            )

        Groups = self.database.select_column("facebook_groups", "group_name")
        Categorys.sort()
        Group_Categorys.sort()
        Groups.sort()

        self.comboBox_7.addItems(Categorys)
        self.comboBox_9.addItems(Categorys)
        self.comboBox_8.addItems(Group_Categorys)
        self.comboBox_2.addItems(Groups)

    def _TelegramFrames_1(self):
        rbt = self.sender()
        self.lineEdit_3.setText("")
        self.frmFileList1.setVisible(rbt.isChecked())

    def _TelegramFrames_4(self):
        rbt = self.sender()
        self.lineEdit_7.setText("")
        self.frmFileList4.setVisible(rbt.isChecked())

    def _WhatsAppFrames_1(self):
        rbt = self.sender()
        self.lineEdit_9.setText("")
        self.frm_wp_1.setVisible(rbt.isChecked())

    def _WhatsAppFrames_3(self):
        rbt = self.sender()
        self.lineEdit_11.setText("")
        self.frm_wp_3.setVisible(rbt.isChecked())

    def _FacebookFrames_2(self):
        rbt = self.sender()
        self.lineEdit_4.setText("")
        self.groupBox_5.setVisible(rbt.isChecked())

    def _FacebookFrames_3(self):
        rbt = self.sender()
        self.lineEdit_18.setText("")
        self.frame_3.setVisible(rbt.isChecked())

    @Slot()
    def add_to_list(self, qtext: QLineEdit, qlist: QListWidget):
        text = qtext.text().strip()
        if text and text not in [qlist.item(i).text() for i in range(qlist.count())]:
            qlist.addItem(text)
            qtext.clear()

    def on_compan(self, Name: str, ObjectText: QComboBox, Source):
        CompanName = self.database.select_column(
            "message_history", "name", {"source": Source}
        )
        CompanName.sort()
        ObjectText.clear()
        match Name:
            case "FPComp1":
                ObjectText.setEnabled(True)
                ObjectText.setEditable(False)
                self.gSlogin.setEnabled(True)
                ObjectText.addItems(CompanName)
            case "FPComp2":
                ObjectText.setEnabled(True)
                ObjectText.setEditable(False)
                self.gSlogin_2.setEnabled(True)
                ObjectText.addItems(CompanName)
            case "FP1":
                ObjectText.clear()
                ObjectText.setEnabled(True)
                ObjectText.setEditable(True)
                self.gSlogin.setEnabled(True)
                ObjectText.addItems(CompanName)
            case "FP2":
                ObjectText.clear()
                ObjectText.setEnabled(True)
                ObjectText.setEditable(True)
                self.gSlogin_2.setEnabled(True)
                ObjectText.addItems(CompanName)
            case "WP":
                ObjectText.clear()
                ObjectText.setEnabled(True)
                ObjectText.setEditable(True)
                self.gSlogin_3.setEnabled(True)
                ObjectText.addItems(CompanName)
            case "WPComp1":
                ObjectText.setEnabled(True)
                ObjectText.setEditable(False)
                self.gSlogin_3.setEnabled(True)
                ObjectText.addItems(CompanName)
            case "TG":
                ObjectText.clear()
                ObjectText.setEnabled(True)
                ObjectText.setEditable(True)
                self.gSlogin_4.setEnabled(True)
                ObjectText.addItems(CompanName)
            case "TGComp":
                ObjectText.setEnabled(True)
                ObjectText.setEditable(False)
                self.gSlogin_4.setEnabled(True)
                ObjectText.addItems(CompanName)
            case _:
                ObjectText.clear()
                ObjectText.setEnabled(False)
                self.gSlogin.setEnabled(False)
                self.gSlogin_2.setEnabled(False)
                self.gSlogin_3.setEnabled(False)
                self.gSlogin_4.setEnabled(False)

    def on_file_open(self, ObjectText: QLineEdit, haveExcel=False):
        if haveExcel:
            file_filter = "Text Files (*.txt);;Excel Files (*.xls *.xlsx)"
        else:
            file_filter = "Text Files (*.txt)"
        path, _ = QFileDialog.getOpenFileName(
            self, "Select file", os.path.dirname(__file__), file_filter
        )
        if path:
            ObjectText.setText(path)

    def ok_clicked(self):
        ppNumber = PhoneParsing()
        self.buttonBox.setEnabled(False)
        self.helper.UpDateOutput("Please Wait, Don't Doing anything...")
        SettingCanSend = self.gsettings.value("can_send")
        SettingCanScrip = self.gsettings.value("can_scrip")
        try:
            self.threads.clear()
            thread = None

            # Telegram
            # =================
            if self.tabTelegram.isVisible():
                match self.tabTelegram.currentIndex():
                    case 0:
                        UseAI = self.useTGAI.isChecked()
                        isCompan = self.useTGCompan.isChecked()
                        comoan_name = self.txtCompName1_2.currentText()
                        send_message = self.textEdit.toPlainText()
                        slogin = self.lineEdit_17.text()
                        slogin_position = self.comboBox_11.currentIndex()
                        message_path = self.lineEdit.text()
                        message_files = self.lineEdit_2.text()
                        message_and_file = self.BothcheckBox.isChecked()
                        categorys = self.comboBox.currentText()
                        ds_from_database = self.radDatabase1.isChecked()
                        ds_from_filelist = self.radFileList1.isChecked()
                        users_datalist = self.lineEdit_3.text()
                        translat = self.chkTranslat.isChecked()

                        if slogin != "":
                            slogin = f"{slogin_position}|{slogin}"
                        if send_message == "":
                            if message_path != "":
                                filetype = self.helper.get_file_type(message_path)
                                if filetype == "text/plain":
                                    send_message = self.helper.read_file_as_text(
                                        message_path
                                    )
                                else:
                                    self._ShowError(
                                        lablel="Error",
                                        Message="Your message file must be [Text File].",
                                    )
                                    return
                            else:
                                if isCompan and comoan_name != "":
                                    send_message = None
                                else:
                                    self._ShowError(
                                        lablel="Error",
                                        Message="You must set a Message for Members",
                                    )
                                    return

                        if ds_from_database:
                            users_datalist = None
                        elif ds_from_filelist:
                            file_type = self.helper.get_file_type(
                                users_datalist.strip()
                            )
                            match file_type:
                                case "text/plain":
                                    users_datalist = self.helper.readlist_file(
                                        users_datalist.strip()
                                    )
                                case "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
                                    ExTable = ET(
                                        self,
                                        database=self.database,
                                        Category=categorys,
                                        Source="telegram",
                                    )
                                    if ExTable.read_excel_file(users_datalist.strip()):
                                        if self.received_data:
                                            users_datalist = [
                                                entry.get("account")
                                                for entry in self.received_data
                                                if str(entry.get("account")).isdigit()
                                                is not None
                                            ]
                                case "application/vnd.ms-excel":
                                    ExTable = ET(
                                        self,
                                        database=self.database,
                                        Category=categorys,
                                        Source="telegram",
                                    )
                                    if ExTable.read_excel_file(users_datalist.strip()):
                                        if self.received_data:
                                            users_datalist = [
                                                entry.get("account")
                                                for entry in self.received_data
                                                if str(entry.get("account")).isdigit()
                                                is not None
                                            ]
                                case _:
                                    QMessageBox.warning(
                                        self,
                                        "File Not Support",
                                        "This File is Not Supported",
                                        QMessageBox.StandardButton.Ok,
                                    )
                                    self.buttonBox.setEnabled(True)
                                    return

                        if (
                            not isinstance(users_datalist, list)
                            and ds_from_database == False
                        ):
                            QMessageBox.warning(
                                self,
                                "Datasource",
                                "There is No List for sending",
                                QMessageBox.StandardButton.Ok,
                            )
                            self.buttonBox.setEnabled(True)
                            return
                        else:
                            users_datalist = None

                        if UseAI:
                            self.SetAI(comoan_name, send_message, "telegram")
                        elif isCompan:
                            UseAI = False
                            send_message = None
                        else:
                            UseAI = False
                            CompanID = ""
                        thread = Worker(
                            "Telegram",
                            SettingCanScrip=SettingCanScrip,
                            SettingCanSend=SettingCanSend,
                            marketing=self.marketing,
                            action=self.tabTelegram.currentIndex(),
                            message=send_message,
                            file_send=message_files,
                            msg_img=message_and_file,
                            file_list=users_datalist,
                            slogin=slogin,
                            category=categorys,
                            compan=comoan_name,
                            translat=translat,
                        )
                    case 1:
                        Member_Category = self.cmdMemCategory2.currentText()
                        group_file_list = self.txtListOfGroup2.text()

                        file_type = self.helper.get_file_type(group_file_list.strip())
                        match file_type:
                            case "text/plain":
                                group_file_list = self.helper.readlist_file(
                                    group_file_list.strip()
                                )
                            case "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
                                ExTable = ET(
                                    self,
                                    database=self.database,
                                    Category=Mem_Categorys,
                                    Source="telegram",
                                )
                                if ExTable.read_excel_file(group_file_list.strip()):
                                    if self.received_data:
                                        group_file_list = [
                                            entry.get("name")
                                            for entry in self.received_data
                                            if str(entry.get("name")) is not None
                                        ]
                            case "application/vnd.ms-excel":
                                ExTable = ET(
                                    self,
                                    database=self.database,
                                    Category=Mem_Categorys,
                                    Source="telegram",
                                )
                                if ExTable.read_excel_file(group_file_list.strip()):
                                    if self.received_data:
                                        group_file_list = [
                                            entry.get("name")
                                            for entry in self.received_data
                                            if str(entry.get("name")) is not None
                                        ]
                            case _:
                                QMessageBox.warning(
                                    self,
                                    "File Not Support",
                                    "This File is Not Supported",
                                    QMessageBox.StandardButton.Ok,
                                )
                                self.buttonBox.setEnabled(True)
                                return

                        if not isinstance(group_file_list, list):
                            QMessageBox.warning(
                                self,
                                "Datasource",
                                "There is No List for sending",
                                QMessageBox.StandardButton.Ok,
                            )
                            self.buttonBox.setEnabled(True)
                            return

                        thread = Worker(
                            "Telegram",
                            SettingCanScrip=SettingCanScrip,
                            SettingCanSend=SettingCanSend,
                            marketing=self.marketing,
                            action=self.tabTelegram.currentIndex(),
                            filelist=group_file_list,
                            category=Member_Category,
                        )
                    case 2:
                        List_From = List_To = []
                        MaxDate = self.dateMax.selectedDate().toString("dd/MM/yyyy")
                        GroupFrom = self.cmbCpyFrom.currentText()
                        ToGroup = self.txtCpyTo.text()
                        if self.rdNew.isChecked():
                            Mood = "new"
                        elif self.rdOld.isChecked():
                            Mood = "old"
                        if ToGroup == "":
                            QMessageBox.warning(
                                self,
                                "Error",
                                "Can't keep your target Empty",
                                QMessageBox.StandardButton.Ok,
                            )
                            return
                        if self.listWFrom.count() > self.listWTo.count():
                            QMessageBox.warning(
                                self,
                                "Replacing",
                                "Can't make From List Bigger than To List",
                                QMessageBox.StandardButton.Ok,
                            )
                            return
                        elif self.listWFrom.count() < self.listWTo.count():
                            QMessageBox.warning(
                                self,
                                "Replacing",
                                "Can't make From List Smaller than To List",
                                QMessageBox.StandardButton.Ok,
                            )
                            return
                        elif self.listWFrom.count() == self.listWTo.count():
                            if self.listWFrom.count() > 0:
                                List_From = [
                                    self.listWFrom.item(i).text()
                                    for i in range(self.listWFrom.count())
                                ]
                            if self.listWTo.count() > 0:
                                List_To = [
                                    self.listWTo.item(i).text()
                                    for i in range(self.listWTo.count())
                                ]
                        thread = Worker(
                            "Telegram",
                            SettingCanScrip=SettingCanScrip,
                            SettingCanSend=SettingCanSend,
                            marketing=self.marketing,
                            action=self.tabTelegram.currentIndex(),
                            main_group=GroupFrom,
                            target_group=ToGroup,
                            max_date=MaxDate,
                            list1=List_From,
                            list2=List_To,
                            mode=Mood,
                        )
                    case 3:
                        AddToGroup = self.txtGroupName4.text()
                        if AddToGroup == "":
                            QMessageBox.warning(
                                self,
                                "Error",
                                "Target can't be empty.",
                                QMessageBox.StandardButton.Ok,
                            )
                            return
                        Category = self.cmdMemCategory4.currentText()
                        group_file_list = self.lineEdit_7.text()
                        getFromDatabase = self.radDatabase4.isChecked()
                        if getFromDatabase == False:
                            file_type = self.helper.get_file_type(
                                group_file_list.strip()
                            )
                            match file_type:
                                case "text/plain":
                                    group_file_list = self.helper.readlist_file(
                                        group_file_list.strip()
                                    )
                                case "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
                                    ExTable = ET(
                                        self,
                                        database=self.database,
                                        Category=Category,
                                        Source="telegram",
                                    )
                                    if ExTable.read_excel_file(group_file_list.strip()):
                                        if self.received_data:
                                            group_file_list = [
                                                entry
                                                for entry in self.received_data
                                                if str(entry.get("account")) is not None
                                            ]
                                case "application/vnd.ms-excel":
                                    ExTable = ET(
                                        self,
                                        database=self.database,
                                        Category=Category,
                                        Source="telegram",
                                    )
                                    if ExTable.read_excel_file(group_file_list.strip()):
                                        if self.received_data:
                                            group_file_list = [
                                                entry
                                                for entry in self.received_data
                                                if str(entry.get("account")) is not None
                                            ]
                                case _:
                                    QMessageBox.warning(
                                        self,
                                        "File Not Support",
                                        "This File is Not Supported",
                                        QMessageBox.StandardButton.Ok,
                                    )
                                    self.buttonBox.setEnabled(True)
                                    return

                            if not isinstance(group_file_list, list):
                                QMessageBox.warning(
                                    self,
                                    "Datasource",
                                    "There is No List for sending",
                                    QMessageBox.StandardButton.Ok,
                                )
                                self.buttonBox.setEnabled(True)
                                return
                        else:
                            group_file_list = None

                        thread = Worker(
                            "Telegram",
                            SettingCanScrip=SettingCanScrip,
                            SettingCanSend=SettingCanSend,
                            marketing=self.marketing,
                            action=self.tabTelegram.currentIndex(),
                            target_group=AddToGroup,
                            category=Category,
                            list_group=group_file_list,
                        )

                thread.progress.connect(self.update_output)
                self.threads.append(thread)

            # WhatsApp
            # =================
            if self.tabWhatsApp.isVisible():
                match self.tabWhatsApp.currentIndex():
                    case 0:  # Tab1
                        UseAI = self.useWPAI_1.isChecked()
                        isCompan = self.useWPCompan_1.isChecked()
                        comoan_name = self.txtWPCompName_1.currentText()
                        send_message = self.textEdit_2.toPlainText()
                        slogin = self.lineEdit_20.text()
                        slogin_position = self.comboBox_12.currentIndex()
                        message_path = self.lineEdit_8.text()
                        message_files = self.lineEdit_10.text()
                        message_and_file = self.chkBoth.isChecked()
                        categorys = self.comboBox_5.currentText()
                        country = self.cmbBCountry.currentText()
                        timezone = self.combTimeZone.currentText()
                        ds_from_database = self.radioButton_5.isChecked()
                        ds_from_filelist = self.radioButton_6.isChecked()
                        users_datalist = self.lineEdit_9.text()

                        if slogin != "":
                            slogin = f"{slogin_position}|{slogin}"
                        if send_message == "":
                            if message_path != "":
                                filetype = self.helper.get_file_type(message_path)
                                if filetype == "text/plain":
                                    send_message = self.helper.read_file_as_text(
                                        message_path
                                    )
                                else:
                                    self._ShowError(
                                        lablel="Error",
                                        Message="Your message file must be [Text File].",
                                    )
                                    return
                            else:
                                if isCompan:
                                    # Get Messages from Database
                                    send_message = None
                                else:
                                    self._ShowError(
                                        lablel="Error",
                                        Message="You must set a Message for Members",
                                    )
                                    return
                        if message_and_file:
                            message_files = f"msg:{message_files}"

                        if ds_from_database:
                            users_datalist = None
                        elif ds_from_filelist:
                            file_type = self.helper.get_file_type(
                                users_datalist.strip()
                            )
                            match file_type:
                                case "text/plain":
                                    users_datalist = self.helper.readlist_file(
                                        users_datalist.strip()
                                    )
                                case "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
                                    ExTable = ET(
                                        self,
                                        database=self.database,
                                        Category=categorys,
                                        Source="whatsapp",
                                    )
                                    if ExTable.read_excel_file(users_datalist.strip()):
                                        if self.received_data:
                                            users_datalist = [
                                                ppNumber.clean_phone_number(
                                                    entry.get("number")
                                                )
                                                for entry in self.received_data
                                                if ppNumber.clean_phone_number(
                                                    entry.get("number")
                                                )
                                                is not None
                                            ]
                                            users_datalist = [
                                                phone
                                                for phone in users_datalist
                                                if phone is not None
                                            ]
                                case "application/vnd.ms-excel":
                                    ExTable = ET(
                                        self,
                                        database=self.database,
                                        Category=categorys,
                                        Source="whatsapp",
                                    )
                                    if ExTable.read_excel_file(users_datalist.strip()):
                                        if self.received_data:
                                            users_datalist = [
                                                ppNumber.clean_phone_number(
                                                    entry.get("number")
                                                )
                                                for entry in self.received_data
                                                if ppNumber.clean_phone_number(
                                                    entry.get("number")
                                                )
                                                is not None
                                            ]
                                            users_datalist = [
                                                phone
                                                for phone in users_datalist
                                                if phone is not None
                                            ]
                                case _:
                                    QMessageBox.warning(
                                        self,
                                        "File Not Support",
                                        "This File is Not Supported",
                                        QMessageBox.StandardButton.Ok,
                                    )
                                    self.buttonBox.setEnabled(True)
                                    return

                        if not isinstance(users_datalist, list):
                            QMessageBox.warning(
                                self,
                                "Datasource",
                                "There is No List for sending",
                                QMessageBox.StandardButton.Ok,
                            )
                            self.buttonBox.setEnabled(True)
                            return

                        if UseAI:
                            self.SetAI(comoan_name, send_message, "whatsapp")
                        elif isCompan:
                            UseAI = False
                            send_message = None
                        else:
                            UseAI = False
                            CompanID = ""
                        thread = Worker(
                            "WhatsApp",
                            SettingCanScrip=SettingCanScrip,
                            SettingCanSend=SettingCanSend,
                            marketing=self.marketing,
                            action=self.tabWhatsApp.currentIndex(),
                            message=send_message,
                            slogin=slogin,
                            category=categorys,
                            file_send=message_files,
                            country=country,
                            timezone=timezone,
                            list_file=users_datalist,
                            compan=comoan_name,
                            translation=self.ckTranslat.isChecked(),
                        )
                    case 1:  # Tab2
                        Category = self.comContactCategory.currentText()
                        thread = Worker(
                            "WhatsApp",
                            SettingCanScrip=SettingCanScrip,
                            SettingCanSend=SettingCanSend,
                            marketing=self.marketing,
                            action=self.tabWhatsApp.currentIndex(),
                            Category=Category,
                        )
                    case 2:  # Tab3
                        Group_Category = self.comboBox_6.currentText()
                        if self.lineEdit_11.text() != "":
                            groupname = self.lineEdit_11.text()
                            file_type = self.helper.get_file_type(groupname.strip())
                            match file_type:
                                case "text/plain":
                                    Group_Name = self.helper.readlist_file(
                                        users_datalist.strip()
                                    )
                                case "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
                                    ExTable = ET(
                                        self,
                                        database=self.database,
                                        Category=Group_Category,
                                        Source="whatsapp",
                                    )
                                    if ExTable.read_excel_file(users_datalist.strip()):
                                        if self.received_data:
                                            users_datalist = [
                                                str(entry.get("name")).strip()
                                                for entry in self.received_data
                                                if str(entry.get("name")).strip()
                                                is not None
                                            ]
                                            Group_Name = [
                                                gName
                                                for gName in users_datalist
                                                if gName is not None
                                            ]
                                case "application/vnd.ms-excel":
                                    ExTable = ET(
                                        self,
                                        database=self.database,
                                        Category=Group_Category,
                                        Source="whatsapp",
                                    )
                                    if ExTable.read_excel_file(users_datalist.strip()):
                                        if self.received_data:
                                            users_datalist = [
                                                str(entry.get("name")).strip()
                                                for entry in self.received_data
                                                if str(entry.get("name")).strip()
                                                is not None
                                            ]
                                            Group_Name = [
                                                gName
                                                for gName in users_datalist
                                                if gName is not None
                                            ]

                                case _:
                                    QMessageBox.warning(
                                        self,
                                        "File Not Support",
                                        "This File is Not Supported",
                                        QMessageBox.StandardButton.Ok,
                                    )
                                    self.buttonBox.setEnabled(True)
                                    return
                        else:
                            Group_Name = self.lineEdit_12.text()

                        thread = Worker(
                            "WhatsApp",
                            SettingCanScrip=SettingCanScrip,
                            SettingCanSend=SettingCanSend,
                            marketing=self.marketing,
                            action=self.tabWhatsApp.currentIndex(),
                            Group_Name=Group_Name,
                            Group_Category=Group_Category,
                        )
                thread.progress.connect(self.update_output)
                self.threads.append(thread)

            # Facebook
            # =================
            if self.tabFacebook.isVisible():
                match self.tabFacebook.currentIndex():
                    case 0:
                        # Tab1
                        Mem_Message = self.textEdit_3.toPlainText()
                        if Mem_Message == "":
                            Mem_Message = self.helper.read_file_as_text(
                                self.lineEdit_14.text()
                            )
                        if Mem_Message == "":
                            if self.useCompan_1.isChecked() == False:
                                self._ShowError(
                                    lablel="Error",
                                    Message="You must set a Message for Members",
                                )
                                return
                            else:
                                if self.lineEdit_15.text() == "":
                                    Mem_Message = None
                                else:
                                    Mem_Image = self.lineEdit_15.text()

                        if self.lineEdit_5.text() != "":
                            Mem_Slogin = f"{self.comboBox_3.currentIndex()}|{self.lineEdit_5.text()}"
                        else:
                            Mem_Slogin = None

                        if self.useFPAI_1.isChecked():
                            UseAI = True
                            CompanID = self.txtCompName1.currentText()
                            self.SetAI(CompanID, Mem_Message, "facebook")
                        elif self.useCompan_1.isChecked():
                            UseAI = False
                            CompanID = self.txtCompName1.currentText()
                        else:
                            UseAI = False
                            CompanID = ""

                        Mem_FilePath = self.lineEdit_15.text()
                        Mem_Categorys = self.comboBox_7.currentText()
                        thread = Worker(
                            "Facebook",
                            marketing=self.marketing,
                            SettingCanScrip=SettingCanScrip,
                            SettingCanSend=SettingCanSend,
                            action=self.tabFacebook.currentIndex(),
                            Mem_Message=Mem_Message,
                            Mem_FilePath=Mem_FilePath,
                            Mem_Categorys=Mem_Categorys,
                            Mem_AI=UseAI,
                            CompanName=CompanID,
                            Mem_Slogin=Mem_Slogin,
                        )
                    case 1:
                        # Tab2
                        Group_Message = self.textEdit_4.toPlainText()
                        if Group_Message == "":
                            Group_Message = self.helper.read_file_as_text(
                                self.lineEdit_16.text()
                            )
                            if Group_Message == "":
                                if self.useCompan_2.isChecked() == False:
                                    self._ShowError(
                                        lablel="Error",
                                        Message="You must set a Message for Groups",
                                    )
                                    return
                                else:
                                    if self.lineEdit_19.text() == "":
                                        Group_Message = None
                                    else:
                                        Group_Image = self.lineEdit_19.text()

                        if self.lineEdit_13.text() != "":
                            Group_Slogin = f"{self.comboBox_10.currentIndex()}|{self.lineEdit_13.text()}"
                        else:
                            Group_Slogin = None
                        if self.useFPAI_2.isChecked():
                            Group_AI = True
                            CompanID = self.txtCompName2.currentText()
                            self.SetAI(CompanID, Group_Message, "facebook")
                        elif self.useCompan_2.isChecked():
                            Group_AI = False
                            CompanID = self.txtCompName2.currentText()
                        else:
                            Group_AI = False
                            CompanID = ""

                        Group_Category = self.comboBox_8.currentText()
                        Group_FileGroupPath = None
                        if self.radioButton_12.isChecked():
                            Group_FileGroupPath = self.lineEdit_4.text()
                            if Group_FileGroupPath == "":
                                self._ShowError(
                                    lablel="Error",
                                    Message="You must set a List for Source Groups",
                                )
                                return
                            else:
                                file_type = self.helper.get_file_type(
                                    Group_FileGroupPath.strip()
                                )
                                match file_type:
                                    case "text/plain":
                                        Group_FileGroupPath = self.helper.readlist_file(
                                            Group_FileGroupPath.strip()
                                        )
                                    case "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
                                        ExTable = ET(
                                            self,
                                            database=self.database,
                                            Category=Group_Category,
                                            Source="facebook",
                                        )
                                        if ExTable.read_excel_file(
                                            Group_FileGroupPath.strip()
                                        ):
                                            if self.received_data:
                                                Group_FileGroupPath = [
                                                    entry
                                                    for entry in self.received_data
                                                ]
                                    case "application/vnd.ms-excel":
                                        ExTable = ET(
                                            self,
                                            database=self.database,
                                            Category=Group_Category,
                                            Source="facebook",
                                        )
                                        if ExTable.read_excel_file(
                                            Group_FileGroupPath.strip()
                                        ):
                                            if self.received_data:
                                                Group_FileGroupPath = [
                                                    entry
                                                    for entry in self.received_data
                                                ]
                                    case _:
                                        QMessageBox.warning(
                                            self,
                                            "File Not Support",
                                            "This File is Not Supported",
                                            QMessageBox.OK,
                                        )
                                        return
                        thread = Worker(
                            "Facebook",
                            marketing=self.marketing,
                            SettingCanScrip=SettingCanScrip,
                            SettingCanSend=SettingCanSend,
                            action=self.tabFacebook.currentIndex(),
                            Group_Message=Group_Message,
                            Group_Category=Group_Category,
                            Group_FileGroupPath=Group_FileGroupPath,
                            Group_AI=Group_AI,
                            CompanName=CompanID,
                            Group_Slogin=Group_Slogin,
                        )
                    case 2:
                        Group_Name = self.comboBox_2.currentText() or ""
                        if Group_Name != "":
                            if not Group_Name.isdigit():
                                _GroupName = self.database.search_by_column(
                                    "facebook_groups", "group_name", Group_Name
                                )[0]
                                if _GroupName:
                                    Group_Name = _GroupName["group_id"]
                        Member_Category = self.comboBox_9.currentText()
                        if self.radioButton_14.isChecked():
                            List_Group_Name = self.lineEdit_18.text()
                            if List_Group_Name == "":
                                self._ShowError(
                                    lablel="Error",
                                    Message="You must select Source of Group or keep it in Database",
                                )
                                return
                            else:
                                file_type = self.helper.get_file_type(
                                    List_Group_Name.strip()
                                )
                                match file_type:
                                    case "text/plain":
                                        List_Group_Name = self.helper.readlist_file(
                                            List_Group_Name.strip()
                                        )
                                    case "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
                                        ExTable = ET(
                                            self,
                                            database=self.database,
                                            Category=Member_Category,
                                            Source="facebook",
                                        )
                                        if ExTable.read_excel_file(
                                            List_Group_Name.strip()
                                        ):
                                            if self.received_data:
                                                List_Group_Name = [
                                                    entry
                                                    for entry in self.received_data
                                                ]
                                    case "application/vnd.ms-excel":
                                        ExTable = ET(
                                            self,
                                            database=self.database,
                                            Category=Member_Category,
                                            Source="facebook",
                                        )
                                        if ExTable.read_excel_file(
                                            List_Group_Name.strip()
                                        ):
                                            if self.received_data:
                                                List_Group_Name = [
                                                    entry
                                                    for entry in self.received_data
                                                ]
                                    case _:
                                        QMessageBox.warning(
                                            self,
                                            "File Not Support",
                                            "This File is Not Supported",
                                            QMessageBox.OK,
                                        )
                                        return
                                Group_Name = List_Group_Name

                        thread = Worker(
                            "Facebook",
                            marketing=self.marketing,
                            SettingCanScrip=SettingCanScrip,
                            SettingCanSend=SettingCanSend,
                            action=self.tabFacebook.currentIndex(),
                            Group_Name=Group_Name,
                            Member_Category=Member_Category,
                        )

                thread.progress.connect(self.update_output)
                self.threads.append(thread)

            for thread in self.threads:
                thread.start()

            self.buttonBox.setEnabled(True)
            self.accept()
        except Exception as e:
            print(e)
            logging.error(traceback.format_exc())
            self._ShowError(
                lablel="Error",
                Message="There is Error , Please re-Check all your inputs",
            )
            self.buttonBox.setEnabled(True)

    def SetAI(self, CompanName, message, Source):
        self.Source = Source
        self.CompanName = CompanName
        self.Compan_ID = str(uuid.uuid4())
        self.helper.UpDateOutput(f"Compan ID {self.CompanName} ({self.Compan_ID})")
        self.helper.UpDateOutput("Run AI...")
        self.setWindowTitle("Please Wait , AI is Working Now")
        self.progress = QProgressDialog(
            "AI Analysis your Message", "Cancel", 0, 0, self.parent
        )
        self.progress.setWindowTitle("Please Wait")
        self.progress.setModal(True)
        self.progress.setCancelButton(None)
        self.progress.show()
        self.run_ai_thread(message)

    def on_ai_finished(self, result):
        self.progress.close()

        if result.result:
            window = AI_Window(
                parent=self,
                command=result.result,
                CompanName=self.CompanName,
                Compan_ID=self.Compan_ID,
                Source=self.Source,
                Database=self.database,
            )
            window.exec()

    def run_ai_thread(self, command):
        if command:
            self.worker = AiWorker(command, self.output)
            self.worker.finished.connect(self.on_ai_finished)
            self.worker.start()

    def getExceData(self):
        file_filter = "Excel Files (*.xls *.xlsx)"
        path, _ = QFileDialog.getOpenFileName(
            self, "Select file", os.path.dirname(__file__), file_filter
        )
        if path:
            users_datalist = path
            file_name = path.split("/")[-1]
        select_category = self.comContactCategory.currentText()
        print(select_category)
        ExTable = ET(self, self.database)
        if ExTable.read_excel_file(users_datalist.strip()):
            DataItem = []
            if self.received_data:
                users_datalist = [
                    str(entry).strip()
                    for entry in self.received_data
                    if str(entry).strip() is not None
                ]
                DataItem = [gName for gName in users_datalist if gName is not None]
            for phone_number in DataItem:
                if not self.database.search_by_column(
                    "phone_numbers", "number", phone_number.get("number")
                ):
                    ContryPhone = PhoneParsing().get_phone_number_and_get_country(
                        phone_number.get("number")
                    )
                    TimeZone = PhoneParsing().get_time_zone_from_number(phone_number)
                    DataSave = {
                        "number": phone_number.get("number"),
                        "country": ContryPhone,
                        "timezone": TimeZone,
                        "category": select_category,
                        "group_name": file_name,
                    }
                    DataSave.update(phone_number)
                    self.database.write_to_database("phone_numbers", DataSave)
                self.helper.UpDateOutput(
                    f"Add {phone_number.get('number')} from {ContryPhone} to your Database"
                )

    def _ShowError(self, lablel: str = None, Message: str = None):
        dlg = QMessageBox(self)
        if lablel is None:
            dlg.setWindowTitle("There is Error!")
        else:
            dlg.setWindowTitle(lablel)

        dlg.setText(Message)
        dlg.setStandardButtons(QMessageBox.Ok)
        dlg.setIcon(QMessageBox.Critical)
        button = dlg.exec()
        if button == QMessageBox.Ok:
            self.buttonBox.setEnabled(True)
            dlg.close()
            return True

    def update_output(self, message: str, update: bool):
        self.progress_signal.emit(message, update)
