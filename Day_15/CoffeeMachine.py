MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

earnings = 0
from art import logo

def process_coins():
    '''Process and calculate the user's coins'''
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    penny = int(input("How many pennies?: "))
    total = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (penny * 0.01)
    return round(total, 2)

def resources_left(machine_resources, needed_resources, user_choice):
    '''Check if the machine has enough resources to make the drink'''
    for item in needed_resources:
        if machine_resources[item] >= needed_resources[item]:
            machine_resources[item] -= needed_resources[item]            
        else:
            print(f"Sorry there is not enough {item} to make your {user_choice}")
            return False
    return machine_resources

def check_amount(amount_received, cost, user_choice):
    '''Check if the user has enough money to make the drink and returns him some change in case there is'''
    global earnings
    if amount_received >= cost:
        amount_received -= cost
        earnings += cost
        print(f"Here is your change : ${round(amount_received, 2)}")
        print(f"Here is your {user_choice} ☕️. Enjoy!")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

choice_list = ['espresso', 'latte', 'cappuccino', 'report', 'off']

machine_active = True
print(logo)
while machine_active:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    while user_choice not in choice_list:
        print("Invalid choice. Please choose a valid option.")
        user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_choice == 'report':
        print(f"""
            Water : {resources['water']}ml
            Milk : {resources['milk']}ml
            Coffee : {resources['coffee']}g
            Money : ${round(earnings, 2)}
            """)
    elif user_choice == 'off':
        machine_active = False
    else:
        drink = MENU[user_choice]
        if resources_left(resources, drink['ingredients'], user_choice) != False:
            user_amount = process_coins()
            check_amount(user_amount, drink['cost'], user_choice)        
