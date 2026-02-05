# IDEA (International Data Encryption Algorithm)
# Pure Python implementation (Educational use)

MODULO = 0x10001  # 65537

def mul(a, b):
    if a == 0:
        a = MODULO - 1
    if b == 0:
        b = MODULO - 1
    result = (a * b) % MODULO
    return result if result != MODULO - 1 else 0

def add(a, b):
    return (a + b) % 0x10000

def generate_subkeys(key):
    subkeys = []
    key = int.from_bytes(key, 'big')

    for _ in range(52):
        subkeys.append((key >> 112) & 0xFFFF)
        key = ((key << 25) | (key >> 103)) & ((1 << 128) - 1)

    return subkeys

def idea_encrypt_block(block, subkeys):
    x1, x2, x3, x4 = block

    for r in range(8):
        k = subkeys[r*6:(r+1)*6]

        x1 = mul(x1, k[0])
        x2 = add(x2, k[1])
        x3 = add(x3, k[2])
        x4 = mul(x4, k[3])

        t1 = x1 ^ x3
        t2 = x2 ^ x4

        t1 = mul(t1, k[4])
        t2 = add(t2, t1)
        t2 = mul(t2, k[5])
        t1 = add(t1, t2)

        x1 ^= t2
        x4 ^= t1
        x2 ^= t1
        x3 ^= t2

        x2, x3 = x3, x2

    k = subkeys[48:]
    return (
        mul(x1, k[0]),
        add(x3, k[1]),
        add(x2, k[2]),
        mul(x4, k[3])
    )

def pad(data):
    pad_len = 8 - (len(data) % 8)
    return data + bytes([pad_len] * pad_len)

def unpad(data):
    return data[:-data[-1]]

def idea_encrypt(plaintext, key):
    subkeys = generate_subkeys(key)
    plaintext = pad(plaintext)

    ciphertext = b''
    for i in range(0, len(plaintext), 8):
        block = plaintext[i:i+8]
        words = [int.from_bytes(block[j:j+2], 'big') for j in range(0, 8, 2)]
        encrypted = idea_encrypt_block(words, subkeys)
        for w in encrypted:
            ciphertext += w.to_bytes(2, 'big')

    return ciphertext

# ================== DEMO ==================

if __name__ == "__main__":
    key = b'0123456789abcdef'  # 16 bytes (128-bit key)
    plaintext = b'HELLO IDEA!!!'

    cipher = idea_encrypt(plaintext, key)

    print("Plaintext :", plaintext)
    print("Key       :", key)
    print("Ciphertext:", cipher.hex())
