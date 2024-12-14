# Rock, Paper, and Scissors game
import random
import my_module

print("Welcome to the Rock, Paper, and Scissors game")
users_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if 0 <= users_choice <= 2:
    print(my_module.RPS[users_choice])

computer_choice = random.randint(0, 2)
print("computer chose")
print(my_module.RPS[computer_choice])

if users_choice == 0 and computer_choice == 1:
    print("You Lose!")
elif users_choice == 1 and computer_choice == 2:    
    print("You Lose!")
elif users_choice == 2 and computer_choice == 0:    
    print("You Lose!")
elif users_choice == 0 and computer_choice == 2:    
    print("You Won!")
elif users_choice == 1 and computer_choice == 0:    
    print("You Won!")
elif users_choice == 2 and computer_choice == 1:    
    print("You Won!")
elif users_choice == computer_choice:    
    print("It's a draw!")
else:
    print("Wrong input. You Lose!")
# print(my_module.RPS[0])
