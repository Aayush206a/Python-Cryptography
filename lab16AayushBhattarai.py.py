def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def modinv(e, phi):
    t, newt = 0, 1
    r, newr = phi, e
    while newr != 0:
        q = r // newr
        t, newt = newt, t - q * newt
        r, newr = newr, r - q * newr
    if r > 1:
        return None
    if t < 0:
        t += phi
    return t

p = int(input("Enter prime number p: "))
q = int(input("Enter prime number q: "))

n = p * q
phi = (p - 1) * (q - 1)

e = int(input("Enter public key e: "))
while gcd(e, phi) != 1:
    e = int(input("Enter e such that gcd(e, phi) = 1: "))

d = modinv(e, phi)

print("Public Key (e, n):", e, n)
print("Private Key (d, n):", d, n)

msg = int(input("Enter message (integer): "))

cipher = pow(msg, e, n)
print("Encrypted message:", cipher)

plain = pow(cipher, d, n)
print("Decrypted message:", plain)
