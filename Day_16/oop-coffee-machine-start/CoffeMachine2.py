from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# menuItem = MenuItem()
menu = Menu()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()

choice_list = ['espresso', 'latte', 'cappuccino', 'report', 'off']

machine_active = True
while machine_active:
    choice = input(f"What would you like? ({menu.get_items()}) : ")
    while choice.lower() not in choice_list:
        choice = input(f"What would you like? ({menu.get_items()}) : ")

    if choice == "report":
        coffeeMaker.report()
        moneyMachine.report()
    elif choice == "off":
        machine_active = False
    else:
        drink = menu.find_drink(choice)
        if coffeeMaker.is_resource_sufficient(drink):
            cost = drink.cost
            if moneyMachine.make_payment(cost):
                coffeeMaker.make_coffee(drink)


