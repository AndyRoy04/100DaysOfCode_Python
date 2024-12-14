# randomisation in python
import random

# generates random integers
# random_number = random.randint(5, 42)
# print(random_number)

# generates random floating point numbers from 0 to and not including 1
# random_number = random.random() * 10
# print(random_number)

# # heads or tail rnadom generator
# random_number = random.randint(0, 1)
# if random_number == 0:
#     print("Heads")
# else:
#     print("Tails")

# random name generator
import my_module
name = random.choice(my_module.african_names)
# names = my_module.african_names
# random_number = random.randint(0, 14)
print(name)

# consonants = ['g', 'b', 'c', 'd', 'e', 'f']
# vowels = ['a', 'e', 'i']
# two_list = [consonants, vowels]
# print(two_list[1][1])