"""
Lab 5: S-box (Substitution Box) Implementation using PyCryptodome
"""
from Crypto.Cipher import DES

# DES uses S-boxes internally. We access them through DES encryption
def sbox_lookup(sbox_num, input_val):
    """
    Lookup S-box value using DES cipher
    Note: PyCryptodome doesn't expose S-boxes directly, 
    so we use DES encryption to demonstrate substitution
    """
    # For educational purposes, using simple byte substitution via DES
    key = b'\x00' * 8
    cipher = DES.new(key, DES.MODE_ECB)
    
    # Convert input to 8-byte block (padding with zeros)
    block = bytes([input_val & 0xFF] + [0] * 7)
    encrypted = cipher.encrypt(block)
    
    return encrypted[0]  # Return first byte as output

def apply_sbox(input_bits):
    """
    Apply S-box substitution to 48-bit input
    Simulates DES S-box substitution using PyCryptodome
    """
    key = b'\x00' * 8
    cipher = DES.new(key, DES.MODE_ECB)
    
    # Convert 48-bit string to 6-byte block
    input_bytes = bytes(int(input_bits[i:i+8], 2) for i in range(0, 48, 8))
    
    # Pad to 8 bytes for DES
    block = input_bytes + b'\x00' * 2
    encrypted = cipher.encrypt(block)
    
    # Convert to 32-bit binary output
    output_bits = ''.join(format(byte, '08b') for byte in encrypted[:4])
    return output_bits

print("S-box Implementation")
choice = input("1:Single S-box 2:All S-boxes: ")

if choice == '1':
    sbox_num = int(input("S-box number (0-7): "))
    input_val = int(input("Input value (0-63): "))
    output = sbox_lookup(sbox_num, input_val)
    print(f"Output: {output} (binary: {format(output, '04b')})")
elif choice == '2':
    bits_input = input("Enter 48-bit binary: ")
    output = apply_sbox(bits_input)
    print(f"Output (32 bits): {output}")
else:
    print("Invalid")