# main.py
from encryption.encryption_factory import get_cipher


def main():
    while True:
        print("Select encryption type:")
        print("1. Caesar Cipher")
        print("2. Hill Cipher")
        print("3. Vigenère Cipher")
        print("4. Transposition Cipher")
        print("5. AES Cipher")
        print("6. DES Cipher")
        print("7. RSA Cipher")
        print("8. Hex Cipher")  # Add Hex option
        choice = input("Enter choice (1/2/3/4/5/6/7/8) or 'quit' to exit: ")

        if choice.lower() == "quit":
            break

        text = input("Enter text to be encrypted/decrypted (or 'quit' to exit): ")
        if text.lower() == "quit":
            break

        if choice == "2":
            key = input("Enter key (4 integers separated by spaces): ")
            key = list(map(int, key.split()))
            while len(key) != 4:
                key = input("Invalid key! Enter key (4 integers separated by spaces): ")
                key = list(map(int, key.split()))
        elif choice == "3":
            key = input("Enter key (a string of alphabets): ")
        elif choice == "4":
            key = input("Enter key (a keyword): ")
            while not key.isalpha():
                key = input("Invalid key! Enter key (a keyword): ")
        elif choice == "5":
            key = input("Enter key (16/24/32 characters): ")  # AES key length
            while len(key) not in [16, 24, 32]:
                key = input("Invalid key! Enter key (16/24/32 characters): ")
        elif choice == "6":
            key = input("Enter key (8 characters): ")  # DES key length
            while len(key) != 8:
                key = input("Invalid key! Enter key (8 characters): ")
        elif choice == "7":
            key = input("Enter RSA key (or press Enter to generate a new key): ")
            if not key:
                key = None
        elif choice == "8":
            key = None  # Hex encoding doesn't require a key
        else:
            key = input("Enter key: ")

        cipher = get_cipher(choice)
        if cipher:
            try:
                encrypted_text = cipher.encrypt(text, key)
                decrypted_text = cipher.decrypt(encrypted_text, key)
                print(f"Encrypted Text: {encrypted_text}")
                print(f"Decrypted Text: {decrypted_text}")
            except ValueError as e:
                print(f"Error: {e}")
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
