import asyncio
import logging
import os

from PySide6.QtCore import QStringListModel
from PySide6.QtWidgets import QListView

from utils.helper import helper
from Facebook.Facebook import Facebook
from Telegram.sTelegram import sTelegram
from WhatsApp.WhatsApp import WhatsApp


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

    async def parse_telegram_send_to_member(
        self,
        message: str = None,
        file_send: str = None,
        file_list: str = None,
        category: str = None,
        slogin: str = None,
        msg_img: bool = False,
        compan: str = None,
        translat: bool = False,
    ):
        self.helper.UpDateOutput(f"Telegram Send Message to Members {file_list}")
        tg = sTelegram(
            self.settings,
            database=self.database,
            category=category,
            output=self.Output_Item,
        )
        return await tg.telegram_send_message(
            message=message,
            file_send=file_send,
            file_list=file_list,
            slogin=slogin,
            compan=compan,
            msg_img=msg_img,
            translat=translat,
        )

    async def parse_telegram_group(self, pathfile: str, category: str):
        tg = sTelegram(
            self.settings,
            database=self.database,
            category=category,
            output=self.Output_Item,
        )
        self.helper.UpDateOutput("Init Telegram Group...")
        return await tg.get_group_members(pathfile)

    async def parse_telegram_message_group(
        self,
        mode: str,
        max_date,
        main_channel: str,
        target_channel: str = None,
        list1: list = None,
        list2: list = None,
        category: str = None,
    ):
        self.helper.UpDateOutput("Telegram Message")
        tg = sTelegram(
            self.settings,
            database=self.database,
            category=category,
            output=self.Output_Item,
        )
        return await tg.fetch_all_group_message(
            mode=mode,
            max_date=max_date,
            main_channel=main_channel,
            target_channel=target_channel,
            list1=list1,
            list2=list2,
        )

    async def parse_add_members_to_channel(
        self, channel_name: str, category: str = None, member_list: str = None
    ):
        self.helper.UpDateOutput("Telegram Add Members to Channel")
        tg = sTelegram(
            self.settings,
            database=self.database,
            category=category,
            output=self.Output_Item,
        )
        return await tg.add_members_to_channel(channel_name, member_list)

    # WhatsApp
    async def parse_whatsapp_group(self, group_name: str, category: str):
        self.helper.UpDateOutput("WhatsApp Group")
        wp = WhatsApp(self.settings, self.database, output=self.Output_Item)
        return await wp.get_group_members(group_name, category)

    async def parse_whatsapp_contact(self, category):
        self.helper.UpDateOutput(f"Get your WhatsApp Contact under Category {category}")
        wp = WhatsApp(self.settings, self.database, output=self.Output_Item)
        return await wp.get_contact_numbers(category)

    def parse_whatsapp_messages(
        self,
        chat_name,
        category: str,
    ):
        self.helper.UpDateOutput("WhatsApp Messages Sender")
        wp = WhatsApp(self.settings, self.database, output=self.Output_Item)
        wp.get_all_message(chat_name, category)

    def parse_new_groups(self):
        wp = WhatsApp(
            self.settings, self.database, output=self.Output_Item
        )
        wp.get_new_groups_google()

    async def send_message_to_whatsapp(
        self,
        message: str,
        slogin: str,
        category: str,
        file_send: str = None,
        country: str = None,
        timezone: str = None,
        list_file: str = None,
        compan: str = None,
        translation: bool = False,
    ):
        self.helper.UpDateOutput("WhatsApp Send Messages to Members")
        wp = WhatsApp(self.settings, self.database, output=self.Output_Item)
        return await wp.send_message_to_members(
            message=message,
            slogin=slogin,
            category=category,
            file_send=file_send,
            country=country,
            timezone=timezone,
            list_file=list_file,
            compan=compan,
            translation=translation,
        )

    # Facebook
    async def post_facebook_group(
        self,
        group_post: str,
        category: str,
        group_list: str,
        use_AI: bool = False,
        CompanName: str = None,
        Slogin: str = None,
    ):
        self.helper.UpDateOutput("Post Message in Facebook Group")
        fb = Facebook(
            self.settings, self.database, output=self.Output_Item
        )
        return await fb.post_to_groups(
            message=group_post,
            category=category,
            list_of_groups=group_list,
            useAI=use_AI,
            CompanName=CompanName,
            Slogin=Slogin,
        )

    async def get_members_facebook_group(self, category: str, group_name: str = None):
        self.helper.UpDateOutput("Get Facebook Members in Group")
        fb = Facebook(
            self.settings, self.database, output=self.Output_Item
        )
        return await fb.get_group_members(category, group_name)

    async def send_message_to_memebers(
        self,
        message: str,
        filePath: str,
        category: str,
        use_AI=False,
        CompanName: str = None,
        Slogin: str = None,
    ):
        self.helper.UpDateOutput("Send Message to Facebook Members")
        fb = Facebook(
            self.settings, self.database, output=self.Output_Item
        )
        return await fb.send_to_members(
            message,
            category,
            filePath,
            useing_AI=use_AI,
            CompanName=CompanName,
            Slogin=Slogin,
        )

    async def send_message_to_chatgroup(self):
        self.helper.UpDateOutput("Send Message to Chat Groups")
        fb = Facebook(self.settings, self.database, self.category)
        return await fb.send_to_group_chat(self.fb_send_msg_to_chatgroup)
