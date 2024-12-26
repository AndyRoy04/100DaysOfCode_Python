# Using the with key word to open and close a file
# with open("100DaysOfCode_Python\Day_24\my_file.txt") as file:
#     content = file.read()
#     print(content)


with open("100DaysOfCode_Python\Day_24\my_file.txt", mode='r') as file:
    content = file.readlines()
    print(content)

