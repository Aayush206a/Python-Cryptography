import random

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

def miller_rabin_test(n, k=10):
    """
    Miller-Rabin primality test.
    - n: number to test
    - k: iterations (higher = more accurate, but slower)
    Returns True if probably prime, False if composite.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    
    # Write n-1 = 2^s * d
    s = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        s += 1
    
    # Witness loop
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
            return False  # Composite
    return True  # Probably prime

def is_prime_deterministic(n):
    """Deterministic Miller-Rabin for n < 2^64 using known witnesses."""
    if n < 2:
        return False
    witnesses = [2, 3, 5, 7, 11, 13, 23, 283]  # Sufficient for n < 2^64
    return miller_rabin_test(n, k=len(witnesses)) and all(mod_pow(w, n-1, n) == 1 for w in witnesses if w < n)

# Interactive usage
if __name__ == "__main__":
    try:
        n = int(input("Enter a large number to test for primality: "))
        if n < 2**64:
            is_prime = is_prime_deterministic(n)
            print(f"{n} is {'prime' if is_prime else 'composite'} (deterministic).")
        else:
            k = int(input("Enter number of iterations (e.g., 10-20 for high accuracy): ") or 10)
            is_prime = miller_rabin_test(n, k)
            prob = 1 - (1/4)**k  # Rough error probability
            print(f"{n} is {'probably prime' if is_prime else 'composite'} (error prob ~{1-prob:.2%}).")
    except ValueError:
        print("Please enter a valid integer.")