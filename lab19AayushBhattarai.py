import struct

# Left rotate 32-bit integer n by b bits
def left_rotate(n, b):
    return ((n << b) | (n >> (32 - b))) & 0xffffffff

# Round 1 function
def F(x, y, z): 
    return (x & y) | (~x & z)

def md4_verbose_user_input(message):
    print(f"--- MD4 EXECUTION ---")
    print(f"Input Message: {message}")
    
    # --------------------------
    # Padding logic
    # --------------------------
    msg_bytes = bytearray(message, 'utf-8')
    orig_len_bits = (len(msg_bytes) * 8) & 0xffffffffffffffff
    msg_bytes.append(0x80)
    while len(msg_bytes) % 64 != 56:
        msg_bytes.append(0x00)
    msg_bytes += struct.pack('<Q', orig_len_bits)
    
    print(f"Post-Padding Hex (first 64 chars): {msg_bytes.hex()[:64]}...")
    print(f"Message Length: {len(msg_bytes)} bytes ({len(msg_bytes)//64} block(s))")

    # --------------------------
    # Initialize Registers
    # --------------------------
    A, B, C, D = 0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476
    print(f"Initial Registers: A={hex(A)}, B={hex(B)}, C={hex(C)}, D={hex(D)}")

    # --------------------------
    # Process first block (simplified: only Round 1)
    # --------------------------
    X = struct.unpack('<16I', msg_bytes[0:64])
    print(f"\nStarting Round 1 (F-Function Operations):")
    
    for i in range(16):
        s = [3, 7, 11, 19][i % 4]
        f_val = F(B, C, D)
        A = left_rotate((A + f_val + X[i]) & 0xffffffff, s)
        # Shift registers
        A, B, C, D = D, A, B, C
        if i < 4:  # Show first 4 steps
            print(f"    Step {i+1}: Registers -> A:{hex(A)} B:{hex(B)} C:{hex(C)} D:{hex(D)}")

    # --------------------------
    # Show final digest preview (first block only)
    # --------------------------
    print(f"\n[RESULT] Final MD4 Digest Preview (first block only): "
          f"{hex(A)}{hex(B)[2:]}{hex(C)[2:]}{hex(D)[2:]}")

# --------------------------
# Main Program
# --------------------------
user_msg = input("Enter your message: ")
md4_verbose_user_input(user_msg)