class TranspositionCipher:
    def encrypt(self, text, keyword):
        num_of_columns = len(keyword)
        num_of_rows = len(text) // num_of_columns + (
            1 if len(text) % num_of_columns != 0 else 0
        )
        ciphertext = [""] * num_of_columns

        for col in range(num_of_columns):
            pointer = col
            while pointer < len(text):
                ciphertext[col] += text[pointer]
                pointer += num_of_columns

        # Sort columns based on the alphabetical order of the keyword
        sorted_columns = sorted(zip(keyword, ciphertext))
        return "".join([col[1] for col in sorted_columns])

    def decrypt(self, text, keyword):
        num_of_columns = len(keyword)
        num_of_rows = len(text) // num_of_columns + (
            1 if len(text) % num_of_columns != 0 else 0
        )
        num_of_shaded_boxes = num_of_columns * num_of_rows - len(text)

        # Determine the number of characters in each column
        col_lengths = [num_of_rows] * num_of_columns
        for i in range(num_of_shaded_boxes):
            col_lengths[-(i + 1)] -= 1

        # Sort the columns based on the original keyword
        sorted_keyword = sorted(keyword)
        ciphertext_columns = [""] * num_of_columns

        index = 0
        for i in range(num_of_columns):
            ciphertext_columns[keyword.index(sorted_keyword[i])] = text[
                index : index + col_lengths[i]
            ]
            index += col_lengths[i]

        # Read the plaintext row by row
        plaintext = []
        for row in range(num_of_rows):
            for col in range(num_of_columns):
                if row < len(ciphertext_columns[col]):
                    plaintext.append(ciphertext_columns[col][row])

        return "".join(plaintext)


# Example usage
# cipher = TranspositionCipher()
# encrypted_text = cipher.encrypt("nishant", "tyr")
# decrypted_text = cipher.decrypt(encrypted_text, "tyr")
# print(f"Encrypted Text: {encrypted_text}")
# print(f"Decrypted Text: {decrypted_text}")
