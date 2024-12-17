from os import system
from art import logo
import random

def display_text():
    global user_guess
    print(f"\t\t\t\tYou have {attempts} attempts remaining to guess the number")
    user_guess = int(input("\t\t\t\tMake a guess : "))
    return user_guess

def compare_guesses(user_guess, computer_guess):
    global attempts
    global game_over

    if user_guess == computer_guess:
        print(f"\n\t\t\t\tYay🥳, you've guessed the number {computer_guess} correctly!\n")
        game_over = True
    elif user_guess < computer_guess:
        print("\t\t\t\tToo low!\n")
        attempts -= 1
    else:
        print("\t\t\t\tToo high!\n")
        attempts -= 1

while input("\n\t\t\t\tDo you want to play my Number Guessing Game ? (y/n) : ").lower() == "y":
    system("cls")
    computer_guess = random.choice(range(1, 101))
    user_guess = 0
    print(computer_guess)

    print(logo)
    print("\t\t\t\tWelcome to the Number Guessing Game! 🔢")
    print("\t\t\t\tI'm thinking of a number between 1️⃣  and 1️⃣ 0️⃣ 0️⃣. ")
    level = input("\t\t\t\tChoose a difficulty. Type 'easy' or 'hard': ").lower()

    if level == 'easy':
        attempts = 10
    else:
        attempts = 5

    game_over = False
    while not game_over:
        
        display_text()
        compare_guesses(user_guess, computer_guess)

        if attempts == 0:
            print(f"\t\t\t\tYou've run out of guesses😓, my guess was : {computer_guess}")
            game_over = True
        elif user_guess != computer_guess:
            print("\t\t\t\tGuess again")

print("\n\t\t\t\tSee you next time 😁😁")