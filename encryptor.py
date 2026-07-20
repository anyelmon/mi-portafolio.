from cryptography.fernet  import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as file:
        file.write(key)
    print("Key generated and saved to key.key")
    return key

def load_key():
    with open("key.key", "rb") as file:
        return file.read()


def encrypt_message(message, key):
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message).decode()
    return decrypted_message

print("=== Messsages Encryptor ===\n")
print("1. Generate a new key")
print("2. Encrypt a message")
print("3. Decrypt a message")
print("4. Encrypt a text file\n")

option = input("Choose an option: ")

if option == "1":
    generate_key()
elif option == "2":
    key = load_key()
    message = input("Enter the message to encrypt: ")
    encrypted = encrypt_message(message, key)
    print(f"\nEncrypted message: {encrypted.decode()}")
elif option == "3":
    key = load_key()
    encrypted_message = input("Enter the encrypted message: ")
    decrypted_message = decrypt_message(encrypted_message.encode(), key)
    print(f"\nDecrypted message: {decrypted}")
elif option == "4":
    key = load_key()
    file_path = input("Enter the path to the text file: ")
    with open(file_path, "r") as file:
        content = file.read()
    encrypted_content = encrypt_message(content, key)
    with open(file_path + ".enc", "wb") as file:
        file.write(encrypted_content)
    print(f"\nFile encrypted and saved as {file_path}.enc")
