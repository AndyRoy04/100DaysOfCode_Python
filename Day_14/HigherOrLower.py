from GameData import data
from art import logo, vs
from os import system
import random

def random_choice():
    ''' This function returns a random data from the GameData list '''
    return random.choice(data)

def compare(a, b, user_choice):
    ''' This function compares the user's choice with the data 
    from the GameData list and returns true if the user is right.''' 
    global score
    A_followers = a['follower_count']
    B_followers = b['follower_count']

    if user_choice == 'a':
        if A_followers > B_followers:
            score += 1
            return True
        # else:
        #     return False
    elif user_choice == 'b':
        if B_followers > A_followers:
            score += 1
            return True
    #     else:
    #         return False
    # # else:
    # #     return False

def change_if_equal():
    ''' This function changes the random_choice_B to a new random choice if it is equal to random_choice_A '''
    global random_choice_A, random_choice_B
    not_same = True
    while not_same:
        if random_choice_A == random_choice_B:
            random_choice_B = random_choice()
        else:
            not_same = False
    return random_choice_B
def feedback():
    ''' This function gives the user their score and changes the values of A and B depending on the user choice'''
    global random_choice_A, random_choice_B
    print(f"\t\t\t\t You're right! Current Score: {score}")
    random_choice_A = random_choice_B
    random_choice_B = random_choice()

    change_if_equal()

random_choice_A = random_choice()
random_choice_B = random_choice()
change_if_equal()

score = 0
game_over = False

system('cls')
print(logo)
while not game_over:

    print(f"\t\t\t\t Compare A: {random_choice_A['name']}, {random_choice_A['description']}, from {random_choice_A['country']}")
    print(vs)
    print(f"\t\t\t\t Againts B: {random_choice_B['name']}, {random_choice_B['description']}, from {random_choice_B['country']}")

    user_choice = input("\t\t\t\t Who has more followers? Type 'A' or 'B' : ").lower()

    if compare(a = random_choice_A, b = random_choice_B, user_choice = user_choice) == True:
        system('cls')
        print(logo)
        feedback()
    else:
        system('cls')
        print(logo)
        print(f"\t\t\t\t Sorry, that's wrong. Final Score: {score}")
        print(f"\t\t\t\t {random_choice_A['name']} has {random_choice_A['follower_count']} followers and {random_choice_B['name']} has {random_choice_B['follower_count']}")
        game_over = True