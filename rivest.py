import random
import math

def mod_pow(base, exp, mod):
    """Efficient modular exponentiation: (base^exp) % mod."""
    result = 1
    base %= mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def is_prime(n, k=5):
    """Miller-Rabin primality test."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    s, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        s += 1
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = mod_pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True

def extended_gcd(a, b):
    """Extended Euclidean Algorithm for modular inverse."""
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

def mod_inverse(e, phi):
    """Compute modular inverse of e modulo phi."""
    gcd, x, _ = extended_gcd(e, phi)
    if gcd != 1:
        raise ValueError("e and phi are not coprime.")
    return x % phi

def generate_keys(p, q):
    """Generate RSA keys."""
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("p and q must be prime.")
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537  # Common public exponent
    if math.gcd(e, phi) != 1:
        e = random.choice([x for x in range(3, phi, 2) if math.gcd(x, phi) == 1])
    d = mod_inverse(e, phi)
    return (e, n), (d, n)  # Public, Private

def encrypt(message, public_key):
    """Encrypt message (int) using public key."""
    e, n = public_key
    return mod_pow(message, e, n)

def decrypt(ciphertext, private_key):
    """Decrypt ciphertext using private key."""
    d, n = private_key
    return mod_pow(ciphertext, d, n)

# Interactive usage
if __name__ == "__main__":
    print("RSA Cryptosystem Simulator")
    try:
        choice = input("1. Generate keys\n2. Encrypt/Decrypt\nChoose: ").strip()
        
        if choice == '1':
            p = int(input("Enter prime p: "))
            q = int(input("Enter prime q: "))
            public_key, private_key = generate_keys(p, q)
            print(f"Public Key: {public_key}")
            print(f"Private Key: {private_key}")
        
        elif choice == '2':
            e = int(input("Enter public e: "))
            n = int(input("Enter n: "))
            d = int(input("Enter private d: "))
            public_key = (e, n)
            private_key = (d, n)
            
            message = int(input("Enter message as integer (e.g., 123): "))
            ciphertext = encrypt(message, public_key)
            print(f"Encrypted: {ciphertext}")
            
            decrypted = decrypt(ciphertext, private_key)
            print(f"Decrypted: {decrypted}")
            if decrypted == message:
                print("Success: Message recovered!")
            else:
                print("Error: Decryption failed.")
        
        else:
            print("Invalid choice.")
    except ValueError as e:
        print(f"Error: {e}")    