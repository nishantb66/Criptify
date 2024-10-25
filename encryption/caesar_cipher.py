class CaesarCipher:
    def encrypt(self, text, key):
        result = ""
        steps = []
        for i in range(len(text)):
            char = text[i]
            if char.isupper():
                new_char = chr((ord(char) + int(key) - 65) % 26 + 65)
                steps.append(f"{char} -> {new_char}")
                result += new_char
            elif char.islower():
                new_char = chr((ord(char) + int(key) - 97) % 26 + 97)
                steps.append(f"{char} -> {new_char}")
                result += new_char
            else:
                result += char
        return result, steps

    def decrypt(self, text, key):
        return self.encrypt(text, -int(key))
