def simulate_dh():
    q, alpha = 23, 15  # Public prime and primitive root
    print(f"Public: q={q}, alpha={alpha}")

    # Alice
    xa = 5  # Private
    ya = (alpha ** xa) % q
    print(f"Alice: Private={xa}, Public(Ya)={ya}")

    # Bob
    xb = 21 # Private
    yb = (alpha ** xb) % q
    print(f"Bob: Private={xb}, Public(Yb)={yb}")

    # Shared Secret Calculation
    ka = (yb ** xa) % q
    kb = (ya ** xb) % q
    print(f"Calculated Keys: Alice={ka}, Bob={kb}")

simulate_dh()