#Write your code below this line
# print("Hello World!\nHello World!\nHello World!")

# This line of code will be executed giving priority to the input() function first
# print("Hello " + input("what is your name? : ") + "!")

# The following lign of code will tell the user the length of their name
name = input("What is your name ? : ")
nameLength = len(name)
print("Hello " + name + "!")
print(f"Your name has " + str(nameLength) + " characters")
