def railfence(text, rails, mode):
    text = text.replace(" ", "").upper()

    # Create zigzag pattern
    pattern = []
    rail = 0
    step = 1
    for _ in text:
        pattern.append(rail)
        if rail == 0:
            step = 1
        elif rail == rails - 1:
            step = -1
        rail += step

    # Encrypt
    if mode == "encrypt":
        fence = [""] * rails
        for i in range(len(text)):
            fence[pattern[i]] += text[i]
        return "".join(fence)

    # Decrypt
    elif mode == "decrypt":
        fence = [""] * rails
        index = 0
        for r in range(rails):
            for i in range(len(text)):
                if pattern[i] == r:
                    fence[r] += text[index]
                    index += 1

        result = ""
        rail_pos = [0] * rails
        for r in pattern:
            result += fence[r][rail_pos[r]]
            rail_pos[r] += 1
        return result


# -------- Main Program --------
print("Rail Fence Cipher")
print("1: Encrypt")
print("2: Decrypt")

choice = input("Enter choice: ")
rails = int(input("Enter number of rails: "))
text = input("Enter text: ")

if choice == "1":
    print("Encrypted Text:", railfence(text, rails, "encrypt"))
elif choice == "2":
    print("Decrypted Text:", railfence(text, rails, "decrypt"))
else:
    print("Invalid choice")
