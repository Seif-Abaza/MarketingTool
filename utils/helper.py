import io
import json
import random
import string
from PySide6.QtWidgets import QListView, QDialog
from PySide6.QtCore import QStringListModel, QThread, Signal
import configparser
import qrcode
from PIL import Image
from pyqrcode import QRCode
import re
from datetime import datetime, timedelta
import os
from bs4 import BeautifulSoup
import time
import pyperclip
import logging
from langdetect import detect
from playwright.sync_api import sync_playwright
import traceback
from Interface.ai_interface_ui import Ui_Dialog as AI_Dialog
import magic


class helper:
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    tens = [
        "",
        "ten",
        "twenty",
        "thirty",
        "forty",
        "fifty",
        "sixty",
        "seventy",
        "eighty",
        "ninety",
    ]
    teens = [
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
    ]
    scales = [
        "",
        "thousand",
        "million",
        "billion",
        "trillion",
        "quadrillion",
        "quintillion",
        "sextillion",
        "septillion",
        "octillion",
        "nonillion",
        "decillion",
    ]

    TELEGRAM_WEB = "https://web.telegram.org"
    WHATSAPP_WEB = "https://web.whatsapp.com"
    FACEBOOK_WEB = "https://facebook.com"
    CHROME_USER_DATA = "./Sessions"

    def __init__(self, output: QListView = None):
        self.Output_Item = output
        global helper_model
        if not output is None:
            self.model = QStringListModel()
            self.OutItem = []
            self.Output_Item.setModel(self.model)
            helper_model = self.model

    def get_file_type(self, file_path):
        mime = magic.Magic(mime=True)  # تحديد النوع بناءً على MIME type
        file_type = mime.from_file(file_path)
        return file_type

    def UpDateOutput(self, String: str):
        String = String.strip()
        if String:
            self.OutItem.append(String)
            self.model.setStringList(self.OutItem)
            helper_model = self.model

    def get_helper_model(self):
        return helper_model

    def number_to_words(self, num):
        if num == 0:
            return "zero"

        # Split the number into groups of three digits
        num_str = str(num)
        groups = []
        while num_str:
            groups.append(int(num_str[-3:]))
            num_str = num_str[:-3]

        words = []
        for i, group in enumerate(groups):
            if group != 0:
                group_words = []

                # Convert hundreds place
                hundreds = group // 100
                if hundreds > 0:
                    group_words.append(self.ones[hundreds] + " hundred")

                # Convert tens and ones places
                tens_ones = group % 100
                if tens_ones >= 10 and tens_ones <= 19:
                    group_words.append(self.teens[tens_ones - 10])
                else:
                    tens_digit = self.tens[tens_ones // 10]
                    ones_digit = self.ones[tens_ones % 10]
                    if tens_digit:
                        group_words.append(tens_digit)
                    if ones_digit:
                        group_words.append(ones_digit)

                # Add scale word
                if i > 0:
                    group_words.append(self.scales[i])
                words.extend(reversed(group_words))
        return " ".join(reversed(words))

    def is_file_path(self, str_path: str = None):
        if str_path is None:
            return False
        pattern = r"^([a-zA-Z]:)?([/\\][^/\\]+)+[/\\]?$|^\.{1,2}[/\\]"
        return bool(re.match(pattern, str_path))

    def readlist_file(self, filename):
        """Reads a file line by line and returns a list of lines."""
        try:
            if os.path.exists(filename):
                with open(filename, "r", encoding="utf-8") as file:
                    lines = file.readlines()  # Read all lines into a list
                return [line.strip() for line in lines]  # Remove newline characters
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
            return []

    def writelist_file(self, filename, datalist):
        with open(filename + ".json", "a", encoding="utf-8") as f:
            json.dump(datalist, f, ensure_ascii=False, indent=4)
            return True
        return False

    def read_file_as_text(self, filepath):
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as file:
                return file.read()
            return ""
        else:
            return ""

    def convert_text_to_html(self, input_file):
        with open(input_file, "r", encoding="utf-8") as file:
            lines = file.readlines()

        html_output = ""
        for line in lines:
            line = line.strip()  # Remove extra spaces or newlines
            if line:  # Ignore empty lines
                html_output += f'<span data-lexical-text="true">{line}</span>\n<br>\n'

        return html_output

    def id_generator(self, size=6, chars=string.ascii_uppercase + string.digits):
        return "".join(random.choice(chars) for _ in range(size))

    def image_to_ascii(self, image_data, new_width=50):
        """Convert image bytes to ASCII art"""
        try:
            img = Image.open(io.BytesIO(image_data))
            width, height = img.size
            aspect_ratio = height / width
            new_height = int(aspect_ratio * new_width * 0.55)
            img = img.resize((new_width, new_height))
            img = img.convert("L")  # Convert to grayscale

            pixels = img.getdata()
            ascii_chars = ["⚫", "⚫", "⚫", "⚫", "⚫", "⚪", "⚪", "⚪", "⚪", "⚪"]
            ascii_str = "".join(
                [
                    ascii_chars[min(pixel // 25, len(ascii_chars) - 1)]
                    for pixel in pixels
                ]
            )

            return "\n".join(
                [
                    ascii_str[i : i + new_width]
                    for i in range(0, len(ascii_str), new_width)
                ]
            )
        except Exception as e:
            print(f"Error converting image: {str(e)}")
            return None

    def generate_terminal_qr(self, url):
        qr = qrcode.QRCode()
        qr.add_data(url)
        qr.print_ascii()

    def convert_to_datetime(self, time_str):
        now = datetime.now()
        days_map = {
            "Monday": 0,
            "Tuesday": 1,
            "Wednesday": 2,
            "Thursday": 3,
            "Friday": 4,
            "Saturday": 5,
            "Sunday": 6,
        }
        parts = time_str.split()
        if parts[1].isdigit():
            value, unit = int(parts[1]), parts[2]
            # تحديد مقدار الوقت المنقضي
            if "minute" in unit:
                delta = timedelta(minutes=value)
            elif "hour" in unit:
                delta = timedelta(hours=value)
            elif "day" in unit:
                delta = timedelta(days=value)
            elif "week" in unit:
                delta = timedelta(weeks=value)
            elif "month" in unit:
                delta = timedelta(days=value * 30)  # تقريبًا
            elif "year" in unit:
                delta = timedelta(days=value * 365)  # تقريبًا
            else:
                return "Format not supported"

            joined_time = now - delta
            return joined_time.strftime("%Y-%m-%d %H:%M:%S")
        else:
            today = datetime.today()
            # Extract day from string
            words = time_str.split()
            if "Today" in words:
                return today.strftime("%Y-%m-%d")  # Return today's date

            for word in words:
                if word in days_map:  # Check if the word is a weekday
                    target_day = days_map[word]
                    days_difference = (today.weekday() - target_day) % 7
                    if (
                        days_difference == 0
                    ):  # If today is the target day, return today's date
                        return today.strftime("%Y-%m-%d")
                    target_date = today - timedelta(days=days_difference)
                    return target_date.strftime("%Y-%m-%d")

            return "Invalid date string"

    def get_today_last_X_year(self, year: int = 1):
        self.today = datetime().date.today()
        previous_year = self.today.year - year
        today_last_year = self.today.replace(year=previous_year)
        today_last_year = str(today_last_year.strftime("%d/%m/%Y"))
        return today_last_year

    def load_settings(self, app_path: str):
        """
        Loading and assigning global variables from our settings.txt file
        """
        section_name = "DEFAULT"
        section_telegram = "TELEGRAM"
        section_facebook = "FACEBOOK"

        config_parser = configparser.RawConfigParser()
        config_file_path = app_path / "settings.txt"
        config_parser.read(config_file_path.absolute())
        app_path_abs = app_path.as_posix()
        settings = {
            "telegram_web": self.TELEGRAM_WEB,
            "whatsapp_web": self.WHATSAPP_WEB,
            "facebook_web": self.FACEBOOK_WEB,
            "chrome_user_data": self.CHROME_USER_DATA,
            "chrome_driver": config_parser.get(section_name, "CHROME_DRIVER_PATH"),
            "session": app_path_abs
            + "/"
            + config_parser.get(section_name, "SESSION_FILE"),
            "log": app_path_abs + "/" + config_parser.get(section_name, "LOG_FILE"),
            "output": app_path_abs
            + "/"
            + config_parser.get(section_name, "DEFAULT_OUTPUT"),
            "wait": config_parser.get(section_name, "WAIT_TIME"),
            "app_path": app_path_abs,
            "message": self.read_file_as_text(
                config_parser.get(section_name, "MESSAGE_PATH")
            ),
            "file": config_parser.get(section_name, "FILE_PATH"),
            "tg_id": config_parser.get(section_telegram, "TG_API_ID"),
            "tg_hash": config_parser.get(section_telegram, "TG_API_HASH"),
            "tg_phone": config_parser.get(section_telegram, "TG_PHONE_1"),
            "fb_username": config_parser.get(section_facebook, "USERNAME"),
            "fb_password": config_parser.get(section_facebook, "PASSWORD"),
        }
        return settings


class Ai:
    URL = "https://playground.allenai.org/"
    MODEL = "Llama-3-1-Tulu-3-70B"
    user_data_dir = helper.CHROME_USER_DATA

    def __init__(self, command, output=None):
        self.is_debug = bool(os.getenv("MT_DEBUG", False))
        self.helper = helper(output)
        if self.is_debug:
            logging.basicConfig(filename="Log/debug.log", level=logging.DEBUG)
        else:
            logging.basicConfig(filename="Log/error.log", level=logging.ERROR)
        language = detect(command)
        _command = f"""Keep the meaning of message and make it more powerful and more creative also use the emojis, 
        start the message direct without any introduction, send this message to my client and try to not mention the gender, 
        the Message with {language} and it is: ({command}) (I want 10 different versions,
        and MUST MUST MUST IMPORTANT each starting with 'Version _NUMBER_:' and keep the word 'Version' with English)"""
        command = f"{_command}, your answer MUST be in {language} language."
        self.result = self._run_browse(command)

    def _browse(self, command):
        try:
            # logger = logging.getLogger(__name__)
            os.makedirs(f"{self.user_data_dir}/AI", exist_ok=True)
            # logger.info(f'--user-data-dir={self.user_data_dir}/default')

            with sync_playwright() as p:
                # logger.info("Launching browser...")
                browser = p.chromium.launch_persistent_context(
                    user_data_dir=f"{self.user_data_dir}/AI",
                    headless=True,
                    args=[
                        "--no-sandbox",
                        "--disable-blink-features=AutomationControlled",
                        "--disable-features=IsolateOrigins,site-per-process",
                        "--disable-web-security",
                        "--disable-gpu",
                        "--disable-dev-shm-usage",
                    ],
                    slow_mo=500,
                )
                page = browser.pages[0] if browser.pages else browser.new_page()

                user_agents = [
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
                    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
                ]
                page.set_extra_http_headers({"User-Agent": random.choice(user_agents)})

                page.goto(self.URL, timeout=30000, wait_until="domcontentloaded")
                page.wait_for_load_state("networkidle")
                self.UpDateOutput("Update AI Model")
                combobox_selector = '.MuiSelect-select[role="combobox"]'
                page.wait_for_selector(combobox_selector, timeout=10000)
                page.click(combobox_selector)

                li_selector = f'li[data-value="{self.MODEL}"]'
                page.wait_for_selector(li_selector, timeout=10000)
                page.click(li_selector)
                self.UpDateOutput("Analysis your Message")
                page.evaluate(
                    """() => {
                    document.querySelectorAll("textarea").forEach(el => el.style.display = "block");
                }"""
                )
                page.wait_for_function(
                    "document.querySelector(\"textarea[aria-label='Message Tülu']\") !== null",
                    timeout=30000,
                )

                textarea_selector = 'textarea[aria-label="Message Tülu"]'
                page.wait_for_selector(textarea_selector, timeout=30000)
                page.click(textarea_selector, force=True)
                time.sleep(random.uniform(1, 3))

                pyperclip.copy(command)
                time.sleep(1)
                page.fill('textarea[aria-label="Message Tülu"]', command)

                time.sleep(random.uniform(1, 2))
                self.UpDateOutput("Generate New Messages List")
                page.keyboard.press("Enter", delay=random.uniform(100, 300))

                # page.screenshot(path="debug_screenshot.png")
                self.UpDateOutput("Please Wait...")
                parent_div_selector = 'div.MuiTypography-root.MuiTypography-body1.css-miq6sy[data-is-streaming="false"]'
                page.wait_for_selector(parent_div_selector, timeout=300000)

                send_icon_selector = 'svg[data-testid="SendIcon"]'
                page.wait_for_selector(send_icon_selector)

                child_div_selector = "div.MuiBox-root.css-0"
                inner_html = page.evaluate(
                    f"""() => {{
                    const parent = document.querySelector('{parent_div_selector}');
                    const child = parent ? parent.querySelector('{child_div_selector}') : null;
                    return child ? child.innerHTML : null;
                }}"""
                )
                self.UpDateOutput("Parsing New Messages")
                if inner_html:
                    FinalResult = []
                    soup = BeautifulSoup(inner_html, "html.parser")
                    text_content = soup.get_text()
                    result = list(text_content.split("Version "))

                    for item in result:
                        FinalResult.append(item.replace(":\n", ":"))
                    # end for
                    self.UpDateOutput("AI is Done")
                    return FinalResult
                else:
                    return None
        except Exception:
            logging.error("Error : \n" + traceback.format_exc())

    def _run_browse(self, command):
        return self._browse(command)

    def UpDateOutput(self, String: str):
        self.helper.UpDateOutput(String)

    def answer(self):
        return self.result if self.result else []


class AiWorker(QThread):
    finished = Signal(object)

    def __init__(self, command, output):
        super().__init__()
        self.command = command
        self.output = output

    def run(self):
        result = Ai(command=self.command, output=self.output)
        self.finished.emit(result)


class AI_Window(QDialog, AI_Dialog):

    def __init__(
        self,
        parent=None,
        command: list = None,
        CompanName: str = None,
        Compan_ID: str = None,
        Source: str = None,
        Database=None,
    ):
        super().__init__(parent)
        self.setupUi(self)
        self.database = Database
        self.model = QStringListModel()
        self.buttonBox.accepted.connect(self.ok_clicked)
        self.buttonBox.rejected.connect(self.reject)
        self.CompanName = CompanName
        self.Compan_ID = Compan_ID
        self.Source = Source
        self.ResultFinal = []

        self.listView.setModel(self.model)
        self.process_data(command)
        self.btnRemove.clicked.connect(self.remove_selected_item)

    def process_data(self, DataList: list):
        try:
            if isinstance(DataList, list):
                processed_list = [
                    msg.split(":", 1)[1].strip() for msg in DataList if ":" in msg
                ]
                if processed_list != self.model.stringList():
                    self.model.setStringList(processed_list)
            else:
                return DataList
        except Exception:
            logging.error("Error : \n" + traceback.format_exc())

    def remove_selected_item(self):
        selected_indexes = self.listView.selectedIndexes()
        if selected_indexes:
            index = selected_indexes[0].row()
            current_list = self.model.stringList()
            if 0 <= index < len(current_list):
                del current_list[index]
                self.model.setStringList(current_list)

    def ok_clicked(self):
        self.ResultFinal = self.model.stringList()
        for msg in self.ResultFinal:
            self.database.save_msg_history(
                self.CompanName, self.Compan_ID, msg, self.Source
            )
        self.accept()
