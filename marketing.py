import asyncio
import logging

from PySide6.QtCore import QStringListModel
from PySide6.QtWidgets import QListView

from Facebook.Facebook import Facebook
from Telegram.sTelegram import sTelegram
from utils.helper import helper
from WhatsApp.WhatsApp import WhatsApp
import os


class marketing:
    settings = None

    def __init__(self, settings, database, output=QListView):
        self.is_debug = bool(os.getenv("MT_DEBUG", False))
        if self.is_debug:
            logging.basicConfig(filename="Log/debug.log", level=logging.DEBUG)
        else:
            logging.basicConfig(filename="Log/error.log", level=logging.ERROR)
        self.settings = settings
        self.database = database
        self.Output_Item = output
        self.helper = helper(output)

    def parse_telegram_send_to_member(
        self, message: str, file: str, file_list: str, category: str, use_AI:bool=False
    ):
        self.helper.UpDateOutput(f"Telegram Send Message to Members {file_list}")
        tg = sTelegram(
            self.settings,
            database=self.database,
            category=category,
            output=self.Output_Item,
        )
        asyncio.run(
            tg.send_message_without_block(
                message=message, file_send=file, file_list=file_list, use_AI=use_AI
            )
        )

    def parse_telegram_group_web(self, pathfile: str, category: str):
        # def parse_telegram_group(self, pathfile: str):
        self.helper.UpDateOutput("Telegram Group : " + pathfile)
        tg = sTelegram(
            self.settings,
            database=self.database,
            category=category,
            output=self.Output_Item,
        )
        tg.get_group_members_low_risk(pathfile, login=False)

    async def parse_telegram_group(self, pathfile: str, category: str):
        self.helper.UpDateOutput("Telegram Group : " + pathfile)
        tg = sTelegram(
            self.settings,
            database=self.database,
            category=category,
            output=self.Output_Item,
        )
        return await tg.get_group_members(pathfile)

    def parse_telegram_message_group(
        self,
        mode: str,
        max_date,
        main_channel: str,
        target_channel: str=None,
        category: str=None,
    ):
        self.helper.UpDateOutput("Telegram Message")
        tg = sTelegram(
            self.settings,
            database=self.database,
            category=category,
            output=self.Output_Item,
        )
        asyncio.run(
            tg.fetch_all_group_message(
                mode=mode,
                max_date=max_date,
                main_channel=main_channel,
                target_channel=target_channel,
            )
        )

    def parse_add_members_to_channel(
        self, channel_name: str, category: str=None, member_list: str=None
    ):
        self.helper.UpDateOutput("Telegram Add Members to Channel")
        tg = sTelegram(
            self.settings,
            database=self.database,
            category=category,
            output=self.Output_Item,
        )
        asyncio.run(tg.add_members_to_channel(channel_name, member_list))

    # WhatsApp
    def parse_whatsapp_group(self, group_name:str, category:str):
        self.helper.UpDateOutput("WhatsApp Group")
        wp = WhatsApp(
            self.settings, self.database, output=self.Output_Item
        )
        asyncio.run(wp.get_group_members(group_name, category))
        

    def parse_whatsapp_contact(self, category):
        self.helper.UpDateOutput(f"Get your WhatsApp Contact under Category {category}")
        wp = WhatsApp(
            self.settings,
            self.database,
            output=self.Output_Item
        )
        asyncio.run(wp.get_contact_numbers(category))

    def parse_whatsapp_messages(self, chat_name, category:str,):
        self.helper.UpDateOutput("WhatsApp Messages Sender")
        wp = WhatsApp(
            self.settings, self.database, output=self.Output_Item
        )
        wp.get_all_message(chat_name, category)

    def parse_new_groups(self):
        wp = WhatsApp(self.settings, self.database, run_browser=False, output=self.Output_Item)
        wp.get_new_groups_google()

    def send_message_to_whatsapp(self, message: str,slogin:str,category:str,file_send: str=None,country: str=None,timezone: str=None,list_file: str=None,compan:str=None,translation: bool=False):
        self.helper.UpDateOutput("WhatsApp Send Messages to Members")
        wp = WhatsApp(
            self.settings, self.database, output=self.Output_Item
        )
        asyncio.run(wp.send_message_to_members(message=message,slogin=slogin,category=category,file_send=file_send,country=country,timezone=timezone,list_file=list_file,compan=compan,translation=translation))

    # Facebook
    def post_facebook_group(self, group_post:str, category:str, group_list:str, use_AI:bool=False, CompanName:str=None):
        self.helper.UpDateOutput("Post Message in Facebook Group")
        fb = Facebook(self.settings, self.database, output=self.Output_Item, headless=False)
        return fb.post_to_groups(message=group_post, category=category, list_of_groups=group_list, useAI=use_AI, CompanName=CompanName)

    def get_members_facebook_group(self, category:str, group_name:str=None):
        self.helper.UpDateOutput("Get Facebook Members in Group")
        fb = Facebook(self.settings, self.database, output=self.Output_Item, headless=True)
        asyncio.run(fb.get_group_members(category, group_name))

    def send_message_to_memebers(self, message:str, filePath:str, category:str, use_AI=False, CompanName:str=None):
        self.helper.UpDateOutput("Send Message to Facebook Members")
        fb = Facebook(self.settings, self.database, output=self.Output_Item, headless=False)
        asyncio.run(fb.send_to_members(message, category, filePath, useing_AI=use_AI, CompanName=CompanName))

    def send_message_to_chatgroup(self):
        self.helper.UpDateOutput("Send Message to Chat Groups")
        fb = Facebook(self.settings, self.database, self.category, headless=False)
        fb.send_to_group_chat(self.fb_send_msg_to_chatgroup)
