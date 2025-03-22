from utils.systeminfo import hash_computer
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64


class Security:

    def __init__(self, key_string:str=None):
        """
        Initialize the Security class with a user-provided key string.
        The key string will be converted into a 32 URL-safe base64-encoded bytes key.
        
        :param key_string: A string provided by the user to use as the key.
        """
        if not key_string is None:
            # Convert the user-provided key string into a 32 URL-safe base64-encoded bytes key
            self.key = self._generate_key_from_string(key_string)
            self.cipher = Fernet(self.key)  # Initialize the cipher with the key
        else:
            self.key = Fernet.generate_key()
            self.cipher = Fernet(self.key)

    def _generate_key_from_string(self, key_string):
        """
        Convert a user-provided key string into a 32 URL-safe base64-encoded bytes key.
        
        :param key_string: The user-provided key string.
        :return: A 32 URL-safe base64-encoded bytes key.
        """
        # Use PBKDF2HMAC to derive a secure key from the user-provided string
        salt = b'some_salt'  # You can use a fixed salt or generate a random one
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,  # 32 bytes key
            salt=salt,
            iterations=100000,  # Number of iterations
        )
        # Derive the key
        key = kdf.derive(key_string.encode('utf-8'))
        # Encode the key in URL-safe base64
        return base64.urlsafe_b64encode(key)

    def save_to_binary_file(self, data, file_path):
        """
        Encrypt the data and save it to a binary file.
        
        :param data: The data to be saved (e.g., a list).
        :param file_path: The path to save the binary file.
        """
        try:
            # Convert the data to a string and encode it to bytes
            data_str = str(data)
            data_bytes = data_str.encode('utf-8')

            # Encrypt the data
            encrypted_data = self.cipher.encrypt(data_bytes)

            # Write the encrypted data to a binary file
            with open(file_path, 'wb') as file:
                file.write(encrypted_data)
            print(f"Data saved to {file_path} successfully.")
        except Exception as e:
            print(f"Error saving data to binary file: {e}")

    def read_from_binary_file(self, file_path):
        """
        Read the encrypted binary file, decrypt it, and return the original data.
        
        :param file_path: The path to the binary file.
        :return: The decrypted data (e.g., a list).
        """
        try:
            # Read the encrypted data from the binary file
            with open(file_path, 'rb') as file:
                encrypted_data = file.read()

            # Decrypt the data
            decrypted_data = self.cipher.decrypt(encrypted_data)

            # Convert the decrypted bytes back to a string and then to the original data
            data_str = decrypted_data.decode('utf-8')
            data = eval(data_str)  # Convert string representation of data to original data

            print(f"Data read from {file_path} successfully.")
            return data
        except Exception as e:
            print(f"Error reading data from binary file: {e}")
            return None

    def write_encrypted_data_to_file(self,filename, data):
        """
        Encrypts the data and writes it to a file.
        
        :param filename: The name of the file to write the encrypted data to.
        :param data: The data to encrypt and write to the file.
        """
        # Encrypt the data
        encrypted_data = self.cipher.encrypt(data.encode())
        
        # Write the encrypted data to the file
        with open(filename, 'wb') as file:
            file.write(encrypted_data)

    def read_and_decrypt_data_from_file(self,filename):
        """
        Reads the encrypted data from a file and decrypts it.
        
        :param filename: The name of the file to read the encrypted data from.
        :return: The decrypted data.
        """
        # Read the encrypted data from the file
        with open(filename, 'rb') as file:
            encrypted_data = file.read()
        
        # Decrypt the data
        decrypted_data = self.cipher.decrypt(encrypted_data).decode()
        
        return decrypted_data
# Example usage
# if __name__ == "__main__":
    # Create an instance of the Security class with a user-provided key string
    # user_key = hash_computer()
    # security = Security(user_key)

    # Example data to save
    # data = [1, 2, 3, "Hello", 4.5]

    # Save the data to a binary file
    # security.save_to_binary_file(data, 'secure_data.bin')

    # Read the data back from the binary file
    # retrieved_data = security.read_from_binary_file('secure_data.bin')
    # print("Retrieved Data:", retrieved_data)

    # Display the generated key
    # print("Generated Key:", security.key)
