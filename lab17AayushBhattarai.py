import random

p = int(input("Enter large prime number p: "))
g = int(input("Enter primitive root g: "))

x = int(input("Enter private key x: "))
y = pow(g, x, p)

print("Public key (p, g, y):", p, g, y)
print("Private key x:", x)

m = int(input("Enter message (integer < p): "))

k = random.randint(1, p-2)

c1 = pow(g, k, p)
c2 = (m * pow(y, k, p)) % p

print("Ciphertext (c1, c2):", c1, c2)

s = pow(c1, x, p)
s_inv = pow(s, p-2, p)

m_dec = (c2 * s_inv) % p

print("Decrypted message:", m_dec)
