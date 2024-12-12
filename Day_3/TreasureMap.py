print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = input("You are at a cross road. Where do you want to go? \n     Type 'left' or 'right' \n").lower()
if direction == 'left':
    wait_swim = input("You've come to a lake. There is an island in the middle of the lake.\n      Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()
    if wait_swim == "wait":
        rooms = input("You arrive at the island unharmed. There is a house with 3 doors.\n    One red, one yellow and one blue. Which colour do you choose?\n").lower()
        if rooms == "red":
            print("You felt into a pit. Game Over")
        elif rooms == "yellow":
            print("You found the treasure! Congratulations!")
        elif rooms == "blue":
            print("You felt in the Ocean. Game Over")
        else:
            print("Wrong color. Game Over")
    elif wait_swim == "swim":
        print("You were eaten by an alligator. Game Over")
    else:
        print("You must type 'wait' or 'swim'. Game Over")
elif direction == "right":
    print("Wrong direction. Game over.")
else:
    print("You must type 'left' or 'right'. Game Over")

