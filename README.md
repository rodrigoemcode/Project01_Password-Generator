# Project01 Password Generator
### README

---


## password_generator_v0.py

**Description:**
This file contains a simple script that generates a single random password.

**Operation:**
The script uses Python's `random` and `string` modules to generate a random password with a specified length. The password consists of uppercase letters, lowercase letters, digits, and punctuation characters.

**Usage:**
To use this script:
1. Set the desired password length by modifying the `password_length` variable.
2. Run the script and it will print the generated password to the output.

---
## password_generator_v1.py

**Description:**
This file contains a more advanced script that generates multiple random passwords with configurable options.

**Operation:**
The script defines a function `generate_random_password` that allows specifying the password length and which types of characters to include (uppercase letters, lowercase letters, digits, and symbols). It ensures that at least one character of each selected type is present in each generated password.

**Usage:**
To use this script:
1. Modify the `length` and `amount` variables in the `main()` function to adjust the desired password length and quantity.
2. Run the script to generate and print the random passwords.
