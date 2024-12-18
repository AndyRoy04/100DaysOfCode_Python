# Debugging and testing

# def my_function():
#     for i in range(1, 21): # change 20 to 21 in the range
#         if i == 20:
#             print("You got it")
# my_function()

# from random import randint
# dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5) # Chgange the range from 1 to 6 ro 0 to 5
# print(dice_num)
# print(dice_images[dice_num])

# year = int(input("What's your year of birth?"))

# if year > 1980 and year < 1994:
#     print("You are a millennial.")
# elif year >= 1994: # change the sign to >=
#     print("You are a Gen Z.")

# try:
#     age = int(input("How old are you?"))
# except ValueError:
#     print("That's not a valid age!. Try again with a numeric value like 18")
#     age = int(input("How old are you?"))
# # Make sure the user know the error by using the try/except operator as shown above
# if age > 18:
#     print(f"You can drive at age {age}.")
# else:
#     print("You can't drive yet.") # change the print to else: print statement


# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: ")) # chnage the double equals sign to single equals sign
# total_words = pages * word_per_page
# print(total_words)


# import random
# import maths

# def mutate(a_list):
#     b_list = []
#     new_item = 0
#     for item in a_list:
#         new_item = item * 2
#         new_item += random.randint(1, 3)
#         new_item = maths.add(new_item, item)
#         b_list.append(new_item) # send the append in the loop so as to get the whole list
#     print(b_list)

# mutate([1, 2, 3, 5, 8, 13])
