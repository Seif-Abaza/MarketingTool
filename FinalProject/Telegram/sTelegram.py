import hashlib
import logging
import math
import os
import sys
import traceback
import unicodedata
from random import randrange
from time import sleep

import telethon
from PySide6.QtCore import QDir
from PySide6.QtWidgets import QInputDialog, QLineEdit, QListView
from telethon import TelegramClient, functions, types
from telethon.errors.rpcerrorlist import UsernameInvalidError
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.messages import SendMessageRequest
from telethon.tl.types import PeerUser, InputPeerChat
from telethon.tl.functions.contacts import ResolveUsernameRequest
from utils.helper import helper
from PySide6.QtWidgets import QApplication, QMessageBox
import uuid

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

TABLE_NAME = "Telegram"


class sTelegram:

    def __init__(self, settings, database, category=None, output: QListView=None):
        self.settings = settings
        self.helper = helper(output)
        self.database = database
        self.database.create_table(TABLE_NAME)
        self.category = category
        api_id, api_hash, phone_number, session_name = (
            self.settings["tg_api_id"],
            self.settings["tg_api_hash"],
            self.settings["tg_phone"],
            "Sessions/teleSession",
        )
        self.is_debug = bool(os.getenv("MT_DEBUG", False))
        if self.is_debug:
            logging.basicConfig(filename="Log/debug.log", level=logging.DEBUG)
        else:
            logging.basicConfig(filename="Log/error.log", level=logging.ERROR)
        self.api_id = api_id
        self.api_hash = api_hash
        self.phone_number = phone_number
        self.session_name = session_name
        self.Tg = None

    def show_message(self):
        number, ok = QInputDialog.getText(
            None, "Enter Code", "Enter the Telegram login code:"
        )
        if ok and number.isdigit():
            return number
        else:
            raise ValueError("Invalid or no code entered!")

    async def Connected(self):
        try:
            if self.Tg is None:
                self.Tg = TelegramClient(self.session_name, self.api_id, self.api_hash)
                if self.phone_number is None:
                    raise ValueError("Phone number is missing!")

                phone = str(self.phone_number).strip()
                if not phone:
                    raise ValueError("Phone number is empty after conversion!")

                if not self.Tg.is_connected():
                    await self.Tg.start(
                        phone=self.phone_number, code_callback=self.show_message
                    )
                    # await self.Tg.connect()
                    return self.Tg
                if not await self.Tg.is_user_authorized():
                    await self.Tg.send_code_request(self.phone_number)
                    text, ok = QInputDialog.getText(
                        self,
                        "QInputDialog.getText()",
                        "Received Code :",
                        QLineEdit.Normal,
                    )
                    if ok and text:
                        await self.Tg.sign_in(self.phone_number, text)
                    return self.Tg
            else:
                return self.Tg

            return None
        except Exception:
            logging.error("Error : \n" + traceback.format_exc())
            await self.Tg.disconnect()
            return None

    async def get_group_members(self, filelist):
        try:
            Number_Of_Group = 0
            await self.Connected()
            if self.Tg.is_connected():
                groups = self.helper.readlist_file(filelist)
                for group in groups:
                    if Number_Of_Group <= 3:
                        self.helper.UpDateOutput(f"Open Group {group}")
                        # channel = await self.Tg(ResolveUsernameRequest(group))
                        # channel = await self.Tg.get_input_entity(str(group))
                        # members = await self.Tg.get_participants(str(group))
                        # channel = await self.Tg.get_entity(str(group))
                        # members = await self.Tg.get_participants(str(channel))
                        # members = self.Tg.iter_participants(entity=channel)
                        members = await self.Tg.get_participants(group, aggressive=True)
                        self.helper.UpDateOutput(f"Get Members from {group}")
                        Number_Of_Group += 1
                    else:
                        Number_Of_Group = 0
                        seconds = randrange(300, 1000)
                        self.helper.UpDateOutput(
                            f"-: Hold from {seconds} seconds and Back to Work :-"
                        )
                        sleep(seconds)
                        continue

                    try:
                        for member in members:
                            if (
                                not member.bot
                                and not member.is_self
                                and not member.deleted
                                and not member.fake
                                and not member.scam
                            ):
                                member_data = {
                                    "id": member.id,
                                    "first_name": unicodedata.normalize(
                                        "NFKC",
                                        getattr(member, "first_name", "Unknown")
                                        or "Unknown",
                                    ),
                                    "last_name": unicodedata.normalize(
                                        "NFKC",
                                        getattr(member, "last_name", "Unknown")
                                        or "Unknown",
                                    ),
                                    "username": unicodedata.normalize(
                                        "NFKC",
                                        getattr(member, "username", "Unknown")
                                        or "Unknown",
                                    ),
                                    "phone": getattr(member, "phone", "Unknown"),
                                    "last_active": "Unknown",
                                    "category": self.category,
                                }
                                if self.database.write_to_database(
                                    TABLE_NAME, member_data
                                ):
                                    self.helper.UpDateOutput(
                                        "Add to database user "
                                        +member_data["username"]
                                    )
                                else:
                                    self.helper.UpDateOutput(
                                        "User Exist in Database : "
                                        +member_data["username"]
                                    )

                    except Exception:
                        logging.error("Error : \n" + traceback.format_exc())
                        continue
                    seconds = randrange(10, 100)
                    # minutes = math.floor(seconds / 60)
                    self.helper.UpDateOutput(
                        f"Finished Group {group} and i will hold {seconds} seconds."
                    )
                    sleep(seconds)
                return True
        except Exception:
            logging.error("Error : \n" + traceback.format_exc())
            return False
        finally:
            await self.Tg.disconnect()

    async def send_to_member(
        self,
        member_id: int,
        text_message: str=None,
        file_send: str=None,
        mode: str="text",
    ):
        try:
            if self.Tg == None:
                await self.Connected()
            members = ""
            if member_id:
                if mode == "text":
                    await self.Tg.send_message(member_id, text_message)
                elif mode == "file":
                    await self.Tg.send_file(member_id, file_send)
                elif mode == "both":
                    await self.Tg.send_message(
                        member_id, message=text_message, file=file_send
                    )
            else:
                members = self.database.read_from_database(
                    TABLE_NAME, {"category": self.category}
                )
                for member in members:
                    if mode == "text":
                        await self.Tg.send_message(member.id, text_message)
                    elif mode == "file":
                        await self.Tg.send_file(member.id, file_send)
                    elif mode == "both":
                        await self.Tg.send_message(
                            member_id, message=text_message, file=file_send
                        )

        except Exception:
            logging.error("Error : \n" + traceback.format_exc())

    async def add_members_to_channel(self, channel: str, member_list: str=None):
        """
        Adds multiple members to a channel or group.

        :param channel: The channel or group entity (or its username) to which members will be added.
        :param member_ids: A list of user IDs or usernames to add.
        """
        MyChannel = None
        await self.Connected()
        try:
            # Resolve the channel entity
            # lchannel = await self.Tg.get_entity('@' + channel)
            MyChannel = await self.Tg.get_input_entity(channel)
            self.helper.UpDateOutput(
                f"Resolved channel: {MyChannel.title} (ID: {MyChannel.id})"
            )

        except UsernameInvalidError:
            dialog_list = await self.Tg.get_dialogs()
            for chats in dialog_list:
                if chats.title == channel:
                    MyChannel = chats
                    break
            else:
                self.helper.UpDateOutput(
                    f"Error: The channel username '{channel}' is invalid or does not exist."
                )
                return
        except Exception as e:
            self.helper.UpDateOutput(f"Error resolving channel: {e}")
            return
        try:
            if member_list is None:
                try:
                    members = self.database.read_from_database(
                        TABLE_NAME, {"category": self.category}
                    )
                    for member in members:
                        user = await self.Tg.get_entity(member["id"])
                        await self.Tg(
                            InviteToChannelRequest(channel=MyChannel, users=[user])
                        )
                        sleep(randrange(1, 3))
                except Exception:
                    pass
            else:
                member_lists = self.helper.readlist_file(member_list)
                for member in member_lists:
                    user = await self.Tg.get_entity(member)
                    await self.Tg(
                        InviteToChannelRequest(channel=MyChannel, users=[user])
                    )
                    sleep(randrange(1, 3))
            return True
        except Exception:
            logging.error("Error : \n" + traceback.format_exc())
            return False
        finally:
            await self.Tg.disconnect()

    async def fetch_all_group_message(
        self,
        mode="new",
        max_date=None,
        main_channel: str=None,
        target_channel: str=None,
    ):
        try:
            Peer = None
            md5Channel = ""
            isOneChannel = False
            if self.Tg == None:
                await self.Connected()  # Ensure connection
            if self.Tg.is_connected():
                if main_channel == "":
                    isOneChannel = False
                else:
                    md5Channel = hashlib.md5(main_channel.encode())
                    isOneChannel = True

                dialog_list = await self.Tg.get_dialogs()

                if not target_channel is None:
                    Peer = await self.Tg.get_input_entity(target_channel)

                for dialog in dialog_list:
                    if isOneChannel:
                        if (
                            hashlib.md5(dialog.title.encode()).digest()
                            != md5Channel.digest()
                        ):
                            continue

                    entity = await self.Tg.get_entity(dialog.id)
                    try:
                        if (
                            isinstance(entity, telethon.tl.types.Channel)
                            and dialog.is_group
                        ):
                            self.fetch_channel(entity, dialog.is_group)

                            if mode == "New":
                                max_message_id = (
                                    self.database.get_max_message_id_of_chat(entity.id)
                                    or 0
                                )
                                msg_iter = self.Tg.iter_messages(
                                    entity.id, min_id=max_message_id
                                )
                            elif mode == "Old":
                                min_message_id = (
                                    self.database.get_min_message_id_of_chat(entity.id)
                                    or 2147483647
                                )
                                msg_iter = self.Tg.iter_messages(
                                    entity.id, max_id=min_message_id
                                )
                            else:
                                msg_iter = self.Tg.iter_messages(entity.id)

                            async for msg in msg_iter:
                                if not max_date is None:
                                    maxdate = msg.date.strftime("%d/%m/%Y")
                                    if maxdate >= max_date:
                                        await self.fetch_message(msg, Peer)
                                    else:
                                        break
                                else:
                                    await self.fetch_message(msg, Peer)
                            # Copy Message to Channel
                            pass

                    except Exception:
                        logging.error("Error : \n" + traceback.format_exc())
        except Exception:
            logging.error("Error : \n" + traceback.format_exc())
        finally:
            await self.Tg.disconnect()

    def fetch_channel(self, entity, is_group):
        """
        Process and fetch a channel
        :param msg:
        :return:
        """
        item = {
            "id": entity.id,
            "title": entity.title,
            "username": entity.username,
            "access_hash": entity.access_hash,
            "is_group": is_group,
            "mega_group": entity.megagroup,
            "giga_group": entity.gigagroup,
            "category": self.category,
        }
        self.helper.UpDateOutput(f"Channel Name : {item['title']}")
        self.database.process_channel(item)

    async def fetch_message(self, msg, send_to_target=None):
        """
        Process and fetch a message
        :param msg:
        :return:
        """
        if msg.media and isinstance(msg.media, telethon.tl.types.MessageMediaPhoto):
            # Download image
            media_path = await msg.download_media(
                "./Output/media/group_{}/{}_{}_{}".format(
                    msg.chat.id, msg.chat.id, msg.from_id, msg.id
                )
            )
            media_file = os.path.basename(media_path)
        elif (
            msg.media
            and isinstance(msg.media, telethon.tl.types.MessageMediaDocument)
            and msg.media.document.mime_type in ["audio/ogg"]
        ):
            # Download voice
            media_path = await msg.download_media(
                "./Output/media/group_{}/{}_{}_{}".format(
                    msg.chat.id, msg.chat.id, msg.from_id, msg.id
                )
            )
            media_file = os.path.basename(media_path)
        else:
            media_file = None
            if not msg.message:
                return
        member = msg.sender
        user = {
            "id": member.id,
            "first_name": unicodedata.normalize(
                "NFKC", getattr(member, "first_name", "Unknown") or "Unknown"
            ),
            "last_name": unicodedata.normalize(
                "NFKC", getattr(member, "last_name", "Unknown") or "Unknown"
            ),
            "username": unicodedata.normalize(
                "NFKC", getattr(member, "username", "Unknown") or "Unknown"
            ),
            "phone": getattr(member, "phone", "Unknown"),
            "last_active": "Unknown",
            "category": self.category,
        }
        self.database.write_to_database(TABLE_NAME, user)

        if len(msg.message) > 1:
            gitem = {
                "id": getattr(msg, "id", 0),  # Message id of current chat
                "chat_id": msg.chat.id,  # ID of current chat
                "message": unicodedata.normalize(
                    "NFKC", getattr(msg, "message", " ")
                ),  # message content
                "date": msg.date.strftime("%d/%m/%Y %H:%M:%S"),
                "from_id": member.id,  # The ID of the user who sent this message
                "is_reply": msg.is_reply,  # True if the message is a reply to some other
                "reply_to_msg_id": msg.reply_to_msg_id,  # The ID to which this message is replying to, if any
                "is_channel": msg.is_channel,
                "is_group": msg.is_group,
                "media_file": media_file,
                "category": self.category,
            }

            self.helper.UpDateOutput("Message: " + gitem["message"])
            self.database.process_message(gitem)

            if not send_to_target is None:
                await self.Tg(SendMessageRequest(send_to_target, gitem["message"]))

    async def send_message_without_block(
        self,
        message: str,
        file_send: str=None,
        file_list: str=None,
        use_AI: bool=False,
    ):
        if file_list:
            members = self.helper.readlist_file(file_list)
        else:
            members = self.database.read_from_database(
                TABLE_NAME, {"category": self.category}
            )
        if self.helper.is_file_path(message):
            message = self.helper.read_file_as_text(message)
        try:
            if self.Tg == None:
                await self.Connected()  # Ensure connection
            if self.Tg.is_connected():
                if use_AI:
                    Compan_ID = str(uuid.uuid4())
                    self.helper.UpDateOutput(f"Compan ID {Compan_ID}")
                    self.helper.UpDateOutput("Run AI...")
                    user_message = self.helper.AI_Command(
                        message=message,
                        withCommand=True,
                        driver=None,
                        settings=self.settings,
                    )
                    for msg in user_message:
                        msg = msg.split(":", 1)[1].strip()
                        self.database.save_msg_history(Compan_ID, msg, "telegram")
                for user in members:
                    try:
                        if not user is None:
                            if user["username"] == "Unknown":
                                Peer = await self.Tg.get_entity(int(user["id"]))
                                # Peer = await self.Tg.get_participants(int(user['id']))
                            else:
                                Peer = await self.Tg.get_entity(user["username"])
                            if use_AI:
                                user_message = self.database.get_msg_history(Compan_ID)
                                if len(user_message) > 0:
                                    send_message = user_message[
                                        randrange(0, len(user_message))
                                    ]["message"]
                                else:
                                    send_message = message
                            else:
                                send_message = message

                            if send_message == "":
                                send_message = message
                            self.helper.UpDateOutput(f"Message: {send_message}")

                            if not send_message is None and file_send is None:
                                await self.send_to_member(
                                    Peer.id, send_message, mode="text"
                                )
                            elif send_message is None and not file_send is None:
                                await self.send_to_member(
                                    Peer.id, file_send=file_send, mode="file"
                                )
                            elif not send_message is None and not file_send is None:
                                await self.send_to_member(
                                    Peer.id,
                                    text_message=send_message,
                                    file_send=file_send,
                                    mode="both",
                                )
                            else:
                                return

                            self.database.save_msg_or_post(
                                user=Peer.username,
                                message=send_message,
                                source="Telegram",
                            )
                        sleep(randrange(1, 5))
                    except Exception:
                        continue
        except Exception:
            self.helper.UpDateOutput("Error Can not Get User, Please read log message")
            logging.error("Error : \n" + traceback.format_exc())
        finally:
            await self.Tg.disconnect()
