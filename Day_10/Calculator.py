# Calculator program
from art import logo
from os import system
import sys

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def divide(a, b):
    return a / b
def multiply(a, b):
    return a * b
def modulo(a, b):
    return a % b

calcualtor_operations = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply,
    "%": modulo,
}

def firsr_part():
    print(logo + "\n")
    begin = True
    num1 = float(input("Enter the first number : "))

    while begin:
        for operation in calcualtor_operations:
            print(operation)
        user_operation = input("Pick an operation : ")
        num2 = float(input("Enter the second number : "))
        result = round(calcualtor_operations[user_operation](num1, num2), 5) # rounds the answer to 3 decimal places
        print(f"{num1} {user_operation} {num2} = {result}")

        restart = input(f"Type 'y' to continue calculating with {result}. Type 'n' to start a new calculation. Type 'e' to exit calculator : ").lower()
        if restart == 'y':
            num1 = result
        elif restart == 'e':
            begin = False
            sys.exit("\nExiting calculator........")
        else:
            system("cls")
            firsr_part()


firsr_part()
