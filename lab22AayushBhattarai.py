import hashlib
import random

# ---------- RSA Simulation ----------
def rsa_sim(message):
    print("\n=== RSA Simulation ===")
    p, q = 61, 53
    n = p * q
    phi = (p-1)*(q-1)
    e = 17
    d = pow(e, -1, phi)
    print(f"Public Key: (e={e}, n={n}), Private Key: (d={d}, n={n})")

    hash_int = int(hashlib.sha256(message.encode()).hexdigest(), 16) % n
    signature = pow(hash_int, d, n)
    verified = pow(signature, e, n)

    print(f"Message hash (int mod n): {hash_int}")
    print(f"RSA Signature: {signature}")
    print(f"Verified hash int: {verified}")
    print("RSA Verification:", "SUCCESS" if verified == hash_int else "FAILED")

# ---------- DSS Simulation (Simplified) ----------
def dss_sim(message):
    print("\n=== DSS (Simulated) ===")
    # Small prime p, q and generator g for simulation
    p, q, g = 467, 233, 2
    x = random.randint(1, q-1)      # Private key
    y = pow(g, x, p)                 # Public key

    h = int(hashlib.sha256(message.encode()).hexdigest(), 16) % q
    k = random.randint(1, q-1)       # Random per-message key
    r = pow(g, k, p) % q
    s = (pow(k, -1, q) * (h + x * r)) % q  # signature
    print(f"Private key x: {x}, Public key y: {y}")
    print(f"Message hash (mod q): {h}")
    print(f"DSS Signature (r, s): ({r}, {s})")

    # Verification
    w = pow(s, -1, q)
    u1 = (h * w) % q
    u2 = (r * w) % q
    v = (pow(g, u1, p) * pow(y, u2, p)) % p % q
    print(f"Verification v: {v}")
    print("DSS Verification:", "SUCCESS" if v == r else "FAILED")

# ---------- Main ----------
msg = input("Enter your message: ")
rsa_sim(msg)
dss_sim(msg)