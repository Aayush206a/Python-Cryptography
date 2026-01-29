# Lab 7: DES (Data Encryption Standard) Key Generation

# Permutation tables and rotations
PC1 = [
    57,49,41,33,25,17,9,1,58,50,42,34,26,18,
    10,2,59,51,43,35,27,19,11,3,60,52,44,36,
    28,20,12,4,63,55,47,39,31,23,15,7,62,54,
    46,38,30,22,14,6,61,53,45,37,29,21,13,5
]

PC2 = [
    14,17,11,24,1,5,3,28,15,6,21,10,23,19,12,4,
    26,8,16,7,27,20,13,2,41,52,31,37,47,55,30,
    40,51,45,33,48,44,49,39,56,34,53,46,42,50,36,
    29,32
]

ROTATIONS = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

# ---------- Functions ----------
def permute(bits, table):
    return ''.join(bits[i-1] for i in table)

def rotate_left(bits, n):
    return bits[n:] + bits[:n]

def generate_subkeys(key64):
    """Generate 16 DES subkeys from 64-bit key"""
    key56 = permute(key64, PC1)
    left, right = key56[:28], key56[28:]
    subkeys = []

    for i in range(16):
        left = rotate_left(left, ROTATIONS[i])
        right = rotate_left(right, ROTATIONS[i])
        combined = left + right
        subkeys.append(permute(combined, PC2))
    
    return subkeys

# ---------- Main Program ----------
print("DES Key Generation")

key = input("Enter 64-bit binary key: ")
if len(key) == 64 and set(key) <= {'0','1'}:
    subkeys = generate_subkeys(key)
    print("\nGenerated Subkeys:")
    for i, k in enumerate(subkeys, 1):
        print(f"K{i}: {k}")
else:
    print("Error: Key must be exactly 64 bits (0s and 1s)")
