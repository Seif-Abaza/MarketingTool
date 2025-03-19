from datetime import datetime
import phonenumbers
import pytz
from phonenumbers import geocoder, timezone, carrier
import re
import json
from langcodes import *

class PhoneParsing:

    def __init__(self):
        pass

    def get_country(self,phone):
        try:
            parsed_number = phonenumbers.parse(phone, None)
            return geocoder.description_for_number(parsed_number, "en")  # إرجاع اسم الدولة بالإنجليزية
        except:
            return "Unknown"

    def get_number_from_text(self,text:str, get_regon=None):
        list_of_phone = dict()
        thislist = []
        for match in phonenumbers.PhoneNumberMatcher(text, get_regon):
            if phonenumbers.is_valid_number(phonenumbers.parse(phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.E164), None)):
                numberis = phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.E164)
                objNum = phonenumbers.parse(numberis, get_regon)
                list_of_phone = {
                    "number": numberis,
                    "country": geocoder.country_name_for_number(objNum, lang='en')
                }
                thislist.append(list_of_phone)
        return thislist or None
    
    def clean_phone_number(self,PhoneNumber):
        try:
            OrgNumber = PhoneNumber
            if PhoneNumber is None or PhoneNumber == '' or len(PhoneNumber) < 10:
                return None
            
            pattern = r"(?:\+?(\d{1,3})[-. ]?)?(?:\(?(\d{2,4})\)?[-. ]?)?(\d{3,4})[-. ]?(\d{3,4})"
            matches = re.findall(pattern, PhoneNumber)
            PhoneNumber = ["".join(match) for match in matches if any(match)]
            
            PhoneNumber = ''.join(filter(lambda x: x.isdigit() or x == "+", PhoneNumber))
            
            if not PhoneNumber.startswith('0'):
                PhoneNumber = f"0{PhoneNumber[1:]}"
            if PhoneNumber.startswith('00'):
                PhoneNumber = f"+{PhoneNumber[2:]}"
                
            if PhoneNumber[0] == 0 and PhoneNumber[1] != 0:
                PhoneNumber = f"+{PhoneNumber[1:]}"
            if len(PhoneNumber) >= 10:
                Informations = self.get_phone_info(PhoneNumber)
                if not Informations is None:
                    regon = Informations['Region'].lower()
                    parsed_number = phonenumbers.parse(PhoneNumber, regon)
                else:
                    parsed_number = phonenumbers.parse(PhoneNumber, None)
                if phonenumbers.is_valid_number(parsed_number):
                    return phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)
        except phonenumbers.NumberParseException as e:
            PhoneNumber = OrgNumber
            pattern = r"(?:\+?(\d{1,3})[-. ]?)?(?:\(?(\d{2,4})\)?[-. ]?)?(\d{3,4})[-. ]?(\d{3,4})"
            matches = re.findall(pattern, PhoneNumber)
            PhoneNumber = ["".join(match) for match in matches if any(match)]
            if len(PhoneNumber) > 0:
                PhoneNumber = PhoneNumber[0]
                if len(PhoneNumber) > 10:
                    if not PhoneNumber.startswith('0'):
                        PhoneNumber = f"0{PhoneNumber[1:]}"
                    if PhoneNumber.startswith('00'):
                        PhoneNumber = f"+{PhoneNumber[2:]}"
                    if PhoneNumber[0] == 0 and PhoneNumber[1] != 0:
                        PhoneNumber = f"+{PhoneNumber[1:]}"
                    return PhoneNumber
        return None  # إذا لم يكن الرقم صحيحًا
        
    def get_phone_number_and_get_country(self, phone_number):
        phoneNumber = phonenumbers.parse(phone_number,None)
        country = geocoder.country_name_for_number(phoneNumber, lang='en')
        return country

    def get_time_zone_from_number(self, phone_number):
        phoneNumber = phonenumbers.parse(phone_number)
        timeZone = timezone.time_zones_for_number(phoneNumber)
        return timeZone[0]

    def get_time_from_number(self, phone_number):
        timezone = self.get_time_zone_from_number(phone_number)
        newYorkTz = pytz.timezone(timezone) 
        timeInNewYork = datetime.now(newYorkTz)
        currentTimeInNewYork = timeInNewYork.strftime("%I:%M:%S %p")
        return currentTimeInNewYork

    def find_country_languages(self,query):
        json_data = '../Resource/countries.json'
        with open(json_data, "r", encoding="utf-8") as file:
            countries = json.load(file)
        query = query.strip().lower()
        if query.upper() in countries:
            return countries[query.upper()].get("languages", {})
        for country_code, data in countries.items():
            name = data.get("name", {})
            if query in [name.get("common", "").lower(), name.get("official", "").lower()]:
                return data.get("languages", {})
        return None
    
    def get_information_from_phone(self,PhoneNumber):
        parsed_number = phonenumbers.parse(PhoneNumber, None)
        country_name = geocoder.description_for_number(parsed_number, "en")
        country_code = phonenumbers.region_code_for_number(parsed_number)
        primary_language = self.find_country_languages(str(country_name))
        return {
            "Country": country_name,
            "Region": country_code,
            "Language": list(primary_language.values()),
        }