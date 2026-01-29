# Lab 6: P-box (Permutation Box) - Expansion and Compression

EXPANSION_BOX = [
    32,1,2,3,4,5, 4,5,6,7,8,9,
    8,9,10,11,12,13, 12,13,14,15,16,17,
    16,17,18,19,20,21, 20,21,22,23,24,25,
    24,25,26,27,28,29, 28,29,30,31,32,1
]

COMPRESSION_BOX = [
    16,7,20,21,29,12,28,17,
    1,15,23,26,5,18,31,10,
    2,8,24,14,32,27,3,9,
    19,13,30,6,22,11,4,25
]

def permute(bits, box):
    return ''.join(bits[i - 1] for i in box)

def get_32bit_input():
    data = input("Enter 32-bit binary: ")
    if len(data) == 32 and set(data) <= {'0', '1'}:
        return data
    print("Error: Input must be exactly 32 bits (0s and 1s)")
    return None

print("P-box: Expansion and Compression")
print("1: Expansion (32 → 48)")
print("2: Compression (32 → 32)")

choice = input("Enter choice: ")

data = get_32bit_input()
if not data:
    exit()

if choice == '1':
    print("Output (48 bits):", permute(data, EXPANSION_BOX))
elif choice == '2':
    print("Output (32 bits):", permute(data, COMPRESSION_BOX))
else:
    print("Invalid choice")
