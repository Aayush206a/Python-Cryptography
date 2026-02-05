import math

def euler_totient(n):
    """
    Compute Euler's totient function φ(n): number of integers k in 1 <= k <= n that are coprime with n.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            result -= result // p
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        result -= result // n
    return result

def mod_pow(base, exp, mod):
    """
    Compute (base^exp) % mod efficiently using exponentiation by squaring.
    """
    result = 1
    base %= mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def fermat_little_theorem(a, p):
    """
    Verify Fermat's Little Theorem: If p is prime and a % p != 0, then a^(p-1) ≡ 1 mod p.
    Also checks a^p ≡ a mod p.
    Returns True if both hold, else False.
    """
    if not is_prime(p):
        raise ValueError("p must be prime for Fermat's Little Theorem.")
    if a % p == 0:
        return True  # Trivially true, but theorem assumes a not divisible by p
    lhs1 = mod_pow(a, p - 1, p)
    lhs2 = mod_pow(a, p, p)
    return lhs1 == 1 and lhs2 == a % p

def euler_theorem(a, n):
    """
    Verify Euler's Theorem: If gcd(a, n) == 1, then a^φ(n) ≡ 1 mod n.
    Returns True if it holds, else False.
    """
    if math.gcd(a, n) != 1:
        return False  # Theorem requires a and n coprime
    phi_n = euler_totient(n)
    lhs = mod_pow(a, phi_n, n)
    return lhs == 1

def is_prime(n):
    """
    Simple primality test (for small n; use better methods for large n).
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Interactive usage
if __name__ == "__main__":
    print("Choose an option:")
    print("1. Compute Euler's Totient φ(n)")
    print("2. Verify Fermat's Little Theorem")
    print("3. Verify Euler's Theorem")
    
    choice = input("Enter choice (1/2/3): ").strip()
    
    if choice == '1':
        try:
            n = int(input("Enter n: "))
            phi = euler_totient(n)
            print(f"φ({n}) = {phi}")
        except ValueError as e:
            print(f"Error: {e}")
    
    elif choice == '2':
        try:
            a = int(input("Enter a: "))
            p = int(input("Enter prime p: "))
            if fermat_little_theorem(a, p):
                print(f"Fermat's Little Theorem holds for a={a}, p={p}.")
            else:
                print(f"Fermat's Little Theorem does NOT hold for a={a}, p={p}.")
        except ValueError as e:
            print(f"Error: {e}")
    
    elif choice == '3':
        try:
            a = int(input("Enter a: "))
            n = int(input("Enter n: "))
            if euler_theorem(a, n):
                print(f"Euler's Theorem holds for a={a}, n={n}.")
            else:
                print(f"Euler's Theorem does NOT hold for a={a}, n={n} (possibly not coprime).")
        except ValueError as e:
            print(f"Error: {e}")
    
    else:
        print("Invalid choice.")