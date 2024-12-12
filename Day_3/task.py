# rollercoaster game
print("Welcome to the rollercoaster")
height = int(input("What is your height? : "))
bill = 0

if height >= 140:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? : "))

    if age < 12:
        bill = 5
        print("Children pay $5")
    elif age > 18:
        bill = 12
        print("Adults pay $12")
    else:
        bill = 7
        print("Youths pay $7")

    take_pic = input("Will you want a picture? 'y' for YES and 'n' for NO : ")
    if take_pic == 'y':
        bill += 3

    print(f"Your total bill will ${bill}")

else:
    print("You are not tall enough to ride the rollercoaster!")

#Even or Odd
# number = int(input("Enter a number? : "))
# if number < 0:
#     print("This number is negative")
# else:
#     if number % 2 == 0:
#         print("This is a negative number")
#     else:
#         print("This number is odd")

# # Pizza delivery
# print("Welcome to Zee Pizza Deliveries!")
# size = input("What size pizza do you want? S, M or L: ")
# pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")
# total_price = 0

# if size == 'S':
#     total_price += 15
#     if pepperoni == "Y":
#         total_price += 2
#     if extra_cheese == "Y":
#         total_price += 1
# elif size == 'M':
#     total_price += 20
#     if pepperoni == "Y":
#         total_price += 3
#     if extra_cheese == "Y":
#         total_price += 1
# elif size == 'L':
#     total_price += 25
#     if pepperoni == "Y":
#         total_price += 3
#     if extra_cheese == "Y":
#         total_price += 1
# else:
#     print("Invalid size. Please choose S, M or L")

# print(f"Your bill is ${total_price}")
