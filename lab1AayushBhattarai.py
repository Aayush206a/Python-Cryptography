def caesar_cipher_tool():
    """
    Runs an interactive command-line tool for Caesar cipher operations.
    """
    print("--- Caesar Cipher Tool ---")
    
    # Ask user for operation mode
    mode = input("Do you want to (E)ncrypt or (D)ecrypt? Enter E or D: ").lower()
    
    if mode not in ['e', 'd']:
        print("Invalid mode selected. Exiting.")
        return
    # Get message and key from user
    message = input("Enter the message: ")
    try:
        key = int(input("Enter the key:"))
    except ValueError:
        print("Invalid key entered.")
        return

    result = ""
    # Adjust key for decryption mode
    if mode == 'd':
        key = -key
    
    # Process each character
    for char in message:
        if 'a' <= char <= 'z':
            result += chr(((ord(char) - ord('a') + key) % 26) + ord('a'))
        elif 'A' <= char <= 'Z':
            result += chr(((ord(char) - ord('A') + key) % 26) + ord('A'))
        else:
            result += char
            
    # Output the final result
    if mode == 'e':
        print(f"\nEncrypted message: {result}")
    else:
        print(f"\nDecrypted message: {result}")

if __name__ == "__main__":
    caesar_cipher_tool()