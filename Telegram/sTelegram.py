import asyncio
import hashlib
import logging
import os
import sys
import time
import traceback
import unicodedata
from random import randrange

import telethon
from googletrans import Translator
from langdetect import detect
from PySide6.QtWidgets import QInputDialog, QLineEdit, QListView, QMessageBox
from telethon import TelegramClient, functions, types
from telethon.errors.rpcerrorlist import UsernameInvalidError
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.messages import SendMediaRequest, SendMessageRequest

from utils.helper import helper

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

TABLE_NAME = "Telegram"
TABLE_NAME_CHANNEL = "channel"
TABLE_NAME_MESSAGES = "message"
TABLE_COLLECTION = "import_data"


class sTelegram:

    def __init__(
        self,
        settings=None,
        database=None,
        category=None,
        output: QListView = None,
        needReset: bool = False,
    ):
        self.settings = settings
        if needReset:
            api_id, api_hash, phone_number, session_name = (
                self.settings.value("tg_api_id"),
                self.settings.value("tg_api_hash"),
                self.settings.value("tg_phone"),
                "Sessions/teleSession",
            )
            self.api_id = api_id
            self.api_hash = api_hash
            self.phone_number = phone_number
            self.session_name = session_name
            self.Tg = None
            asyncio.run(self.Connected())
        else:
            self.helper = helper(output)
            self.database = database
            self.database.create_table(TABLE_NAME)
            self.database.create_table(TABLE_NAME_CHANNEL)
            self.database.create_table(TABLE_NAME_MESSAGES)
            self.category = category
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
        except telethon.errors.rpcerrorlist.PhoneNumberInvalidError:
            QMessageBox.warning(
                self,
                "Error",
                "Phone Number Invalid",
                QMessageBox.StandardButton.Ok,
            )
        except Exception:
            logging.error("Error : \n" + traceback.format_exc())
            await self.Tg.disconnect()
            return None

    async def get_group_members(self, filelist):
        try:
            Number_Of_Group = 0
            await self.Connected()
            if self.Tg.is_connected():
                for group in filelist:
                    if Number_Of_Group <= 3:
                        self.helper.UpDateOutput(f"Open Group {group}")
                        members = await self.Tg.get_participants(group, aggressive=True)
                        self.helper.UpDateOutput(f"Get Members from {group}")
                        Number_Of_Group += 1
                    else:
                        Number_Of_Group = 0
                        seconds = randrange(300, 1000)
                        self.helper.UpDateOutput(
                            f"-: Hold from {seconds} seconds and Back to Work :-"
                        )
                        asyncio.sleep(seconds)
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
                                if not self.database.search_by_column(
                                    TABLE_NAME, "id", member.id
                                ):
                                    if self.database.write_to_database(
                                        TABLE_NAME, member_data
                                    ):
                                        self.helper.UpDateOutput(
                                            f"Add to database user {member_data["first_name"] or member_data["username"]}"
                                        )
                                    else:
                                        self.helper.UpDateOutput(
                                            f"User Exist in Database : {member_data["first_name"] or member_data["username"]}"
                                        )
                                        continue
                                else:
                                    continue

                    except Exception:
                        logging.error("Error : \n" + traceback.format_exc())
                        continue
                    seconds = randrange(10, 100)
                    # minutes = math.floor(seconds / 60)
                    self.helper.UpDateOutput(
                        f"Finished Group {group} and i will hold {seconds} seconds."
                    )
                    asyncio.sleep(seconds)
                return True
        except Exception:
            logging.error("Error : \n" + traceback.format_exc())
            return False
        finally:
            await self.Tg.disconnect()

    async def send_to_member(
        self,
        member_id: int,
        text_message: str = None,
        file_send: str = None,
        mode: str = "text",
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

    async def add_members_to_channel(self, channel: str, member_list: str = None):
        """
        Adds multiple members to a channel or group.

        :param channel: The channel or group entity (or its username) to which members will be added.
        :param member_ids: A list of user IDs or usernames to add.
        """
        MyChannel = None
        await self.Connected()
        try:
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
                members = self.database.read_from_database(
                    TABLE_NAME, {"category": self.category}
                )
                if not members:
                    members = self.database.read_from_database(
                        TABLE_COLLECTION, {"category": self.category}
                    )

            await self._memeber_add_implement(MyChannel=MyChannel, UserList=members)
        except Exception:
            logging.error("Error : \n" + traceback.format_exc())
            return False
        finally:
            await self.Tg.disconnect()

    async def fetch_all_group_message(
        self,
        mode: str = "new",
        max_date=None,
        main_channel: str = None,
        target_channel: str = None,
        list1: list = None,
        list2: list = None,
    ):
        try:
            Peer = None
            md5Channel = ""
            if self.Tg == None:
                await self.Connected()  # Ensure connection
            if self.Tg.is_connected():
                dialog_list = await self.Tg.get_dialogs()
                if main_channel == "":
                    self.helper.UpDateOutput("Build Telegram Channel Database...")
                    for entity in dialog_list:
                        if entity.is_channel or entity.is_group:
                            if main_channel == "":
                                self.helper.UpDateOutput(
                                    f"The Main Channel is {entity.title}"
                                )
                                main_channel = entity.title
                            if not self.database.search_by_column(
                                TABLE_NAME_CHANNEL, "id", entity.id
                            ):
                                item = {
                                    "id": entity.id,
                                    "title": entity.title,
                                    "is_group": entity.is_group,
                                    "is_channel": entity.is_channel,
                                    "username": unicodedata.normalize(
                                        "NFKC",
                                        getattr(entity, "username", "name")
                                        or "Unknown",
                                    ),
                                    "access_hash": unicodedata.normalize(
                                        "NFKC",
                                        getattr(entity, "access_hash", "Unknown")
                                        or "Unknown",
                                    ),
                                    "mega_group": unicodedata.normalize(
                                        "NFKC",
                                        getattr(entity, "megagroup", "false")
                                        or "false",
                                    ),
                                    "giga_group": unicodedata.normalize(
                                        "NFKC",
                                        getattr(entity, "gigagroup", "false")
                                        or "false",
                                    ),
                                    "category": self.category,
                                }
                                self.helper.UpDateOutput(f"Add Channel {entity.title}")
                                self.database.write_to_database(
                                    TABLE_NAME_CHANNEL, item
                                )

                if not target_channel is None:
                    Peer = await self.Tg.get_input_entity(target_channel)
                    self.helper.UpDateOutput(f"Target Channel ID {Peer.channel_id}")

                entity = None
                for dialog in dialog_list:
                    if dialog.title == main_channel:
                        entity = await self.Tg.get_entity(dialog.id)

                try:
                    if not entity is None and isinstance(
                        entity, telethon.tl.types.Channel
                    ):
                        self.helper.UpDateOutput(f"Fetching Channel and Messages...")
                        self.fetch_channel(entity, dialog.is_group)
                        if mode == "new":
                            max_message_id = (
                                self.database.get_max_message_id_of_chat(entity.id) or 0
                            )
                            msg_iter = self.Tg.iter_messages(
                                entity.id, min_id=max_message_id
                            )
                        elif mode == "old":
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
                                if mode == "new":
                                    if maxdate >= max_date:
                                        await self.fetch_message(
                                            msg, Peer, list1, list2
                                        )
                                    else:
                                        break
                                elif mode == "old":
                                    if maxdate <= max_date:
                                        await self.fetch_message(
                                            msg, Peer, list1, list2
                                        )
                                    else:
                                        break
                            else:
                                await self.fetch_message(msg, Peer, list1, list2)
                    else:
                        self.helper.UpDateOutput(
                            f"Can't Parsing {entity.title}, i'll Close Telegram Module..."
                        )
                        return False
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

    async def fetch_message(self, msg, send_to_target=None, list1=None, list2=None):
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
        else:
            media_path = None

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
            Message = unicodedata.normalize("NFKC", getattr(msg, "message", ""))
            if not list1 is None and not list2 is None and Message != "":
                for part in list1:
                    if part in Message:
                        index = list1.index(part)
                        Message = Message.replace(part, list2[index])

                words = Message.split()
                for i, word in enumerate(words):
                    if word in list1:
                        index = list1.index(word)
                        if index < len(list2):
                            words[i] = list2[index]
                Message = " ".join(words)

            gitem = {
                "id": getattr(msg, "id", 0),  # Message id of current chat
                "chat_id": msg.chat.id,  # ID of current chat
                "message": Message,
                "date": msg.date.strftime("%d/%m/%Y %H:%M:%S"),
                "from_id": member.id,  # The ID of the user who sent this message
                "is_reply": msg.is_reply,  # True if the message is a reply to some other
                "reply_to_msg_id": msg.reply_to_msg_id,  # The ID to which this message is replying to, if any
                "is_channel": msg.is_channel,
                "is_group": msg.is_group,
                "media_file": media_path,
                "category": self.category,
            }

            self.helper.UpDateOutput(f"Message: {Message}")
            self.database.process_message(gitem)
            try:
                if not send_to_target is None:
                    if not media_path is None:
                        await self.Tg(
                            SendMediaRequest(
                                peer=send_to_target.channel_id,
                                media=types.InputMediaUploadedPhoto(
                                    file=await self.Tg.upload_file(
                                        media_path
                                    )  # Upload the media file
                                ),
                                message=Message,
                            )
                        )
                    else:
                        await self.Tg(
                            SendMessageRequest(
                                peer=send_to_target,
                                message=Message,
                            )
                        )
            except:
                logging.error("Error : \n" + traceback.format_exc())
                self.helper.UpDateOutput(f"Error can not send to your target.")

    async def telegram_send_message(
        self,
        message: str = None,
        file_send: str = None,
        file_list: str = None,
        slogin: str = None,
        compan: str = None,
        msg_img: bool = False,
        translat: bool = False,
    ):
        if file_send == "":
            file_send = None

        if file_list:
            members = file_list
        else:
            members = self.database.read_from_database(
                TABLE_NAME, {"category": self.category}
            )
        if not message is None and self.helper.is_file_path(message):
            message = self.helper.read_file_as_text(message)

        try:
            if self.Tg == None:
                await self.Connected()  # Ensure connection
            if self.Tg.is_connected():

                if compan:
                    self.helper.UpDateOutput("Waitnig AI Results")
                    loop_time = 0
                    message_list = []
                    while len(message_list) == 0:
                        if loop_time >= 50:
                            if not message is None:
                                send_message = message
                            else:
                                return False
                            break
                        else:
                            loop_time += 1
                        message_list = self.database.get_msg_history(compan)
                        await asyncio.sleep(randrange(4, 10))

                for user in members:
                    try:
                        if not user is None:
                            if user["username"] == "Unknown":
                                Peer = await self.Tg.get_entity(int(user["id"]))
                                # Peer = await self.Tg.get_participants(int(user['id']))
                            else:
                                Peer = await self.Tg.get_entity(user["username"])
                            if Peer.deleted:
                                continue

                            if Peer.is_self:
                                continue

                            self.helper.UpDateOutput(
                                f"Send To: {Peer.first_name or Peer.username }"
                            )

                            if len(message_list) == 0:
                                send_message = message
                            else:
                                msg = message_list[randrange(0, len(message_list))][
                                    "message"
                                ]
                                if slogin:
                                    _slogin = slogin.split("|")
                                    if int(_slogin[0]) == 0:
                                        send_message = f"{_slogin[1]}\n\n{msg}"
                                    else:
                                        send_message = f"{msg}\n\n{_slogin[1]}"
                                else:
                                    send_message = msg
                            if translat:
                                async with Translator(timeout=20000) as translator:
                                    if Peer.lang_code:
                                        lang = Peer.lang_code
                                    else:
                                        lang = detect(Peer.first_name or Peer.username)

                                    result = await translator.translate(
                                        send_message,
                                        dest=lang,
                                    )
                                    send_message = result.text

                            self.helper.UpDateOutput(f"Message: {send_message}")

                            if not send_message is None and file_send is None:
                                await self.send_to_member(
                                    Peer.id, send_message, mode="text"
                                )
                            elif send_message is None and not file_send is None:
                                await self.send_to_member(
                                    Peer.id, file_send=file_send, mode="file"
                                )
                            elif (
                                not send_message is None
                                and not file_send is None
                                and msg_img
                            ):
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
                        await asyncio.sleep(randrange(5, 15))
                    except Exception:
                        logging.error("Error : \n" + traceback.format_exc())
                        continue
        except Exception:
            self.helper.UpDateOutput("Error Can not Get User, Please read log message")
            logging.error("Error : \n" + traceback.format_exc())
        finally:
            await self.Tg.disconnect()

    async def _memeber_add_implement(self, MyChannel, UserList):
        UserLists = []
        for member in UserList:
            try:
                if not member.get("username") is None:
                    user = await self.Tg.get_entity(member.get("username"))
                else:
                    user = await self.Tg.get_entity(int(member.get("account")))
                try:
                    participant = await self.Tg(
                        functions.channels.GetParticipantRequest(MyChannel, user.id)
                    )
                    self.helper.UpDateOutput(
                        f"User Exist {user.username} on {MyChannel.title}"
                    )
                    continue
                except Exception:
                    UserLists.append(user)
                    self.helper.UpDateOutput(
                        f"Add User {user.username} to {MyChannel.title}"
                    )
                if len(UserLists) >= 20:
                    if MyChannel.is_channel:
                        await self.Tg(
                            InviteToChannelRequest(channel=MyChannel, users=UserLists)
                        )
                        self.helper.UpDateOutput("Send Invitations for your Channel...")
                    else:
                        for user in UserLists:
                            await self.Tg(
                                functions.messages.AddChatUserRequest(
                                    chat_id=MyChannel.id,
                                    user_id=user.id,
                                )
                            )
                            self.helper.UpDateOutput(
                                "Send Invitations for your Group..."
                            )
                            asyncio.sleep(3)
                    UserLists = []
                    self.helper.UpDateOutput(
                        "I will Make Super Freezing Now DON'T CLOSE ME..."
                    )
                    time.sleep(randrange(30, 60))
            except telethon.errors.ChatAdminRequiredError:
                self.helper.UpDateOutput(
                    f"Chat admin privileges are required to do that in the specified chat (for example, to send a message in a channel which is not yours), or invalid permissions used for the channel or group."
                )
                return False
            except telethon.errors.ChatIdInvalidError:
                self.helper.UpDateOutput(f"Group ID not exisit")
                return False
            except ValueError:
                self.helper.UpDateOutput(f'Not fund {member.get("username")}')
                continue
            except telethon.errors.rpcerrorlist.UsernameInvalidError:
                self.helper.UpDateOutput(f'Not fund {member.get("username")}')
                continue
            except telethon.errors.rpcerrorlist.FloodWaitError:
                self.helper.UpDateOutput(
                    "I will Make Super Freezing Now DON'T CLOSE ME... (45982 sec)"
                )
                time.sleep(45982)
                continue
            except telethon.errors.rpcerrorlist.PeerFloodError:
                self.helper.UpDateOutput(f"========== We are must waiting ==========")
                asyncio.sleep(1800)
                continue
