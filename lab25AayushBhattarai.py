import hashlib

def sha_comparison():
    message = input("Enter a message to hash: ")
    print(f"\n--- SHA-256 vs SHA-512 ---\n")
    
    data = message.encode()
    sha256 = hashlib.sha256(data).hexdigest()
    sha512 = hashlib.sha512(data).hexdigest()
    
    print(f"SHA-256 (256 bits): {sha256}")
    print("-" * 20)
    print(f"SHA-512 (512 bits): {sha512}")

# Run the function
sha_comparison()