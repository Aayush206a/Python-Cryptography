from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

def aes_encrypt(plaintext, key):
    """
    Encrypts plaintext using AES-128 in ECB mode.
    - plaintext: string to encrypt
    - key: 16-byte (128-bit) key as bytes
    Returns base64-encoded ciphertext.
    """
    cipher = AES.new(key, AES.MODE_ECB)
    # Pad plaintext to 16-byte blocks (simple PKCS7-like padding)
    block_size = 16
    padding_length = block_size - (len(plaintext) % block_size)
    padded_plaintext = plaintext + chr(padding_length) * padding_length
    ciphertext = cipher.encrypt(padded_plaintext.encode('utf-8'))
    return base64.b64encode(ciphertext).decode('utf-8')

def aes_decrypt(ciphertext_b64, key):
    """
    Decrypts base64-encoded ciphertext using AES-128 in ECB mode.
    - ciphertext_b64: base64 string
    - key: 16-byte key as bytes
    Returns original plaintext string.
    """
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = base64.b64decode(ciphertext_b64)
    decrypted_padded = cipher.decrypt(ciphertext).decode('utf-8')
    # Remove padding
    padding_length = ord(decrypted_padded[-1])
    return decrypted_padded[:-padding_length]

# Interactive usage
if __name__ == "__main__":
    # Generate a random 128-bit key (you could also ask the user for one)
    key = get_random_bytes(16)
    print("AES-128 Key generated (keep it secret!):", key.hex())

    # Ask for plaintext to encrypt
    plaintext = input("Enter the plaintext to encrypt: ")
    encrypted = aes_encrypt(plaintext, key)
    print(f"Encrypted (base64): {encrypted}")

    # Ask for ciphertext to decrypt
    ciphertext_b64 = input("Enter the base64-encoded ciphertext to decrypt: ")
    try:
        decrypted = aes_decrypt(ciphertext_b64, key)
        print(f"Decrypted: {decrypted}")
    except Exception as e:
        print(f"Decryption failed: {e} (Ensure the ciphertext and key match)")