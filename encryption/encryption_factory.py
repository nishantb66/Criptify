# encryption_factory.py
from .caesar_cipher import CaesarCipher
from .hill_cipher import HillCipher
from .vigenere_cipher import VigenereCipher
from .transposition_cipher import TranspositionCipher
from .aes_cipher import AESCipher
from .des_cipher import DESCipher
from .rsa_cipher import RSACipher
from .hex_cipher import HexCipher  # Import the Hex cipher


def get_cipher(choice):
    if choice == "1":
        return CaesarCipher()
    elif choice == "2":
        return HillCipher()
    elif choice == "3":
        return VigenereCipher()
    elif choice == "4":
        return TranspositionCipher()
    elif choice == "5":
        return AESCipher()
    elif choice == "6":
        return DESCipher()
    elif choice == "7":
        return RSACipher()
    elif choice == "8":
        return HexCipher()  # Return Hex cipher instance
    else:
        return None
