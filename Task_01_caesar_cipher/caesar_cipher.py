letters= 'abcdefghijklmnopqrstuvwxyz'
num_letters= len(letters)

# Encryption and Decryption functions
# Older version kept for learning and comparison

# def encrypt(plaintext, key):
#     ciphertext=' '
#     for letter in plaintext:
#         letter= letter.lower()
#         if not letter == ' ':
#             index= letter.find(letter)
#             if index == -1:
#                 ciphertext += letter
#             else:
#                 newindex= index + key
#                 if new_index >= 26:
#                     new_index -= 26
#                 ciphertext += letters[new_index]
#     return ciphertext

# def decrypt(ciphertext, key):
#     plaintext=' '
#     for letter in plaintext:
#         letter= letter.lower()
#         if not letter == ' ':
#             index= letter.find(letter)
#             if index == -1:
#                 plaintext += letter
#             else:
#                 new_index= index - key
#                 if new_index >0:
#                     new_index += 26
#                 plaintext += letters[new_index]
#     return plaintext

# Combined function for encryption and decryption
def encrypt_decrypt(text, mode, key):
    result = ""
    shift = -key if mode == 'decrypt' else key

    for ch in text:
        if ch.islower():
            index = letters.find(ch)
            result += letters[(index + shift) % num_letters]
        elif ch.isupper():
            lower_index = letters.find(ch.lower())
            result += letters[(lower_index + shift) % num_letters].upper()
        else:
            result += ch

    return result


def main():
    print("*--*CAESAR CIPHER*--*")
    while True:
        mode = input("Type 'encrypt' or 'decrypt': ").strip().lower()
        if mode in ("encrypt", "decrypt"):
            break
        print("Please type the full word 'encrypt' or 'decrypt'.")
    while True:
         try:
            key = int(input("Enter the key (1 through 26): "))
            if not 1 <= key <= 26:
                print(f"Key {key} must be in between 1 to 26. Try again.")
                continue
            break
         except ValueError:
             print("Invalid input. Please enter a number between 1 and 26.")

    text = input("Enter the message: ")
    result = encrypt_decrypt(text, mode=mode, key=key)
    print(f"Result is: {result}") 
    
    
if __name__ == "__main__":
    main()
