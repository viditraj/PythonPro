import random
small_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    password = ""
    n_small_letters = random.randint(8, 10)
    n_capital_letters = random.randint(2, 4)
    n_symbols = random.randint(2, 4)
    n_numbers = random.randint(2, 4)

    for i in range(0, n_small_letters):
        password += random.choice(small_letters)
    for i in range(0, n_symbols):
        password += random.choice(symbols)
    for i in range(0, n_numbers):
        password += random.choice(numbers)
    for i in range(0, n_capital_letters):
        password += random.choice(capital_letters)
    random_order = list(password)
    random.shuffle(random_order)
    final_password = ''.join(random_order)
    return final_password
