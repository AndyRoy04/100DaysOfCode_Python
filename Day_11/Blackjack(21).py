# Building a BlackJack game
from art import logo
import random
from os import system

first_part = True
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal(user_cards, computer_cards):
    if sum(user_cards) == sum(computer_cards):
        print("Draw 🫱🏾‍🫲🏾")
        start = False
    elif sum(computer_cards)> 21:
        print("Opponent went over. You win. 🏆") 
        start = False
    elif sum(user_cards) > 21:
        print("You went over. You lose. 😰")
        start = False
    elif sum(computer_cards) > sum(user_cards):
        print("You Lose 😓")
        start = False
    elif sum(user_cards) > sum(computer_cards):
        print("You Win 🥳")
        start = False
    else:
        print("You lose. 😿")
        start = False
    print(user_cards, computer_cards)
    
while first_part:

    user_cards = []
    computer_cards = []
    start = True    

    game_start = input("Do you want to start the game ? (y/n): ").lower()
    system("cls")
    if game_start == "y":
        print(logo)
        for i in range(2):
            user_cards.append(random.choice(cards))
            computer_cards.append(random.choice(cards))

        while sum(computer_cards) < 17:
            computer_cards.append(random.choice(cards))
            if sum(computer_cards) > 21:
                deal(user_cards, computer_cards)
                start = False

        print(f"Your cards : {user_cards}, current score : {sum(user_cards)}")
        print(f"Computer's first card : {computer_cards[0]}")

        if sum(computer_cards) == 21 and len(computer_cards) == 2:
            print("Computer has a Blackjack. You lose! 😱")
            start = False
        elif sum(user_cards) == 21 and len(user_cards) == 2:
            print("You have a Blackjack. You win! 😎")
            start = False
        
        if sum(user_cards) > 21:
            print("You went over. You lose! 😭")
            start = False

        while start:                  

            another_cards = input("Type 'y' to get another card, type 'n' to pass : ").lower()

            if another_cards == "y":
                user_cards.append(random.choice(cards))
                print(f"Your cards : {user_cards}, current score : {sum(user_cards)}")
                print(f"Computer's first card : {computer_cards[0]}")
                if sum(user_cards) > 21:
                    deal(user_cards, computer_cards)
                    start = False
            else:
                print(f"Your final hand : {user_cards}, final score : {sum(user_cards)}")
                print(f"Computer's final hand : {computer_cards}")
                deal(user_cards, computer_cards)
                start = False
    else:
        first_part = False
