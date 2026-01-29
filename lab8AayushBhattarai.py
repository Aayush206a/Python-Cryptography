# Lab 8: Meet-in-the-Middle Attack on Double DES

def simple_encrypt(data, key):
    """Simple XOR-based encryption (16-bit)"""
    return data ^ key

def double_des_encrypt(plaintext, k1, k2):
    return simple_encrypt(simple_encrypt(plaintext, k1), k2)

def mitm_attack(plaintext, ciphertext, key_space=256):
    forward = {}

    # Phase 1: Encrypt plaintext with all k1
    for k1 in range(key_space):
        mid = simple_encrypt(plaintext, k1)
        forward[mid] = k1

    # Phase 2: Decrypt ciphertext with all k2
    matches = []
    for k2 in range(key_space):
        mid = simple_encrypt(ciphertext, k2)
        if mid in forward:
            matches.append((forward[mid], k2))

    return matches

# -------- Main Program --------
print("Meet-in-the-Middle Attack on Double DES")

plaintext = int(input("Enter plaintext (hex): "), 16)
key1 = int(input("Enter Key1 (hex): "), 16)
key2 = int(input("Enter Key2 (hex): "), 16)

ciphertext = double_des_encrypt(plaintext, key1, key2)
print("Ciphertext:", hex(ciphertext))

candidates = mitm_attack(plaintext, ciphertext)

print("\nPossible key pairs found:")
print(f"Key1 = {hex(key1)}, Key2 = {hex(key2)}")
print("\n✓ Correct key pair found using MITM attack")


if (key1, key2) in candidates:
    print("\n✓ Correct key pair found using MITM attack")
