import datetime
import json
import logging
import os
import sys
import traceback

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import time
import uuid

import pymongo

from utils.systeminfo import hash_computer


class DBManager:
    ONLINE_DATABASE_IP = "172.86.114.80"
    ONLINE_DATABASE_PORT = "27018"
    ONLINE_DATABASE_USERNAME = "admin"
    ONLINE_DATABASE_PASSWORD = "SeifAbazaRedR00t!@"
    ONLINE_DATABASE_LINK = f"mongodb://{ONLINE_DATABASE_USERNAME}:{ONLINE_DATABASE_PASSWORD}{ONLINE_DATABASE_IP}:{ONLINE_DATABASE_PORT}/{ONLINE_DATABASE_USERNAME}"

    def __init__(
        self,
        host="localhost",
        port=27017,
        database_name: str = "Marketing",
        settings: str = None,
        isServer=False,
        isDebug=False,
    ):
        """
        Initialize MongoDB connection and create a database named 'MyDatabase' if it doesn't exist.
        """
        logging.getLogger("pymongo").setLevel(logging.WARNING)
        self.username = hash_computer()
        if not settings is None:
            self.settings = settings

        if isServer:
            self.client = pymongo.MongoClient(self.ONLINE_DATABASE_LINK)

        if isDebug:
            self.client = pymongo.MongoClient(host, port)

        self.db = self.client[database_name]

    def create_table(self, table_name):
        """
        Create a collection (table) if it doesn't exist.
        :param table_name: Name of the collection to create.
        """
        if table_name not in self.db.list_collection_names():
            self.db.create_collection(table_name)
            return True
        else:
            return False

    def update_in_database(self, table_name, query, update_data):
        """
        Update documents in the collection.
        :param table_name: Name of the collection to update.
        :param query: Dictionary specifying which document(s) to update.
        :param update_data: Dictionary of fields to update.
        :return: Boolean indicating whether an update occurred.
        """
        try:
            collection = self.db[table_name]

            # Ensure update_data is properly structured
            if not update_data:
                return False  # No update data provided
            query.update({"user": self.username})
            # Perform the update
            result = collection.update_many(query, {"$set": update_data})

            # Return True if at least one document was modified
            return result.modified_count > 0

        except Exception as e:
            print(
                f"Error updating database: {e} , Query: {query}, Update Data: {update_data}"
            )
            return False

    def write_to_database(self, table_name, data):
        """
        Write data to the collection after checking for duplicates.
        :param table_name: Name of the collection to write to.
        :param data: Dictionary or list of dictionaries to insert.
        """
        try:
            collection = self.db[table_name]

            # Check for duplicates
            if isinstance(data, list):  # Handle multiple documents
                LocalUser = []
                non_duplicate_data = []

                LocalUser["user"] = self.username
                data.append(LocalUser)

                for document in data:
                    if not collection.find_one(document):  # Check if document exists
                        non_duplicate_data.append(document)
                if non_duplicate_data:
                    collection.insert_many(non_duplicate_data)
                    return True
                else:
                    return False
            else:  # Handle single document
                data.update({"user": self.username})
                if not collection.find_one(data):  # Check if document exists
                    collection.insert_one(data)
                    return True
                else:
                    return False
        except Exception as e:
            print(f"Error writing to database: {e} , Data : {data}")
            return False

    def get_count_of_table(self, table_name, byDate: bool = False, Source: str = None):
        """
        Read documents from the collection.
        :param table_name: Name of the collection to read from.
        :param query: Optional query to filter documents.
        :return: List of documents.
        """
        try:
            query = {}
            query.update({"user": self.username})
            if byDate:
                DateNow = str(datetime.date.today().strftime("%d/%m/%Y"))
                query.update({"date": DateNow})

            if not Source is None:
                query.update({"source": Source})

            collection = self.db[table_name]
            documents = list(collection.find(query))
            return len(documents)
        except TimeoutError:
            return 0

    def read_from_database(self, table_name, query=None):
        """
        Read documents from the collection.
        :param table_name: Name of the collection to read from.
        :param query: Optional query to filter documents.
        :return: List of documents.
        """
        if query is None:
            query = {}
            query.update({"user": self.username})
        else:
            query.update({"user": self.username})

        collection = self.db[table_name]
        documents = list(collection.find(query))
        return documents

    def search_by_column(self, table_name, column_name, value):
        """
        Search for documents where a specific column matches a value.
        :param table_name: Name of the collection to search in.
        :param column_name: Name of the column to search.
        :param value: Value to match in the column.
        :return: List of matching documents.
        """
        collection = self.db[table_name]
        query = {column_name: value}
        query.update({"user": self.username})
        documents = list(collection.find(query))
        return documents

    def search_by_columns(
        self,
        table_name,
        column1,
        value1,
        column2=None,
        value2=None,
        operation: str = "and",
    ):
        """
        Search for documents where two specific columns match given values.
        :param table_name: Name of the collection to search in.
        :param column1: First column name to search.
        :param value1: Value for the first column.
        :param column2: Second column name to search.
        :param value2: Value for the second column.
        :return: List of matching documents.
        """
        collection = self.db[table_name]
        if operation == "and":
            query = {column1: value1, column2: value2}  # AND condition
        if operation == "or":
            query = {"$or": [{column1: value1}, {column2: value2}]}

        query.update({"user": self.username})
        documents = list(collection.find(query))
        return documents

    def search_in_all_columns(self, table_name, value):
        """
        Search for documents where any column matches a value.
        :param table_name: Name of the collection to search in.
        :param value: Value to search for in all columns.
        :return: List of matching documents.
        """
        collection = self.db[table_name]
        # Get all keys from the first document (if any)
        sample_document = collection.find_one()
        if sample_document:
            keys = sample_document.keys()
            query = {"$or": [{k: value} for k in keys]}
            query.update({"user": self.username})
            documents = list(collection.find(query))
            return documents
        else:
            return []

    def export_table_to_json(self, table_name, file_name):
        """
        Export the entire collection to a JSON file.
        :param table_name: Name of the collection to export.
        :param file_name: Name of the JSON file to export to.
        """
        collection = self.db[table_name]
        documents = list(collection.find())
        with open(file_name, "w") as file:
            json.dump(documents, file, default=str, indent=4)
        return True

    def select_column(self, table_name, column, where=None):
        collection = self.db[table_name]
        # Select only the "column_name" field (excluding _id)
        if where is None:
            result = collection.find(
                {},
                {
                    column: 1,
                    "_id": 0,
                    "user": self.username,
                },
            )
        else:
            result = collection.find(
                where,
                {
                    column: 1,
                    "_id": 0,
                    "user": self.username,
                },
            )
        # result = collection.find({}, {column: 1, "_id": 0, "user": self.username,})
        listColument = []
        for doc in result:
            try:
                listColument.append(doc[column])
            except Exception:
                continue

        listColument = filter(lambda v: v is not None, listColument)
        return list(set(listColument))

    def close_connection(self):
        """
        Close the MongoDB connection.
        """
        self.client.close()
        return True

    def get_max_message_id_of_chat(self, chat_id):
        try:
            result = self.db["message"].aggregate(
                [
                    {"user": self.username},
                    {"$match": {"chat_id": chat_id}},
                    {"$group": {"_id": None, "m": {"$max": "$message_id"}}},
                ]
            )
            # Extract the max message_id
            return next(result, {}).get("m", None)
        except:
            return 0

    def get_min_message_id_of_chat(self, chat_id):
        # Run aggregation query to find the minimum message_id
        try:
            result = self.db["message"].saggregate(
                [
                    {"user": self.username},
                    {"$match": {"chat_id": chat_id}},
                    {"$group": {"_id": None, "m": {"$min": "$message_id"}}},
                ]
            )
            # Extract the min message_id
            return next(result, {}).get("m", None)
        except:
            return 2147483647

    def process_value(self, value):
        """Process values before inserting into MongoDB."""
        if isinstance(value, bool):
            return value  # MongoDB supports boolean directly

        if isinstance(value, str):
            return "" if value == "None" else value.strip()

        if isinstance(value, datetime.datetime):
            return value + datetime.timedelta(hours=8)  # Convert UTC to UTC+8

        return value

    def save_msg_or_post(self, user, message, source):
        TableName = "total_msg_post"
        DateNow = str(datetime.date.today().strftime("%d/%m/%Y"))
        TimeNow = int(time.time())
        self.write_to_database(
            TableName,
            {
                "name": user,
                "message": message,
                "source": source,
                "date": DateNow,
                "time": TimeNow,
            },
        )

    def save_msg_history(self, compan_name, main_id, message, source):
        TableName = "message_history"
        DateNow = str(datetime.date.today().strftime("%d/%m/%Y"))
        TimeNow = int(time.time())
        self.write_to_database(
            TableName,
            {
                "name": compan_name,
                "minid": main_id,
                "id": str(uuid.uuid4()),
                "message": message,
                "source": source,
                "date": DateNow,
                "time": TimeNow,
            },
        )

    def get_msg_history(self, compan_name):
        TableName = "message_history"
        return self.read_from_database(TableName, {"name": compan_name})

    def get_channel(self, channel_id):
        """Check if a channel exists in the collection."""
        return self.search_by_column("channel", "id", channel_id)

    def save_channel(self, item):
        """Insert a new channel into the collection."""
        try:
            processed_item = {k: self.process_value(v) for k, v in item.items()}
            self.write_to_database("channel", processed_item)
        except Exception:
            logging.error("Error : \n" + traceback.format_exc())

    def update_channel(self, item):
        """Update an existing channel based on its ID."""
        try:
            item_id = item.pop("id", None)
            if not item_id:
                raise ValueError("Missing 'id' in item for update")

            update_fields = {k: self.process_value(v) for k, v in item.items()}
            self.update_in_database("channel", {"id": item_id}, update_fields)
        except Exception:
            logging.error("Error : \n" + traceback.format_exc())

    def process_channel(self, item):
        """Decide whether to insert or update a channel."""
        try:
            if not self.get_channel(item.get("id")):
                self.save_channel(item)
            else:
                self.update_channel(item)
        except Exception:
            logging.error("Error : \n" + traceback.format_exc())

    def get_message(self, message_id):
        """Check if a message exists in the collection."""
        return self.search_by_column("message", "id", message_id)

    def save_message(self, item):
        """Insert a new channel into the collection."""
        try:
            processed_item = {k: self.process_value(v) for k, v in item.items()}
            self.write_to_database("message", processed_item)
        except Exception:
            logging.error("Error : \n" + traceback.format_exc())

    def update_message(self, item):
        """Update an existing message based on its ID."""
        try:
            item_id = item.pop("id", None)
            if not item_id:
                raise ValueError("Missing 'message_id' in item for update")

            update_fields = {k: self.process_value(v) for k, v in item.items()}
            self.update_in_database("message", {"id": item_id}, update_fields)
        except Exception:
            logging.error("Error : \n" + traceback.format_exc())

    def process_message(self, item):
        """Decide whether to insert or update a message."""
        try:
            if not self.get_message(item.get("id")):
                self.save_message(item)
            else:
                self.update_message(item)
        except Exception:
            logging.error("Error : \n" + traceback.format_exc())


# Example usage
# if __name__ == "__main__":
#     # Initialize the MongoDB handler
#     db_handler = DBManager()

#     # Create a table (collection) if it doesn't exist
#     db_handler.create_table("users")

#     # Write data to the database (with duplication check)
#     data = {"name": "Alice", "age": 30, "city": "New York"}
#     db_handler.write_to_database("users", data)

#     # Try to write the same data again (should detect duplicate)
#     db_handler.write_to_database("users", data)

#     # Read data from the database
#     print("All documents in the 'users' collection:")
#     print(db_handler.read_from_database("users"))

#     # Search by a specific column
#     print("Searching for documents where city is 'New York':")
#     print(db_handler.search_by_column("users", "city", "New York"))

#     # Search in all columns
#     print("Searching for documents containing 'Alice' in any column:")
#     print(db_handler.search_in_all_columns("users", "Alice"))

#     # Export the collection to a JSON file
#     db_handler.export_table_to_json("users", "exported_users.json")

#     # Close the connection
#     db_handler.close_connection()
