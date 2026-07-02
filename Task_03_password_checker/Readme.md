## Password Strength Checker

An easy-to-use tool to check the strength of passwords and provide feedback on how to improve them.

## Requirements

- Python 3.6 or higher
- No external dependencies
  
## Features

- **Interactive password strength checking** - Prompts for a password and evaluates it locally
- **Detailed feedback** - Specific suggestions for password improvement
- **4 strength labels**:
  - STRONGER (if all criteria met)
  - STRONG (if 4 criteria met)
  - MODERATE (if 3 criteria met)
  - WEAK (less than 3 criteria met)

## Password Strength Criteria

A password is evaluated based on the following criteria:
1. Minimum 8 characters in length
2. Contains at least one digit (0-9)
3. Contains at least one uppercase letter (A-Z)
4. Contains at least one lowercase letter (a-z)
5. Contains at least one special character (@*&?%..)

## Run

Run the password strength checker:

```bash
python pass_check.py
```

The tool will:
1. Display a welcome message
2. Prompt you to enter a password with hidden input
3. Display the password strength level
4. Show suggestions for improvement if needed
5. Repeat until you type `exit` to quit

### Example

```
^-_-^ welcome to password strength checker ^-_-^
enter your password to check: (or type 'exit' to quit): ••••••••

Your password strength is: MODERATE
Suggestions to improve:
weak: password must contain upper characters
weak: password must contain a special character
```

## Security Notes

- Passwords are hidden when typed using the `getpass` module
- Passwords are not stored or logged
- This tool is for local use only

## License
This project is open source and available for educational purposes.


                                  ----------------_______----------------
