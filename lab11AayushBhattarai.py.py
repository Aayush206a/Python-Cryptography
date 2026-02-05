def extended_euclidean(a, b):
    """
    Computes the GCD of a and b, and coefficients x, y such that a*x + b*y = gcd(a, b).
    Uses recursion.
    """
    if b == 0:
        return a, 1, 0  # Base case: gcd = a, x=1, y=0
    else:
        gcd, x1, y1 = extended_euclidean(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y

# Interactive usage
if __name__ == "__main__":
    try:
        a = int(input("Enter the first integer (a): "))
        b = int(input("Enter the second integer (b): "))
        
        gcd, x, y = extended_euclidean(a, b)
        
        print(f"GCD of {a} and {b} is: {gcd}")
        print(f"Coefficients: x = {x}, y = {y}")
        print(f"Verification: {a} * {x} + {b} * {y} = {a * x + b * y}")
        
        # Optional: Check if modular inverse exists (if gcd == 1)
        if gcd == 1:
            inverse_a = x % b  # Modular inverse of a modulo b
            print(f"Modular inverse of {a} modulo {b} is: {inverse_a}")
        else:
            print("No modular inverse exists since GCD != 1.")
    except ValueError:
        print("Please enter valid integers.")