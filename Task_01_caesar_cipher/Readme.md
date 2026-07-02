## Caesar Cipher

This is a small command-line Caesar cipher program in Python. It shifts each alphabetic character by a key you choose and works for both encryption and decryption.

## Requirements
- Python 3.8+

## Usage
1. Run the script:
   ```bash
   python caesar_cipher.py
   ```
2. When prompted, type `encrypt` or `decrypt`.
3. Enter a key from 1 to 26.
4. Enter the message.

Example session:
```text
*--*CAESAR CIPHER*--*
Type 'encrypt' or 'decrypt': encrypt
Enter the key (1 through 26): 3
Enter the message: attack at dawn
Result is: dwwdfn dw gdzq
```

## Notes
- Non-letter characters pass through unchanged.
- Uppercase and lowercase letters are both supported.
- Keys wrap around the alphabet; a key of 26 returns the original text.

  
                                  ----------------_______----------------
