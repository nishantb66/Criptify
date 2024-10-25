import numpy as np


class HillCipher:
    def __init__(self):
        self.key_matrix = None

    def set_key(self, key):
        if len(key) != 4:
            raise ValueError("Key must contain exactly 4 integers.")
        # Reshape the key into a 2x2 matrix
        self.key_matrix = np.array(key).reshape(2, 2)
        # Calculate the determinant
        det = int(np.round(np.linalg.det(self.key_matrix)))
        # Validate the determinant for invertibility (GCD(det, 26) must be 1)
        if np.gcd(det, 26) != 1:
            raise ValueError(
                "Key matrix is not invertible under mod 26. Please provide a valid key."
            )

    def encrypt(self, text, key):
        # Validate the key first
        self.set_key(key)
        text = text.upper()
        # Pad text if necessary (for even number of letters)
        if len(text) % 2 != 0:
            text += "X"
        encrypted_text = ""
        for i in range(0, len(text), 2):
            # Convert text pair into a vector
            text_vector = [ord(char) - 65 for char in text[i : i + 2]]
            text_vector = np.array(text_vector).reshape(2, 1)
            # Matrix multiplication and mod 26 for encryption
            encrypted_vector = np.dot(self.key_matrix, text_vector) % 26
            encrypted_text += "".join(
                chr(int(num) + 65) for num in encrypted_vector.flatten()
            )
        return encrypted_text

    def decrypt(self, text, key):
        # Validate the key first
        self.set_key(key)
        # Calculate the modular inverse of the key matrix
        det = int(np.round(np.linalg.det(self.key_matrix)))
        det_inv = pow(det, -1, 26)
        adjugate_matrix = (
            np.round(det * np.linalg.inv(self.key_matrix)).astype(int) % 26
        )
        inverse_key_matrix = (det_inv * adjugate_matrix) % 26

        text = text.upper()
        decrypted_text = ""
        for i in range(0, len(text), 2):
            text_vector = [ord(char) - 65 for char in text[i : i + 2]]
            text_vector = np.array(text_vector).reshape(2, 1)
            decrypted_vector = np.dot(inverse_key_matrix, text_vector) % 26
            decrypted_text += "".join(
                chr(int(num) + 65) for num in decrypted_vector.flatten()
            )

        # Remove padding character 'X' if it was added
        return decrypted_text.rstrip("X")


# Example usage
# cipher = HillCipher()
# key = [3, 3, 2, 5]  # Example key matrix
# encrypted_text = cipher.encrypt("nishant", key)
# decrypted_text = cipher.decrypt(encrypted_text, key)
# print(f"Encrypted Text: {encrypted_text}")
# print(f"Decrypted Text: {decrypted_text}")
