# Lab 21: SHA-1 Implementation
import hashlib

def implement_sha1(text):
    print("--- SHA-1 Implementation ---")
    # Step 1: Encode string to bytes
    byte_data = text.encode()
    
    # Step 2: Apply SHA-1
    sha1_hash = hashlib.sha1(byte_data).hexdigest()
    
    print(f"Input: {text}")
    print(f"SHA-1 Digest: {sha1_hash}")

implement_sha1("AayushBhattaraisGod")