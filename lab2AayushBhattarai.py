"""
Lab 2: Hill Cipher Implementation
"""

def mod_inverse(a, m):
    """Find modular inverse"""
    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        gcd_val, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        return gcd_val, x, x1
    
    _, x, _ = extended_gcd(a % m, m)
    return (x % m + m) % m

def hill_encrypt(plaintext, key_matrix):
    """Encrypt using Hill Cipher"""
    plaintext = plaintext.upper().replace(" ", "")
    ciphertext = ""
    
    # 2x2 matrix encryption
    for i in range(0, len(plaintext), 2):
        if i + 1 < len(plaintext):
            x1 = ord(plaintext[i]) - ord('A')
            x2 = ord(plaintext[i + 1]) - ord('A')
            
            y1 = (key_matrix[0][0] * x1 + key_matrix[0][1] * x2) % 26
            y2 = (key_matrix[1][0] * x1 + key_matrix[1][1] * x2) % 26
            
            ciphertext += chr(y1 + ord('A')) + chr(y2 + ord('A'))
    
    return ciphertext

def hill_decrypt(ciphertext, key_matrix):
    """Decrypt using Hill Cipher"""
    ciphertext = ciphertext.upper().replace(" ", "")
    plaintext = ""
    
    # Calculate determinant
    det = (key_matrix[0][0] * key_matrix[1][1] - key_matrix[0][1] * key_matrix[1][0]) % 26
    det_inv = mod_inverse(det, 26)
    
    # Inverse matrix: (1/det) * [[d, -b], [-c, a]]
    inv = [
        [(key_matrix[1][1] * det_inv) % 26, ((-key_matrix[0][1]) * det_inv) % 26],
        [((-key_matrix[1][0]) * det_inv) % 26, (key_matrix[0][0] * det_inv) % 26]
    ]
    
    for i in range(0, len(ciphertext), 2):
        if i + 1 < len(ciphertext):
            y1 = ord(ciphertext[i]) - ord('A')
            y2 = ord(ciphertext[i + 1]) - ord('A')
            
            x1 = (inv[0][0] * y1 + inv[0][1] * y2) % 26
            x2 = (inv[1][0] * y1 + inv[1][1] * y2) % 26
            
            plaintext += chr(x1 + ord('A')) + chr(x2 + ord('A'))
    
    return plaintext

print("Hill Cipher")
choice = input("1:Encrypt 2:Decrypt: ")
key = [[1, 2], [3, 5]]

if choice == '1':
    text = input("Enter text: ")
    print("Result:", hill_encrypt(text, key))
elif choice == '2':
    text = input("Enter text: ")
    print("Result:", hill_decrypt(text, key))
else:
    print("Invalid")