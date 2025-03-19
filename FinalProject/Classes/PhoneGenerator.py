import os
import sys
import threading
import time

from PySide6.QtWidgets import QDialog, QMessageBox

from Interface.generate_phone_ui import Ui_Dialog as PhoneGeneratorDialog
from utils.SMSServices import SMSServices

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class PhoneGenerator(PhoneGeneratorDialog, QDialog):

    def __init__(self, parent=None, database=None, settings=None,server_url=None):
        super().__init__(parent)
        self.setupUi(self)
        self.database = database
        self.settings = settings
        self.CountryList = []
        self.buttonBox.accepted.connect(self.finished_service)
        self.buttonBox.rejected.connect(self.cancel_services)
        self.sms = SMSServices(settings=settings, database=database, server_url=server_url)
        self.comboBox_2.addItems(self.sms.get_services_allow_from_server())
        self.comboBox.setEnabled(False)
        self.label_6.setVisible(False)
        self.label.setVisible(False)
        Old = self.sms.checkup_old_order()
        if Old is None:
            self.comboBox_2.activated.connect(self.on_change_service)
            self.comboBox.activated.connect(self.confirmation_make_order)
        else:
            OldData = Old.split(":")
            self.comboBox_2.setEnabled(False)
            self.comboBox.setEnabled(False)
            self.label_5.setText(OldData[0])
            if OldData[1] == "None":
                self.label.setText("SMS Code : 000000")
                self.label.setVisible(False)
                thread = threading.Thread(
                    target=self.CheckUpCode, name="CheckUpCode", daemon=True
                )
                thread.start()
            else:
                OldText = self.label.text().split(":")
                OldText[1] = OldData[1]
                self.label.setText(":".join(map(str, OldText)))
                self.label.setVisible(True)

    def cancel_services(self):
        if self.sms.CancelOrder(self.label_5.text()):
            self.reject
        else:
            QMessageBox.critical(self, "Error", "Can't Cancel This Order")

    def finished_service(self):
        if self.sms.FinishedOrder(self.label_5.text()):
            self.accept()
        else:
            QMessageBox.critical(self, "Error", "Can't Finished This Order")

    def on_change_service(self):
        self.CountryList = []
        Service_Name = self.comboBox_2.currentText()
        ListService = self.sms.send_top_country_for_service(Service_Name)
        if len(ListService) > 0:
            ComboList = []
            for providers in ListService:
                self.CountryList.append(
                    {
                        "name": providers["country_name"],
                        "code": providers["country_code"],
                    }
                )
                ComboList.append(
                    f"{providers['country_name']} have ({providers['number']}) numbers"
                )

            self.comboBox.setEnabled(True)
            self.comboBox.clear()
            self.comboBox.addItems(ComboList)
        # print(ListService)

    def confirmation_make_order(self):
        Service = self.comboBox_2.currentText()
        Country = self.comboBox.currentText().split(" ")[0]
        country_dict = {item["name"]: item["code"] for item in self.CountryList}
        code = country_dict.get(Country, "Not Found")
        scode = self.sms.get_service_code(Service)
        if code != "Not Found":
            replay = QMessageBox.question(
                self,
                "Confirmation",
                f"Are you sure you want {Service} from {Country} ?",
                QMessageBox.Yes | QMessageBox.No,
            )
            if replay == QMessageBox.Yes:
                result = self.sms.set_service_order(
                    ServiceCode=scode, CountryNumber=code
                )
                self.label_5.setText("")
                self.label_5.setText(result)
                thread = threading.Thread(
                    target=self.CheckUpCode, name="CheckUpCode", daemon=True
                )
                thread.start()
            else:
                self.label_5.setText("+000-0000000")

    def CheckUpCode(self):
        while True:
            print("Waiting Code...")
            Code = self.sms.get_service_order(self.label_5.text())
            if Code:
                if Code == "Expired Date":
                    self.comboBox_2.addItems(self.sms.get_services_allow_from_server())
                    self.comboBox.setEnabled(False)
                    self.label_6.setVisible(False)
                    self.label.setVisible(False)
                    break
                else:
                    OldText = self.label.text().split(":")
                    OldText[1] = Code
                    self.label.setText(":".join(map(str, OldText)))
                    self.label.setVisible(True)
                    break
            else:
                time.sleep(10)
