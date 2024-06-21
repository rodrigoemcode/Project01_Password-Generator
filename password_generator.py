import random
import string


def generate_random_password(length, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    """
    Generates a random password based on the specified parameters.

    :param length: Length of the password.
    :param use_upper: Include uppercase letters.
    :param use_lower: Include lowercase letters.
    :param use_digits: Include digits.
    :param use_symbols: Include symbols.
    :return: Generated password.
    """
    if length <= 0:
        raise ValueError("Password length must be greater than zero.")

    all_characters = ''
    if use_upper:
        all_characters += string.ascii_uppercase
    if use_lower:
        all_characters += string.ascii_lowercase
    if use_digits:
        all_characters += string.digits
    if use_symbols:
        all_characters += string.punctuation

    if not all_characters:
        raise ValueError("At least one type of character must be selected.")

    # Ensure the password contains at least one of each selected type
    password = []
    if use_upper:
        password.append(random.choice(string.ascii_uppercase))
    if use_lower:
        password.append(random.choice(string.ascii_lowercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_symbols:
        password.append(random.choice(string.punctuation))