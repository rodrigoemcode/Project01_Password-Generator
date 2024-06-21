import random
import string


def generate_random_password(length, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    """
    Gera uma senha aleatória baseada nos parâmetros especificados.

    :param length: Comprimento da senha.
    :param use_upper: Incluir letras maiúsculas.
    :param use_lower: Incluir letras minúsculas.
    :param use_digits: Incluir dígitos.
    :param use_symbols: Incluir símbolos.
    :return: Senha gerada.
    """
    if length <= 0:
        raise ValueError("O comprimento da senha deve ser maior que zero.")

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
        raise ValueError("Pelo menos um tipo de caractere deve ser selecionado.")

    # Garante que a senha contenha pelo menos um de cada tipo selecionado
    password = []
    if use_upper:
        password.append(random.choice(string.ascii_uppercase))
    if use_lower:
        password.append(random.choice(string.ascii_lowercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_symbols:
        password.append(random.choice(string.punctuation))

    # Completa o restante da senha com caracteres aleatórios
    password.extend(random.choice(all_characters) for _ in range(length - len(password)))
    random.shuffle(password)

    return ''.join(password)


def main():
    length = 20
    amount = 10

    for _ in range(amount):
        password = generate_random_password(length)
        print(password)


if __name__ == "__main__":
    main()
