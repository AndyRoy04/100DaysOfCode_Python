# #------------------ Dealing With Errors and exceptions ----------------- #

# FileNotFoundError
# with open('unknown_file.txt', 'r') as file:
#     file.read()

# KeyNotFoundError  
# dictionary = {'key': 'value'}
# print(dictionary['non_existent_key'])  

# TypeError
# print(5 + 'a')

# IndexError
# list = [1, 2, 3]
# print(list[4])

# NameError
# print(lazy)

# Catching Errors
# try:
#     # Code that might raise an exception
#     file = open('hello.txt')
#     a_dict = {'a': 1, 'b': 2, 'c': 3}
#     print(a_dict['c'])
# except FileNotFoundError:
#     # Code to execute when exception occurs
#     file = open('100DaysOfCode_Python/Day_30/hello.txt', 'w')
#     file.write('Maniacs are present')
# except KeyError as error:
#     # Code to execute when exception occurs
#     print(f"The key '{error}' does not exist in the dictionary.")
# else:
#     # Code to execute if no exception occurs
#     print('No exceptions occurred.')
#     print(file.read())
# finally:
#     # Code to execute regardless of whether an exception occurred or not
#     # file.close()
#     raise TypeError("It's fun crashing codes")


# # bmi
# height = float(input("Height: "))
# weight = float(input("Weight: "))

# if height > 3:
#     raise ValueError("Height should be less than or equal to 3 meters")

# bmi = weight / (height ** 2)
# print(bmi)

# facebook_posts = [
#     {'Likes': 21, 'Comments': 2},
#     {'Likes': 13, 'Comments': 2, 'Shares': 1},
#     {'Likes': 33, 'Comments': 8, 'Shares': 3},
#     {'Comments': 4, 'Shares': 2},
#     {'Comments': 1, 'Shares': 1},
#     {'Likes': 19, 'Comments': 3}
# ]


# def count_likes(posts):

#     total_likes = 0
#     for post in posts:
#         try:
#             total_likes = total_likes + post['Likes']
#         except KeyError:
#             total_likes += 0
    
#     return total_likes


# count_likes(facebook_posts)
