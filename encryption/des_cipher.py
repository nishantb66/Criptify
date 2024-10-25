# des_cipher.py
from Crypto.Cipher import DES
import base64


class DESCipher:
    def __init__(self):
        self.bs = 8  # Block size for DES

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    def _unpad(self, s):
        return s[: -ord(s[len(s) - 1 :])]

    def encrypt(self, raw, key):
        raw = self._pad(raw)
        cipher = DES.new(key.encode("utf-8"), DES.MODE_ECB)
        return base64.b64encode(cipher.encrypt(raw.encode("utf-8"))).decode("utf-8")

    def decrypt(self, enc, key):
        enc = base64.b64decode(enc)
        cipher = DES.new(key.encode("utf-8"), DES.MODE_ECB)
        return self._unpad(cipher.decrypt(enc).decode("utf-8"))
