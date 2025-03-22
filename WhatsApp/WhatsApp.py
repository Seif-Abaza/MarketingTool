import asyncio
import logging
import os
import random
import re
import shutil
import sys
import traceback
from datetime import datetime
from random import randrange
from time import sleep

import urllib3
from googletrans import Translator
from PySide6.QtWidgets import QListView, QMessageBox

from utils.PhoneParsing import PhoneParsing

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from playwright.async_api import TimeoutError as PlaywrightTimeoutError
from playwright.async_api import async_playwright
from playwright.sync_api import sync_playwright

from utils.helper import helper


class WhatsApp:

    MESSAGES = "wp_message"
    PHONE = "phone_numbers"
    GROUPS = "groups"

    availabledom = [
        "pastebin",
        "throwbin",
        "pastr",
        "pasteio",
        "paste2",
        "hastebin",
        "gist.github",
        "ghostbin",
        "ideone",
        "codepen",
        "pastefs",
        "snipplr",
        "slexy",
        "justpaste",
        "0bin",
        "cl1p.net",
        "dpaste.com",
        "dpaste.org",
        "heypasteit.com",
        "hpaste.org",
        "ideone.com",
        "kpaste.net",
        "paste.kde.org",
        "paste2.org",
        "pastebin.ca",
        "pastebin.com",
        "paste.org.ru",
        "pastie.org",
        "snipplr.com",
        "paste.org",
    ]

    def __init__(
        self,
        settings,
        database,
        run_browser=True,
        output: QListView = None,
        headless: bool = True,
    ):
        self.settings = settings
        self.database = database

        # Create Table if not exist
        self.database.create_table(self.MESSAGES)
        self.database.create_table(self.PHONE)
        self.database.create_table(self.GROUPS)

        self.helper = helper(output)
        self.helper.UpDateOutput("Starting WhatsApp...")
        if not os.path.isdir(f"{self.helper.CHROME_USER_DATA}/whatsapp"):
            with sync_playwright() as p:
                # logger.info("Launching browser...")
                browser = p.chromium.launch_persistent_context(
                    user_data_dir=f"{self.helper.CHROME_USER_DATA}/whatsapp",
                    headless=False,
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
                page.goto(self.helper.WHATSAPP_WEB, timeout=10000)
                page.wait_for_load_state("networkidle")
                self.helper.UpDateOutput("Start WhatsApp")
                page.wait_for_selector(
                    '//canvas[@aria-label="Scan this QR code to link a device!" and @role="img"]',
                    timeout=500000,
                )
                msg_box = QMessageBox()
                msg_box.setWindowTitle("Confirmation")
                msg_box.setText(
                    "This is First time only, did you scanned your QR Code ?"
                )
                msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                response = msg_box.exec()
                if response == QMessageBox.No:
                    self.driver.close()

    async def search(self, page, text_search: str):
        try:
            # Wait for the search box to be visible
            search_box = await page.wait_for_selector(
                '//div[@contenteditable="true"][@data-tab="3"]', timeout=5000
            )
            # Click, clear previous text, and enter new text
            await search_box.click()
            await search_box.fill("")  # Clear text field
            await search_box.type(text_search)  # Enter new text
            # Wait for the search result to appear
            element = await page.wait_for_selector(
                f'//span[contains(@title, "{text_search}")]', timeout=10000
            )
            # Click on the search result
            await element.click()
        except Exception as e:
            logging.error("Error:\n" + traceback.format_exc())
            return False

    def reLogin(self):
        if os.path.exists(self.helper.CHROME_USER_DATA + "/whatsapp"):
            shutil.rmtree(
                self.helper.CHROME_USER_DATA + "/whatsapp", ignore_errors=True
            )
        with sync_playwright() as p:
            browser = p.chromium.launch_persistent_context(
                user_data_dir=self.helper.CHROME_USER_DATA + "/whatsapp",
                headless=False,
                args=[
                    "--no-sandbox",
                    "--disable-blink-features=AutomationControlled",
                    "--disable-features=IsolateOrigins,site-per-process",
                    "--disable-web-security",
                ],
            )
            page = browser.pages[0] if browser.pages else browser.new_page()
            user_agents = [
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
            ]

            page.set_extra_http_headers({"User-Agent": random.choice(user_agents)})
            page.goto(self.helper.WHATSAPP_WEB, timeout=100000)
            page.wait_for_load_state("networkidle")
            self.helper.UpDateOutput("Start WhatsApp")
            page.wait_for_selector(
                '//canvas[@aria-label="Scan this QR code to link a device!" and @role="img"]',
                timeout=500000,
            )
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Confirmation")
            msg_box.setText("This is First time only, did you scanned your QR Code ?")
            msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            response = msg_box.exec()
            if response == QMessageBox.No:
                self.driver.close()
                return False
            else:
                return True

    async def send_message(self, phone_number, message: str):
        try:
            url = f"https://web.whatsapp.com/send?phone={phone_number}&text={message}"
            async with async_playwright() as p:
                browser = await p.chromium.launch_persistent_context(
                    user_data_dir=self.helper.CHROME_USER_DATA + "/whatsapp",
                    headless=True,
                    args=[
                        "--no-sandbox",
                        "--disable-blink-features=AutomationControlled",
                        "--disable-features=IsolateOrigins,site-per-process",
                        "--disable-web-security",
                    ],
                )
                page = browser.pages[0] if browser.pages else await browser.new_page()
                user_agents = [
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
                    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
                ]

                selected_user_agent = random.choice(user_agents)
                await page.set_extra_http_headers({"User-Agent": selected_user_agent})
                await page.set_viewport_size({"width": 830, "height": 930})
                await page.goto(url, timeout=120000)
                await page.wait_for_selector(
                    '//button[@aria-label="Send"]', timeout=15000
                )  # 15 seconds timeout
                await page.locator('//button[@aria-label="Send"]').click(force=True)
                self.database.save_msg_or_post(
                    user=phone_number, message=message, source="WhatsApp"
                )
                await browser.close()

            return True
        except PlaywrightTimeoutError:
            self.helper.UpDateOutput("Please Re-Login to WhatsApp")
            return self.reLogin()
        except NoSuchElementException:
            logging.error("Error : \n" + traceback.format_exc())
            return False

    async def send_message_to_members(
        self,
        message: str = None,
        slogin: str = None,
        category: str = None,
        file_send: str = None,
        country: str = None,
        timezone: str = None,
        list_file: str = None,
        compan: str = None,
        translation: bool = False,
    ):
        self.helper.UpDateOutput("Init Send Message Module")
        ppPhone = PhoneParsing()
        if list_file:
            members = list_file
        else:
            data = {"category": category, "country": country, "timezone": timezone}
            filtered_data = {
                key: value
                for key, value in data.items()
                if value is not None and len(value) > 0
            }
            members = self.database.read_from_database("phone_numbers", filtered_data)

        if compan:
            self.helper.UpDateOutput("Waitnig AI Results")
            loop_time = 0
            message_list = []
            while len(message_list) == 0:
                if loop_time >= 50:
                    send_message = message
                    break
                else:
                    loop_time += 1
                message_list = self.database.get_msg_history(compan)
                await asyncio.sleep(randrange(4, 10))
        else:
            send_message = message

        NumberOfUsers = 1

        try:
            for member in members:
                if isinstance(member, str):
                    PhoneNumber = member
                else:
                    PhoneNumber = member["number"]

                Information = ppPhone.get_information_from_phone(PhoneNumber)
                if not Information is None:
                    self.helper.UpDateOutput(
                        f'Number {PhoneNumber} from {Information["Country"]} and there Language is {Information["Language"]}'
                    )
                else:
                    self.helper.UpDateOutput(f"Number {PhoneNumber}")
                # Hold for Un-Block
                if NumberOfUsers >= 25:
                    NumberOfUsers = 1
                    self.helper.UpDateOutput("Holding....")
                    asyncio.sleep(randrange(25, 30))
                    continue

                # Get Message from AI or Direct
                if len(message_list) > 0:
                    send_message = message_list[randrange(0, len(message_list))][
                        "message"
                    ]
                else:
                    send_message = message
                if translation:
                    if not Information is None:
                        self.helper.UpDateOutput(
                            f'Translation to {list(Information["Language"])[0]} ({list(Information["Language"])[0].lower()[:2]})'
                        )
                        async with Translator(timeout=20000) as translator:
                            result = await translator.translate(
                                send_message,
                                dest=list(Information["Language"])[0].lower()[:2],
                            )
                            send_message = result.text
                    else:
                        self.helper.UpDateOutput("There is issue in number...")

                # Set Slogin if Exist
                if not slogin is None:
                    sloginText = slogin.split(":")
                    if int(sloginText[0]) == 0:
                        send_message = f"{sloginText[1]}\n\n{send_message}"
                    else:
                        send_message = f"{send_message}\n\n{sloginText[1]}"

                # Send Message
                self.helper.UpDateOutput(f"Message: {send_message}")
                if await self.send_message(PhoneNumber, message=send_message):
                    self.helper.UpDateOutput(f"Send to {PhoneNumber} is Done")
                    NumberOfUsers += 1
                    sleep(randrange(5, 15))
                else:
                    self.helper.UpDateOutput(
                        f"There is Error when try to send to this Number {PhoneNumber}"
                    )
                    break
        except Exception as e:
            self.helper.UpDateOutput(e)
            logging.error(traceback.format_exc())

    def _add_phone_number(self, phone_number: str, source: str, category: str) -> bool:
        if phone_number.startswith("+"):
            if not self.database.search_by_column(self.PHONE, "number", phone_number):
                ContryPhone = PhoneParsing().get_phone_number_and_get_country(
                    phone_number
                )
                TimeZone = PhoneParsing().get_time_zone_from_number(phone_number)
                self.database.write_to_database(
                    self.PHONE,
                    {
                        "number": phone_number,
                        "country": ContryPhone,
                        "timezone": TimeZone,
                        "category": category,
                        "group_name": source,
                    },
                )
                self.helper.UpDateOutput(
                    f"Add {phone_number} from {ContryPhone} to your Database"
                )
                return True
        return False

    def _add_group_name_to_database(self, group_name, group_url=None):
        if group_name is None:
            return False
        self.database.write_to_database(
            self.GROUPS,
            {
                "name": group_name,
                "url": group_url,
            },
        )
        return True

    async def get_contact_numbers(self, category):
        try:
            async with async_playwright() as p:
                browser = await p.chromium.launch_persistent_context(
                    user_data_dir=self.helper.CHROME_USER_DATA + "/whatsapp",
                    headless=True,
                    args=[
                        "--no-sandbox",
                        "--disable-blink-features=AutomationControlled",
                        "--disable-features=IsolateOrigins,site-per-process",
                        "--disable-web-security",
                    ],
                )
                page = browser.pages[0] if browser.pages else await browser.new_page()
                user_agents = [
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
                    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
                ]

                selected_user_agent = random.choice(user_agents)
                await page.set_extra_http_headers({"User-Agent": selected_user_agent})
                await page.set_viewport_size({"width": 830, "height": 930})
                await page.goto(self.helper.WHATSAPP_WEB, timeout=100000)
                await page.wait_for_load_state("networkidle")
                self.helper.UpDateOutput("Start WhatsApp")
                self.helper.UpDateOutput("Waiting for chats to load...")
                await page.wait_for_selector(
                    '//div[@id="pane-side"]//span[@title]', timeout=20000
                )
                chat_list = await page.locator(
                    '//div[@id="pane-side"]//span[@title]'
                ).all()
                # Iterate through the chat list and extract contact numbers
                self.helper.UpDateOutput("Scan contact numbers...")
                for idx, chat in enumerate(chat_list, start=1):
                    contact_number = await chat.get_attribute("title")
                    if contact_number:
                        contact_number = (
                            contact_number.replace(" ", "")
                            .replace("-", "")
                            .replace("(", "")
                            .replace(")", "")
                        )
                    if not self._add_phone_number(
                        contact_number, source="Contact", category=category
                    ):
                        self.helper.UpDateOutput(
                            f"Contact {idx}: {contact_number} is not added."
                        )

                self.helper.UpDateOutput("Scan completed successfully.")
                await self.reset_whatsapp(page)
                browser.close()
            return True
        except Exception as e:
            self.helper.UpDateOutput(f"An error occurred during scaning")
            await self.reset_whatsapp(page)
            browser.close()
            logging.error("Error : \n" + traceback.format_exc())
            return False

    def get_all_message(self, chat_name, category):
        try:
            self.search(chat_name)
            sleep(3)
            # Scroll to the top to load all messages
            self.helper.UpDateOutput("Scrolling to load all messages...")
            last_height = self.driver.execute_script(
                "return document.querySelector('div.copyable-area').scrollHeight"
            )
            while True:
                self.driver.execute_script(
                    "document.querySelector('div.copyable-area').scrollTo(0, 0);"
                )
                sleep(2)  # Reduced wait time for quicker scrolling
                new_height = self.driver.execute_script(
                    "return document.querySelector('div.copyable-area').scrollHeight"
                )
                if new_height == last_height:
                    break
                last_height = new_height

            # Extract messages
            self.helper.UpDateOutput("Extracting messages...")
            messages = self.driver.find_elements(
                By.XPATH,
                '//div[contains(@class, "message-in") or contains(@class, "message-out")]',
            )

            for idx, message in enumerate(messages, start=1):
                try:
                    text_elements = message.find_elements(
                        By.XPATH,
                        './/span[@class="_ao3e selectable-text copyable-text"]//span',
                    )
                    if text_elements:
                        text = " ".join([element.text for element in text_elements])
                        timestamp = message.find_element(
                            By.XPATH, ".//div[@data-pre-plain-text]"
                        ).get_attribute("data-pre-plain-text")
                        phone_in_chat = PhoneParsing().get_number_from_text(text)
                        if not phone_in_chat is None:
                            for ptnumber in phone_in_chat:
                                self._add_phone_number(
                                    ptnumber["number"],
                                    source=chat_name,
                                    category=category,
                                )

                        self.database.write_to_database(
                            self.MESSAGES,
                            {
                                "chat_name": chat_name,
                                "message": text,
                                "timestamp": timestamp,
                                "category": category,
                            },
                        )
                        self.helper.UpDateOutput(f"Message {idx}: {timestamp} - {text}")
                except Exception as e:
                    self.helper.UpDateOutput(f"Error extracting message {idx}: {e}")
                    continue

            self.helper.UpDateOutput(f"Scraping completed for chat: {chat_name}")
            self.reset_whatsapp()
            return True

        except Exception as e:
            self.helper.UpDateOutput(
                f"An error occurred while scraping chat {chat_name}: {e}"
            )
            logging.error("Error : \n" + traceback.format_exc())
            return False

    async def get_group_members(self, group_name=None, category: str = None):
        try:
            if isinstance(group_name, list):
                for group in group_name:
                    await self._get_group_members(group, category)
            elif len(group_name) > 1:
                await self._get_group_members(group_name, category)
            elif (
                group_name is None or len(group_name) == 0
            ):  # It's not List of Group Name
                await self.get_groups(category)
        except Exception:
            logging.error("Error : \n" + traceback.format_exc())

    async def get_groups(self, category: str):
        try:
            group_tab = await self.page.wait_for_selector("#group-filter", timeout=5000)
            await group_tab.click()
        except Exception as e:
            self.helper.UpDateOutput(f"Error clicking on 'Groups' tab: {e}")
            return []

        # Find all group elements in the chat list
        try:
            groups = await self.page.locator("//div[@role='gridcell']").all()
            group_names = [
                await group.inner_text()
                for group in groups
                if (await group.inner_text()).strip()
            ]

            cleaned_groups = [
                re.sub(r"\n.*", "", group)
                for group in group_names
                if not group.isnumeric()
            ]

            for group_name in cleaned_groups:
                self.helper.UpDateOutput(f" Get Members in Group {group_name}")
                await self._get_group_members(
                    group_name, category
                )  # Ensure _get_group_members is async
                self.helper.UpDateOutput(f"Members in group {group_name} is Done")

        except Exception as e:
            self.helper.UpDateOutput(f"Error fetching group names: {e}")
            return []

    async def _get_group_members(self, group_name, category):
        self.helper.UpDateOutput(f"Starting scraping for chat: {group_name}")
        try:
            async with async_playwright() as p:
                browser = await p.chromium.launch_persistent_context(
                    user_data_dir=self.helper.CHROME_USER_DATA + "/whatsapp",
                    headless=True,
                    args=[
                        "--no-sandbox",
                        "--disable-blink-features=AutomationControlled",
                        "--disable-features=IsolateOrigins,site-per-process",
                        "--disable-web-security",
                    ],
                )
                page = browser.pages[0] if browser.pages else await browser.new_page()
                user_agents = [
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
                    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
                ]

                selected_user_agent = random.choice(user_agents)
                await page.set_extra_http_headers({"User-Agent": selected_user_agent})
                await page.set_viewport_size({"width": 830, "height": 930})
                await page.goto(self.helper.WHATSAPP_WEB, timeout=100000)
                await page.wait_for_load_state("networkidle")
                sleep(randrange(2, 10))
                # Click on the chat
                self.helper.UpDateOutput("Selecting the Group...")
                await self.search(page, group_name)
                # await page.screenshot(path="debug_search.png")
                sleep(randrange(2, 5))  # Wait for chat to load
                text_element = await page.wait_for_selector(
                    '//span[contains(@class, "_ao3e") and contains(@class, "selectable-text") and contains(@class, "copyable-text")]',
                    timeout=10000,
                )
                # self._get_group_members(group_name)
                text = await text_element.inner_text()
                text = text.replace(" ", "")
                list_of_numbers = text.split(",")
                for number in list_of_numbers:
                    self._add_phone_number(number, source=group_name, category=category)

                self.helper.UpDateOutput("Completed successfully.")
                await self.reset_whatsapp(page)
                # await page.screenshot(path="debug_clear_search.png")
                return True
        except TimeoutException as e:
            self.helper.UpDateOutput(f" :triangular_flag_on_post: An error occurred")
            logging.error("Error : \n" + traceback.format_exc())
            return False
        pass

    async def reset_whatsapp(self, page):
        try:
            self.helper.UpDateOutput("Returning to the home screen...")
            contenteditable_element = page.locator(
                '[aria-label="Search input textbox"][contenteditable="true"]'
            )
            # Click inside the input box
            await contenteditable_element.click()
            # Select all text (Ctrl + A or Command + A) and delete
            await contenteditable_element.press("Control+A")  # For Windows/Linux
            await contenteditable_element.press("Backspace")
            # Alternative for macOS
            await contenteditable_element.press("Meta+A")
            await contenteditable_element.press("Backspace")
            return True
        except TimeoutException:
            logging.error("Error : \n" + traceback.format_exc())
            return False

    def get_new_groups_google(self, number_of_groups=0):
        self.helper.UpDateOutput("[bold yellow]Get New Groups[/bold yellow]")
        for dom in self.availabledom:
            user_agents = [
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
                "Mozilla/5.0 (Windows NT 6.1; Win64; x64)",
            ]
            # query = "link:chat.whatsapp.com AND site:" + dom
            query = "intext:chat.whatsapp.com inurl:" + dom
            self.helper.UpDateOutput(query)
            try:
                for url in search(
                    query,
                    num=10,
                    stop=10,
                    pause=10,
                    user_agent=random.choice(user_agents),
                ):
                    req = urllib3.request.Request(
                        url, headers=random.choice(user_agents)
                    )
                    txt = urllib3.request.urlopen(req).read().decode("utf8")
                    # var_dump(txt)
                    # scrape(txt)
                    sleep(5)
            except Exception:
                logging.error("Error : \n" + traceback.format_exc())
                sleep(5)

    def get_new_groups_from_links(self, number_of_groups):
        pass
