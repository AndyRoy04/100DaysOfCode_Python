# Learning about Dictionary and List Comprehension

# name = 'anderson'
# new_name = [letter.upper() for letter in name]
# print(new_name)
# fruits = [ 'apple', 'banana', 'cherry', 'date', 'fig', 'grape', 'kiwi', 'lemon', 'mango', 'orange', 'pear', 'pineapple', 'raspberry', 'strawberry', 'watermelon']
# # double_list = [num**2 for num in range(1, 10)]
# # print(double_list)
# new_list = [fruit.upper() for fruit in fruits if len(fruit) > 6]
# print(new_list)


# # Squaring Numbers
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [num ** 2 for num in numbers]
# print(squared_numbers)


# # Filtering even Numbers
# list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
# numbers = [int(item) for item in list_of_strings]
# result = [num for num in numbers if num%2 == 0]
# print(result)


# # Data Overlap
# first_file = open('file1.txt', 'r')
# file1 = first_file.readlines()

# second_file = open('file2.txt', 'r')
# file2 = second_file.readlines()

# numbers1 = [int(letter) for letter in file1]
# numbers2 = [int(letter) for letter in file2]

# print(numbers1)
# print(numbers2)

# result = [num for num in numbers1 if num in numbers2]
# print(result)


## Random score generator from Dictionary Comprehension
# import random
# names = ['Alberto', 'Bacon', 'Carlita', 'Drake', 'Erica', 'Frankenstein', 
#         #  'George', 'Harry', "Ivan", 'John', 'Karen', 'Lamine', 'Messi', 'Neymare',
#         #  'Oliver', 'Peter', 'Quinn', 'Ronald', 'Sophia', 'Tony', 'Uma', 'Victor', 
#         #  'Winston', 'Xavier', 'Yvonne', 'Zachary'
#          ]
# name_scores = {name:random.randint(1, 100) for name in names}
# print(name_scores)

# high_score = {name:score for name, score in name_scores.items() if score >= 60}
# print(high_score)


# # Temperature in celcius to farenheit from Dictionary comprehension
# weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
# weather_f = {day:((temp*9/5)+32) for day, temp in weather_c.items()}
# print(weather_f)


student_list = {
    "Students": ['George', 'Harry', "Ivan", 'John', 'Karen', 'Lamine', 'Messi', 'Neymare'],
    "Grades": [45, 83, 72, 69, 53, 85, 90, 87]
}
# # Looping through Dictionaries
# for key, value in student_list.items():
#     print(value)

# Looping through a DataFrame
import pandas

student_data = pandas.DataFrame(student_list)
print(student_data)
# # Looping through a DataFrame
# for key, value in student_data.items():
#     print(value)
# Looping through rows of a DataFrame
for index, row in student_data.iterrows():
    if row.Grades < 70:
        print(row.Students, row.Grades)
