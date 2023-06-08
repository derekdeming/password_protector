# password generator project 

import random

letters = "abcdefghijklmnopqrstuvwxyz"
letter_list = list(letters)
comma_letters = list("".join(letter_list))
# print(comma_letters)

numbers = "0123456789"
numbers_list = list(numbers)
comma_numbers = list("".join(numbers_list))
# print(comma_numbers)

symbols = "!@#$%^&*()_+"
symbols_list = list(symbols)
comma_symbols = list("".join(symbols_list))
# print(comma_symbols)

print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))

password_list = []

for char in range(1, nr_letters + 1):
    password_list.append(random.choice(comma_letters))

for num in range(1, nr_numbers + 1):
    password_list.append(random.choice(comma_numbers))

for sym in range(1, nr_symbols + 1):
    password_list.append(random.choice(comma_symbols))

print(password_list)

random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")