import streamlit as st
from encryption.caesar_cipher import CaesarCipher
from encryption.hill_cipher import HillCipher
from encryption.vigenere_cipher import VigenereCipher
from encryption.transposition_cipher import TranspositionCipher
from encryption.aes_cipher import AESCipher
from encryption.des_cipher import DESCipher
from encryption.rsa_cipher import RSACipher
from encryption.hex_cipher import HexCipher

# Inject advanced CSS for Neumorphism and Glassmorphism styling
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@600&family=Poppins:wght@400&display=swap');

    body {
        font-family: 'Poppins', sans-serif;
        background: linear-gradient(135deg, #1f1f1f, #2c3e50);
        color: #FFFFFF;
    }

    /* Container styling */
    .main {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 40px;
        box-shadow: 0px 4px 30px rgba(0, 0, 0, 0.4);
        backdrop-filter: blur(10px);
    }

    /* Textarea and Input Field */
    textarea, input, select {
        width: 100%;
        padding: 15px;
        margin: 10px 0;
        border-radius: 15px;
        border: none;
        background-color: rgba(0, 0, 0, 0.2);
        color: #fff;
        box-shadow: 6px 6px 15px rgba(0, 0, 0, 0.5), -6px -6px 15px rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(8px);
        transition: all 0.3s ease-in-out;
    }

    /* Button with Neumorphism effect */
    button {
        background: #2d2d2d;
        border-radius: 50px;
        padding: 12px 30px;
        font-size: 16px;
        color: #00C9A7;
        cursor: pointer;
        box-shadow: 9px 9px 18px rgba(0, 0, 0, 0.5), -9px -9px 18px rgba(255, 255, 255, 0.1);
        transition: 0.4s;
    }

    button:hover {
        transform: translateY(-3px);
        box-shadow: 0px 15px 30px rgba(0, 201, 167, 0.5);
    }

    /* Card-style sections */
    .card {
        background: rgba(0, 0, 0, 0.3);
        padding: 20px;
        border-radius: 15px;
        box-shadow: 6px 6px 15px rgba(0, 0, 0, 0.5), -6px -6px 15px rgba(255, 255, 255, 0.1);
    }

    /* Sidebar styling with Glassmorphism */
    .css-1d391kg {
        background-color: rgba(44, 62, 80, 0.8);
        border-right: 1px solid rgba(255, 255, 255, 0.1);
        color: #fff;
    }

    /* Icon styling */
    .lock-icon {
        margin-right: 5px;
        color: #FFD700;
    }

    .key-icon {
        margin-right: 5px;
        color: #F9A825;
    }

    /* Loader Animation */
    @keyframes pulse {
        0% {
            transform: scale(1);
        }
        50% {
            transform: scale(1.1);
        }
        100% {
            transform: scale(1);
        }
    }

    .loading {
        animation: pulse 2s infinite;
        font-size: 20px;
        color: #00C9A7;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# Helper function to get cipher based on selection
def get_cipher(choice):
    if choice == "Caesar Cipher":
        return CaesarCipher()
    elif choice == "Hill Cipher":
        return HillCipher()
    elif choice == "Vigenère Cipher":
        return VigenereCipher()
    elif choice == "Transposition Cipher":
        return TranspositionCipher()
    elif choice == "AES Cipher":
        return AESCipher()
    elif choice == "DES Cipher":
        return DESCipher()
    elif choice == "RSA Cipher":
        return RSACipher()
    elif choice == "Hex Cipher":
        return HexCipher()
    else:
        return None


# Streamlit app setup
st.title("🔐 Cryptify")
st.write("Select an encryption method from the sidebar and enter the required details.")

# Sidebar for selecting encryption method
option = st.sidebar.selectbox(
    "Select encryption type:",
    (
        "Caesar Cipher",
        "Hill Cipher",
        "Vigenère Cipher",
        "Transposition Cipher",
        "AES Cipher",
        "DES Cipher",
        "RSA Cipher",
        "Hex Cipher",
    ),
)

# Display container for user input
st.markdown(
    "<div class='card'>📝 Enter text to be encrypted or decrypted:</div>",
    unsafe_allow_html=True,
)
text = st.text_area("", placeholder="Enter your text here...")

# Key input based on cipher selection
if option == "Hill Cipher":
    key = st.text_input(
        "🔑 **Enter key (4 integers separated by spaces):**", value="6 24 1 3"
    )
    key = list(map(int, key.split()))
elif option == "Vigenère Cipher":
    key = st.text_input("🔑 **Enter key (a string of alphabets):**", value="KEY")
elif option == "Transposition Cipher":
    key = st.text_input("🔑 **Enter key (a keyword):**", value="SECRET")
elif option == "AES Cipher":
    key = st.text_input(
        "🔑 **Enter key (16/24/32 characters):**", value="ThisIsASecretKey"
    )
elif option == "DES Cipher":
    key = st.text_input("🔑 **Enter key (8 characters):**", value="8CharKey")
elif option == "RSA Cipher":
    key = st.text_area("🔑 **Enter RSA key (leave blank to generate a new key):**")
    if not key:
        key = None
elif option == "Hex Cipher":
    key = None  # No key for Hex
else:
    key = st.text_input("🔑 **Enter key:**", value="3")

# Cipher action
cipher = get_cipher(option)

col1, col2 = st.columns(2)

with col1:
    if st.button("🔐 Encrypt"):
        with st.spinner("Encrypting..."):
            if cipher:
                try:
                    if option == "Caesar Cipher":
                        encrypted_text, steps = cipher.encrypt(text, key)
                        st.success(f"🔒 **Encrypted Text**: {encrypted_text}")
                        st.markdown("### Steps:")
                        for step in steps:
                            st.write(step)
                    elif option == "Vigenère Cipher":
                        encrypted_text, steps = cipher.encrypt(text, key)
                        st.success(f"🔒 **Encrypted Text**: {encrypted_text}")
                        st.markdown("### Steps:")
                        for step in steps:
                            st.write(step)
                    elif option == "Hex Cipher":
                        encrypted_text, steps = cipher.encrypt(text, key)
                        st.success(f"🔒 **Encrypted Text**: {encrypted_text}")
                        st.markdown("### Steps:")
                        for step in steps:
                            st.write(step)
                    else:
                        encrypted_text = cipher.encrypt(text, key)
                        st.success(f"🔒 **Encrypted Text**: {encrypted_text}")
                except ValueError as e:
                    st.error(f"Error: {e}")
            else:
                st.error("Invalid choice!")

with col2:
    if st.button("🔓 Decrypt"):
        with st.spinner("Decrypting..."):
            if cipher:
                try:
                    if option == "Caesar Cipher":
                        decrypted_text, steps = cipher.decrypt(text, key)
                        st.success(f"🔓 **Decrypted Text**: {decrypted_text}")
                        st.markdown("### Steps:")
                        for step in steps:
                            st.write(step)
                    elif option == "Vigenère Cipher":
                        decrypted_text, steps = cipher.decrypt(text, key)
                        st.success(f"🔓 **Decrypted Text**: {decrypted_text}")
                        st.markdown("### Steps:")
                        for step in steps:
                            st.write(step)
                except ValueError as e:
                    st.error(f"Error: {e}")
                except Exception as e:
                    st.error(f"An unexpected error occurred: {e}")
