import hashlib
import hmac

def manual_hmac(key, message):
    block_size = 64  # Block size for SHA-256

    # Step 1: Prepare Key
    if len(key) > block_size:
        key = hashlib.sha256(key).digest()
    if len(key) < block_size:
        key = key.ljust(block_size, b'\x00')

    # Step 2: Create ipad and opad
    ipad = bytes([b ^ 0x36 for b in key])
    opad = bytes([b ^ 0x5c for b in key])

    # Step 3: Inner hash
    inner_hash = hashlib.sha256(ipad + message.encode()).digest()

    # Step 4: Outer hash
    final_mac = hashlib.sha256(opad + inner_hash).hexdigest()

    return final_mac


def verify_mac(key, message, received_mac):
    calculated_mac = manual_hmac(key, message)

    # Secure constant-time comparison
    if hmac.compare_digest(calculated_mac, received_mac):
        print("Verification Successful: Message is authentic!")
    else:
        print("Verification Failed: Message or key is incorrect!")


# =========================
# Main Program
# =========================

print("=== HMAC-SHA256 Message Authentication ===")

# User input
key_input = input("Enter secret key: ")
secret_key = key_input.encode()

msg_text = input("Enter your message: ")

# Generate MAC
mac_result = manual_hmac(secret_key, msg_text)

print("\n------------------------------")
print(f"Message: {msg_text}")
print(f"Generated MAC: {mac_result}")
print("------------------------------")

# Simulate verification
print("\nNow verifying the message...")
verify_mac(secret_key, msg_text, mac_result)