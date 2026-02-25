# Co-prime checker with user input
def check_coprime_user():
    # Get numbers from the user
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    # Euclidean Algorithm to find GCD
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    res = gcd(a, b)
    if res == 1:
        print(f"{a} and {b} are co-prime.")
    else:
        print(f"{a} and {b} are NOT co-prime (GCD is {res}).")

# Run the function
check_coprime_user()