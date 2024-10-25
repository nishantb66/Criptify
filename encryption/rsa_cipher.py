# rsa_cipher.py
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64


class RSACipher:
    def __init__(self, key=None):
        if key:
            self.key = RSA.import_key(key)
        else:
            self.key = RSA.generate(2048)
        self.public_key = self.key.publickey()
        self.cipher = PKCS1_OAEP.new(self.key)
        self.cipher_public = PKCS1_OAEP.new(self.public_key)

    def encrypt(self, raw, key=None):
        if key:
            public_key = RSA.import_key(key)
            cipher_public = PKCS1_OAEP.new(public_key)
            encrypted = cipher_public.encrypt(raw.encode("utf-8"))
        else:
            encrypted = self.cipher_public.encrypt(raw.encode("utf-8"))
        return base64.b64encode(encrypted).decode("utf-8")

    def decrypt(self, enc, key=None):
        if key:
            private_key = RSA.import_key(key)
            cipher = PKCS1_OAEP.new(private_key)
            enc = base64.b64decode(enc)
            decrypted = cipher.decrypt(enc)
        else:
            enc = base64.b64decode(enc)
            decrypted = self.cipher.decrypt(enc)
        return decrypted.decode("utf-8")
