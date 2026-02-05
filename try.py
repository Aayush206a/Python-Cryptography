def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def euler_totient(n):
    count = 0
    for i in range(1, n + 1):
        if gcd(n, i) == 1:
            count += 1
    return count

def fermat_theorem(a, p):
    return pow(a, p-1, p)

def euler_theorem(a, n):
    phi = euler_totient(n)
    return pow(a, phi, n), phi

print("Fermat's Theorem")
a = int(input("Enter a (integer): "))
p = int(input("Enter p (prime number): "))
if gcd(a, p) != 1:
    print("Warning: a and p are not coprime")
else:
    print(f"a^(p-1) mod p = {fermat_theorem(a, p)} (should be 1)")

print("\nEuler's Theorem ")
a = int(input("Enter a (integer): "))
n = int(input("Enter n (integer > 1): "))
if gcd(a, n) != 1:
    print("Warning: a and n are not coprime")
else:
    val, phi = euler_theorem(a, n)
    print(f"a^phi(n) mod n = {val} (phi({n}) = {phi})")

print("\nEuler's Totient Function")
n = int(input("Enter n to compute phi(n): "))
print(f"phi({n}) = {euler_totient(n)}")
