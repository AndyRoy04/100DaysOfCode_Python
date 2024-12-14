# Random Password generator
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
            'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 
            'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("\nWelcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []

for letter in range(0, nr_letters):
    random_letter = random.choice(letters)
    password_list.append(random_letter)
for number in range(0, nr_numbers):
    random_number = random.choice(numbers)
    password_list.append(random_number)
for symbol in range(0, nr_symbols):
    random_symbol = random.choice(symbols)
    password_list.append(random_symbol)
    
random.shuffle(password_list)
string_password = ''.join(password_list)
print(f"\nYour password is : {string_password}")