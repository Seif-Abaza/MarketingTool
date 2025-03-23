from datetime import datetime

import requests
from smsactivate.api import SMSActivateAPI


class SMSServices:
    TABLE_NAME = "sms_user_service"
    APIKEY = "bd3c71fed30f5453Ac6421e78Ae4ff10"

    def __init__(self, settings=None, database=None, server_url=None):
        self.settings = settings
        self.ServicesData = None
        api_key = self.settings.value("sms_key")
        self.server_url = server_url
        if not api_key is None:
            self.SMS = SMSActivateAPI(api_key)
        else:
            self.SMS = SMSActivateAPI(self.APIKEY)

        self.CountrysInfo = self.SMS.getCountries()
        Server_Url = f"{self.server_url}/get_sms_services"
        response = requests.get(Server_Url)
        if response.status_code == 200:
            self.ServicesData = response.json().get("data")

        if not database is None:
            self.database = database
            self.database.create_table(self.TABLE_NAME)

    def get_services_allow_from_server(self):
        Server_Url = f"{self.server_url}/get_sms_name_by_code"
        data_name = []
        if self.ServicesData:
            for item in self.ServicesData:
                data_name.append(item["name"])
            exception_for_user = self.settings.value("can_sms_service")
            existing_codes = {item["code"] for item in self.ServicesData}
            for code in exception_for_user:
                if code not in existing_codes:
                    response = requests.get(f"{Server_Url}/{code}")
                    if response.status_code == 200:
                        item_name = response.json().get("data")
                        self.ServicesData.append({"code": code, "name": item_name})
                        data_name.append(item_name)
        return data_name

    def get_service_code(self, Service_Name: str):
        if Service_Name:
            for item in self.ServicesData:
                if item["name"] == Service_Name:
                    return item["code"]
        return None

    def send_top_country_for_service(self, ServiceName: str) -> list:
        ListOfService = []
        if ServiceName:
            TopServiec = self.SMS.getTopCountriesByService(
                self.get_service_code(ServiceName)
            )
            for item in TopServiec:
                NumberOfServif = TopServiec[item]["count"] - 1
                if NumberOfServif > 0:
                    ListOfService.append(
                        {
                            "country_code": TopServiec[item]["country"],
                            "country_name": self.CountrysInfo[
                                str(TopServiec[item]["country"])
                            ]["eng"],
                            "number": NumberOfServif,
                        }
                    )
        return ListOfService

    def set_service_order(self, ServiceCode, CountryNumber):
        number = self.SMS.getNumberV2(service=ServiceCode, country=CountryNumber)
        DataToDB = {
            "id": number["activationId"],
            "phone": f"+{number['phoneNumber']}",
            "cost": number["activationCost"],
            "start": number["activationTime"],
            "end": number["activationEndTime"],
            "provider": number["activationOperator"],
            "code": "",
            "text": "",
        }
        self.database.write_to_database(self.TABLE_NAME, DataToDB)
        return DataToDB["phone"]

    def get_service_order(self, phone_number):
        DateNow = str(datetime.today().strftime("%d/%m/%Y"))
        DataFromDB = self.database.read_from_database(
            self.TABLE_NAME, {"code": "", "phone": phone_number}
        )
        if DataFromDB:
            record = DataFromDB[0]
            date_format1 = "%Y-%m-%d %H:%M:%S"
            date_format2 = "%d/%m/%Y"
            if record["end"]:
                date1 = datetime.strptime(record["end"], date_format1)
                date2 = datetime.strptime(DateNow, date_format2)
                if date1 > date2:
                    self.SMS.setStatus(id=record["id"], status=8)
                    return "Expired Date"

            activations = self.SMS.getActiveActivations()
            if activations["status"] == "success":
                activations = activations["activeActivations"][0]
                DataToDB = {
                    "service_code": activations["serviceCode"],
                    "country": activations["countryName"],
                    "phone": f"+{activations['phoneNumber']}",
                    "cost": activations["activationCost"],
                    "start": activations["activationTime"],
                    "end": activations["activationEndTime"],
                    "provider": activations["activationOperator"],
                    "code": activations["smsCode"],
                    "text": activations["smsText"],
                }
                self.database.update_in_database(
                    self.TABLE_NAME, {"id": record["id"]}, DataToDB
                )
                if int(activations["smsCode"]) > 0:
                    return int(activations["smsCode"])
                else:
                    return False

    def checkup_old_order(self):
        activations = self.SMS.getActiveActivations()
        if activations["status"] == "success":
            for activat in activations["activeActivations"]:
                if activat["smsCode"] is None:
                    return f"+{activat['phoneNumber']}:{None}"
                else:
                    return f"+{activat['phoneNumber']}:{activat['smsCode']}"
        return None

    def CancelOrder(self, phone_number):
        try:
            DataFromDB = self.database.read_from_database(
                self.TABLE_NAME, {"code": "", "phone": phone_number}
            )
            if DataFromDB[0]:
                DataFromDB = DataFromDB[0]
                order_id = DataFromDB["id"]
                if self.SMS.setStatus(id=order_id, status=8):
                    return True
                else:
                    return False
            else:
                return True
        except Exception as e:
            return False

    def FinishedOrder(self, phone_number):
        try:
            DataFromDB = self.database.read_from_database(
                self.TABLE_NAME, {"code": "", "phone": phone_number}
            )
            if DataFromDB[0]:
                DataFromDB = DataFromDB[0]
                order_id = DataFromDB["id"]
                if self.SMS.setStatus(id=order_id, status=6):
                    return True
                else:
                    return False
            else:
                return True
        except Exception as e:
            return False
