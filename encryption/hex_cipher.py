class HexCipher:
    def encrypt(self, raw, key=None):
        steps = []
        hex_result = raw.encode("utf-8").hex()
        for char in raw:
            hex_char = char.encode("utf-8").hex()
            steps.append(f"{char} -> {hex_char}")
        return hex_result, steps

    def decrypt(self, enc, key=None):
        steps = []
        raw_result = bytes.fromhex(enc).decode("utf-8")
        for i in range(0, len(enc), 2):
            hex_char = enc[i : i + 2]
            char = bytes.fromhex(hex_char).decode("utf-8")
            steps.append(f"{hex_char} -> {char}")
        return raw_result, steps
