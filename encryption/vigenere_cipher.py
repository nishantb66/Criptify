class VigenereCipher:
    def generate_key(self, text, key):
        key = list(key)
        if len(text) == len(key):
            return key
        else:
            for i in range(len(text) - len(key)):
                key.append(key[i % len(key)])
        return "".join(key)

    def encrypt(self, text, key):
        key = self.generate_key(text, key)
        encrypted_text = []
        steps = []
        for i in range(len(text)):
            x = (ord(text[i].upper()) + ord(key[i].upper()) - 2 * ord("A")) % 26
            x += ord("A")
            encrypted_text.append(chr(x))
            steps.append(
                f"{text[i]} ({ord(text[i].upper())}) + {key[i]} ({ord(key[i].upper())}) -> {chr(x)} ({x})"
            )
        return "".join(encrypted_text), steps

    def decrypt(self, text, key):
        key = self.generate_key(text, key)
        decrypted_text = []
        steps = []
        for i in range(len(text)):
            x = (ord(text[i]) - ord(key[i].upper()) + 26) % 26
            x += ord("A")
            decrypted_text.append(chr(x))
            steps.append(
                f"{text[i]} ({ord(text[i])}) - {key[i]} ({ord(key[i].upper())}) -> {chr(x)} ({x})"
            )
        return "".join(decrypted_text), steps
