# # funtions with no input parameter
# def greet():
#     print("Hello, World!")
#     print("Press enter to continue...")
#     print("Press enter to continue...")
# greet()

# # Functions with one parameter(Life in Week calculator):
# def life_in_weeks(age):
#     overall_weeks = 90 * 52
#     weeks_lived = age * 52
#     weeks_left = overall_weeks - weeks_lived
#     print(f"You have {weeks_left} weeks left.")

# age = int(input("Enter your age : "))
# life_in_weeks(age)

# # Functions with multiple parameters
# def greet_with(name, location):
#     print(f"Hello, {name}!")
#     print(f"What is it like in {location}")

# greet_with(location="London", name="Angela")

# Love Calculator function
def calculate_love_score(name1, name2):
    combine_name = name1 + name2
    TRUE = "true"
    LOVE = "love"
    total_true = 0
    total_love = 0
    for letter_of_true in TRUE:
        for letter in combine_name:
            if letter == letter_of_true:
                total_true += 1
    
    for letter_of_love in LOVE:
        for letter in combine_name:
            if letter == letter_of_love:
                total_love += 1
    
    love_percent = str(total_true) + str(total_love)
    print(f"Your compatibility is : {love_percent}%")

name1 = input("Enter first name : ")
name2 = input("Enter second name : ")

calculate_love_score(name1, name2)
