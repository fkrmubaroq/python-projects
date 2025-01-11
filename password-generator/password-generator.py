import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy
password_generator = ""
for _ in range(nr_letters):
    random_index = random.randint(0, len(letters) - 1)
    password_generator += letters[random_index]

for _ in range(nr_symbols):
    random_index = random.randint(0, len(symbols) - 1)
    password_generator += symbols[random_index]

for _ in range(nr_numbers):
    random_index = random.randint(0, len(numbers) - 1)
    password_generator += numbers[random_index]

print(f"Easy level Password : {password_generator}")


# Hard
password = ""
is_letter = 0
is_number = 1
is_symbol = 2
compound_inputs =[
    letters,
    numbers,
    symbols
]

letter_used = 0
number_used = 0
symbol_used = 0

total_character = nr_letters + nr_symbols + nr_numbers
while len(password) != total_character:
    random_inputs_index = random.randint(0, len(compound_inputs) - 1)
    selected_inputs = compound_inputs[random_inputs_index]
    random_character_index = random.randint(0, len(selected_inputs) - 1)
    random_character = selected_inputs[random_character_index]

    if random_inputs_index == is_letter and letter_used < nr_letters:
        letter_used += 1
        password += random_character
        continue

    if random_inputs_index == is_number and number_used < nr_numbers:
        number_used += 1
        password += random_character
        continue

    if random_inputs_index == is_symbol and symbol_used < nr_symbols:
        symbol_used += 1
        password += random_character
        continue

print(f"Hard level Password : {password}")

