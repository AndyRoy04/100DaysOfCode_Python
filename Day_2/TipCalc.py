# Tip calculator

user_name = input("What is your name? : ")
print(f"Welcome to the Tip Calculator {user_name}")
bill = float(input("What is your bill? : $"))
tip_percent = float(input("What tip percentage will you like to offer? : "))
people = int(input("How many people will split the bill? : "))

tip = (tip_percent / 100) * bill
total_price = (bill + tip)
split_price = round((total_price / people), 2)

print(f"Each person should pay ${split_price}")
