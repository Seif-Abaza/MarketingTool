import datetime
import hashlib
import json
import logging
import os
import sys
import time

from flask import Flask, jsonify, request, send_file
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from nacl.public import (  # Replace with your actual crypto library
    Box,
    PrivateKey,
    PublicKey,
)

# Load environment variables

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../utils/")))
from DBManager import DBManager

PORT = 23004
# IP_ADDRESS = "127.0.0.1"
IP_ADDRESS = "172.86.114.80"
SMS_APIKEY = "bd3c71fed30f5453Ac6421e78Ae4ff10"
OLD_VERSION = "1.0.0"
CURRENT_VERSION = "1.0.0"
DOWNLOAD_PATH = os.path.join(os.getcwd(), "dist/")
SERVER_IP = f"http://{IP_ADDRESS}:{PORT}"

VERSIONS = {
    "windows": {
        "version": CURRENT_VERSION,
        "download_url": f"{IP_ADDRESS}/download/marketingtools_{CURRENT_VERSION}.exe",
        "patch_url": f"{IP_ADDRESS}/patch/windows_{OLD_VERSION}_to_{CURRENT_VERSION}.patch",
        "sha256": "abcd1234...",  # ضع هنا التوقيع الفعلي للملف
    },
    "linux": {
        "version": CURRENT_VERSION,
        "download_url": f"{IP_ADDRESS}/download/marketingtools_{CURRENT_VERSION}.AppImage",
        "patch_url": f"{IP_ADDRESS}/patch/linux_{OLD_VERSION}_to_{CURRENT_VERSION}.patch",
        "sha256": "2f1550a4905199d3e9f916b1d4f26af453a228eb6bbd924a2c0e0e2f9cf6b00e",
    },
    "macos": {
        "version": CURRENT_VERSION,
        "download_url": f"{IP_ADDRESS}/download/marketingtools_{CURRENT_VERSION}.dmg",
        "patch_url": f"{IP_ADDRESS}/patch/macos_{OLD_VERSION}_to_{CURRENT_VERSION}.patch",
        "sha256": "lmno999...",
    },
}

TABLE_ADMIN = "admin_accounts"
TABLE_SMS_SERVICE = "sms_service"

IS_DEBUG = bool(os.getenv("MT_DEBUG", False))

if IS_DEBUG:
    logging.basicConfig(filename="Log/server_debug.log", level=logging.WARNING)
else:
    logging.basicConfig(filename="Log/server_info.log", level=logging.INFO)


class MarketingToolsServer:
    def __init__(self):
        # Logging and initialization
        if IS_DEBUG:
            logging.warning("Open Database in Debug Mode")
            logging.warning("Starting Server in Debug Mode")
        else:
            logging.warning("Open Database online")
            logging.warning("Starting Server online")

        self.DateNow = str(datetime.date.today().strftime("%d/%m/%Y"))
        self.TimeNow = int(time.time())
        self.logger = logging.getLogger(__name__)
        self.server_private_key = PrivateKey.generate()
        self.server_public_key = self.server_private_key.public_key

        # Initialize the database
        self.database = DBManager(database_name="MarketingTools", isServer=True)

        # Initialize the Flask app
        self.app = Flask(__name__)

        # Initialize the Limiter
        self.limiter = Limiter(
            app=self.app,  # Pass the Flask app object
            key_func=get_remote_address,  # Use the client's IP address for rate limiting
            storage_uri="mongodb://localhost:27017",
            strategy="fixed-window",  # Use "fixed-window" or "moving-window" strategy
        )

        # Initialize database tables and data
        if self.database:
            logging.warning("======Database is Run Now======")
            self.database.create_table(TABLE_ADMIN)
            if self.database.create_table(TABLE_SMS_SERVICE):
                with open(
                    os.path.join(os.path.dirname(__file__), "services.json"),
                    "r",
                    encoding="utf-8",
                ) as file:
                    ServicesData = json.load(file)
                    for item in ServicesData:
                        self.database.write_to_database(TABLE_SMS_SERVICE, item)

        # Register routes
        self.register_routes()

    def register_routes(self):
        """Register all routes with the Flask app."""
        self.app.add_url_rule("/", view_func=self.home)
        self.app.add_url_rule(
            "/get_public_key", view_func=self.get_public_key, methods=["GET"]
        )
        self.app.add_url_rule(
            "/verify_data", view_func=self.verify_data, methods=["POST"]
        )
        self.app.add_url_rule(
            "/get_account", view_func=self.get_account, methods=["POST"]
        )
        self.app.add_url_rule(
            "/get_sms_services", view_func=self.get_sms_services, methods=["GET"]
        )
        self.app.add_url_rule(
            "/get_sms_name_by_code/<sms_code>",
            view_func=self.get_service_name_by_code,
            methods=["GET"],
        )
        self.app.add_url_rule(
            "/check_update", view_func=self.check_update, methods=["GET"]
        )
        self.app.add_url_rule(
            "/download/<application_os>", view_func=self.download_app, methods=["GET"]
        )
        self.app.add_url_rule(
            "/patch/<application_os>", view_func=self.patch_app, methods=["GET"]
        )

    def validate_input(self, data, required_fields):
        """Validate input data for required fields."""
        for field in required_fields:
            if field not in data:
                raise ValueError(f"Missing required field: {field}")

    def home(self):
        """Home route."""
        return "MarketMiner"

    def get_public_key(self):
        """Return the server's public key."""
        if IS_DEBUG:
            self.logger.warning("Return the Server Public Key")
        return jsonify({"public_key": self.server_public_key.encode().hex()})

    def verify_data(self):
        """Verify encrypted data from the client."""
        try:
            data = request.json
            self.validate_input(data, ["encrypted_data", "client_public_key"])
            if IS_DEBUG:
                self.logger.warning(f"Data is {data}")

            encrypted_data = bytes.fromhex(data.get("encrypted_data"))
            client_public_key = bytes.fromhex(data.get("client_public_key"))
            client_public_key = PublicKey(client_public_key)

            box = Box(self.server_private_key, client_public_key)
            decrypted_data = box.decrypt(encrypted_data).decode()
            if IS_DEBUG:
                self.logger.warning(f"Decryption is Done and it's {decrypted_data}")

            if decrypted_data:
                data_client = decrypted_data.split(",")
                name_user = data_client[0].split(":")[1]
                phone_user = data_client[1].split(":")[1]
                mail_user = data_client[2].split(":")[1]
                txid = data_client[3].split(":")[1]
                is_user = bool(data_client[4].split(":")[1])
                computer_hash = data_client[5].split(":")[1]
                logging.warning(f"Computer {computer_hash}")

                if is_user:
                    logging.warning(f"New User {computer_hash}")
                    user_hash = hashlib.md5(
                        f"name:{name_user},phone:{phone_user},mail:{mail_user},computer_hash: {str(computer_hash)}".encode(
                            "utf-8"
                        )
                    ).hexdigest()
                    logging.warning(f"User Hash {user_hash}")
                    user_account = self.database.search_by_columns(
                        TABLE_ADMIN,
                        "key",
                        str(user_hash),
                        "computer_hash",
                        str(computer_hash),
                        operation="or",
                    )
                    logging.warning(f"User Data {user_account}")

                    if user_account:
                        user_account = user_account[0]
                    else:
                        _sm_allow = ["telegram", "whatsapp", "facebook"]
                        _sms_allow = self.get_service_code_by_name(
                            self._internal_sms_services()
                        )
                        sm_allow = [str(item) for item in _sm_allow]
                        d_coma = ","
                        self.database.write_to_database(
                            TABLE_ADMIN,
                            {
                                "name": name_user,
                                "phone": phone_user,
                                "mail": mail_user,
                                "txid": txid,
                                "computer_hash": computer_hash,
                                "key": str(user_hash),
                                "is_active": False,
                                "can_access_numbers": False,
                                "can_export_data": False,
                                "can_use_database_offline": False,
                                "can_use_database_online": True,
                                "can_network": False,
                                "can_send": True,
                                "can_scrip": True,
                                "can_use_ai": False,
                                "can_use": d_coma.join(sm_allow),
                                "can_sms": False,
                                "can_sms_service": d_coma.join(_sms_allow),
                                "can_tmp_mail": False,
                                "can_super_fast": False,
                                "date": self.DateNow,
                                "time": self.TimeNow,
                            },
                        )
                        if IS_DEBUG:
                            self.logger.warning("Server Will Answer with 600")
                        return (
                            jsonify(
                                {
                                    "success": True,
                                    "msg": "Please Connect with Provider",
                                    "hash": str(user_hash),
                                }
                            ),
                            600,
                        )
                    return jsonify({"success": False, "error": "Invalid data"}), 400

        except Exception as e:
            self.logger.error(f"Error in verify_data: {e}")
            return jsonify({"success": False, "error": str(e)}), 500

    def get_account(self):
        """Get account details."""
        try:
            data = request.json
            self.validate_input(data, ["hash", "com_hash"])
            if IS_DEBUG:
                self.logger.warning(f"Get Account Data with")
            user_hash = data.get("hash")
            computer_hash = data.get("com_hash")
            if IS_DEBUG:
                self.logger.warning(
                    f"User Key {user_hash} Computer Hash {computer_hash} and i will Search by this OR this."
                )
            user_account = self.database.search_by_columns(
                TABLE_ADMIN,
                "key",
                str(user_hash),
                "computer_hash",
                str(computer_hash),
                operation="or",
            )
            if user_account:
                user_account = user_account[0]
                if IS_DEBUG:
                    self.logger.warning(f"Find Account")
                if user_hash is None:
                    user_hash = hashlib.md5(
                        f"name:{user_account['name']},phone:{user_account['phone']},mail:{user_account['mail']},computer_hash: {str(computer_hash)}".encode(
                            "utf-8"
                        )
                    ).hexdigest()
                    if user_hash == user_account["key"]:
                        return (
                            jsonify(
                                {
                                    "success": True,
                                    "msg": "Please Connect with Provider By WhatsApp +201032231755",
                                }
                            ),
                            600,
                        )
            else:
                if IS_DEBUG:
                    self.logger.warning(
                        f"Not Find Account With this Data and i will Return With Code 420"
                    )
                return jsonify({"success": False, "error": "Not Registered"}), 420

            if user_account["is_active"]:
                if IS_DEBUG:
                    self.logger.warning(f"Find Account and it's Active and Ready")
                allow_user = {
                    "can_access_numbers": user_account["can_access_numbers"],
                    "can_export_data": user_account["can_export_data"],
                    "can_use_database_offline": user_account[
                        "can_use_database_offline"
                    ],
                    "can_use_database_online": user_account["can_use_database_online"],
                    "can_network": user_account["can_network"],
                    "can_send": user_account["can_send"],
                    "can_scrip": user_account["can_scrip"],
                    "can_use_ai": user_account["can_use_ai"],
                    "can_use": user_account["can_use"],
                    "can_sms": user_account["can_sms"],
                    "can_sms_service": user_account["can_sms_service"],
                    "can_tmp_mail": user_account["can_tmp_mail"],
                    "can_super_fast": user_account["can_super_fast"],
                    "sms_key": SMS_APIKEY,
                }
                return jsonify(
                    {
                        "success": True,
                        "user_name": user_account["name"],
                        "user_allow": allow_user,
                    }
                )
            else:
                if IS_DEBUG:
                    self.logger.warning(
                        f"Find Account But it's Not Active , Return With Code 600"
                    )
                return (
                    jsonify({"success": True, "msg": "Please Connect with Provider"}),
                    600,
                )

        except Exception as e:
            self.logger.error(f"Error in get_account: {e}")
            return jsonify({"success": False, "error": "Not Registered"}), 500

    def get_sms_services(self):
        """Get SMS services."""
        try:
            services = []  # Renamed to avoid shadowing the loop variable
            all_services = self.database.search_by_column(
                TABLE_SMS_SERVICE, "allow", True
            )
            if all_services:
                for service in all_services:
                    services.append(
                        {"name": service["name"], "code": service["code"]}
                    )  # Fixed variable name
                return jsonify({"success": True, "data": services, "error": ""}), 200
            else:
                return jsonify({"success": False, "message": "No services found"}), 500
        except Exception as err:
            # Log the error for debugging
            self.logger.error(f"Error in get_sms_services: {err}")
            # Convert the exception to a string before returning it
            return jsonify({"success": False, "message": str(err)}), 500

    def _get_sms_service_by_name(self, list_of_name=None):
        list_of_codes = []
        if not list_of_name is None:
            for item in list_of_name:
                list_of_codes.append(
                    self.database.search_by_column(TABLE_SMS_SERVICE, "name", item)[
                        "code"
                    ]
                )
        return list_of_codes

    def _internal_sms_services(self):
        """Get SMS services."""
        try:
            services = []  # Renamed to avoid shadowing the loop variable
            all_services = self.database.search_by_column(
                TABLE_SMS_SERVICE, "allow", True
            )
            if all_services:
                for service in all_services:
                    services.append(
                        {"name": service["name"], "code": service["code"]}
                    )  # Fixed variable name
                return services
            else:
                return []
        except Exception as err:
            # Log the error for debugging
            self.logger.error(f"Error in get_sms_services: {err}")
            return []

    def get_service_code_by_name(self, list_of_name=None):
        list_of_codes = []
        if not list_of_name is None:
            for item in list_of_name:
                iname = self.database.search_by_column(
                    TABLE_SMS_SERVICE, "name", item["name"]
                )
                if iname[0]:
                    list_of_codes.append(iname[0]["code"])
        return list_of_codes

    def get_service_name_by_code(self, sms_code=None):
        if not sms_code is None:
            iname = self.database.search_by_column(TABLE_SMS_SERVICE, "code", sms_code)
            if iname[0]:
                name_service = iname[0]["name"]
            return jsonify({"success": True, "data": name_service, "error": ""}), 200
        else:
            return jsonify({"success": False, "message": "No services found"}), 500

    def check_update(self):
        """Check for updates."""
        os_type = request.args.get("os", "").lower()
        current_version = request.args.get("version", "")
        if IS_DEBUG:
            self.logger.warning(
                f"Check Update with this Information OS:{os_type} and Version:{current_version}"
            )

        if os_type not in VERSIONS:
            return jsonify({"error": "Unsupported OS"}), 400

        latest_version = VERSIONS[os_type]["version"]
        if current_version == latest_version:
            return jsonify({"status": "up-to-date"})

        return jsonify(
            {
                "latest_version": latest_version,
                "patch_url": VERSIONS[os_type]["patch_url"],
                "download_url": VERSIONS[os_type]["download_url"],
                "sha256": VERSIONS[os_type]["sha256"],
            }
        )

    def download_app(self, application_os):
        """Download the application."""
        if IS_DEBUG:
            self.logger.warning(f"Downloading New Version")
        download = f"{DOWNLOAD_PATH}{application_os}"
        logging.warning(f"Download Application {download}")
        return send_file(f"{download}", as_attachment=True)

    def patch_app(self, application_os):
        """Download the patch."""
        if IS_DEBUG:
            self.logger.warning(f"Downloading Patch Only")
        download = f"{DOWNLOAD_PATH}{application_os}"
        logging.warning(f"Patch Application {download}")
        return send_file(f"{download}", as_attachment=True)

    def run(self):
        """Run the Flask app."""
        self.logger.warning("Server is Working Now")
        self.app.run(host="0.0.0.0", port=PORT, debug=IS_DEBUG)


# Main entry point
if __name__ == "__main__":
    server = MarketingToolsServer()
    server.run()
