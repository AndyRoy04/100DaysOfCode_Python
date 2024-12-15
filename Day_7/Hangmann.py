# HangMan Project
import random
import Hang_arts, Hang_words

chosen_word = random.choice(Hang_words.word_list)
print(chosen_word)

placeholder = ""

for letter in chosen_word:
    placeholder += "-"

letter_list = []
game_over = False
lives = 6

print(Hang_arts.logo)

while not game_over:    

    print(f"\n**************************** You have {lives}/6 lives left ****************************")
    guess = input("Guess a letter : ").lower()
    display = ""
    if guess in letter_list:
        print(f"You've already guessed : {guess}")

    for letter in chosen_word:
        if letter == guess:
            display += letter
            letter_list.append(letter)
        elif letter in letter_list:
            display += letter
        else:
            display += "-"

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            print("**************************** You lose😒!! ****************************\n The word was : " + chosen_word)
            game_over = True        
    
    print(Hang_arts.stages[lives])
    print(display)
    
    if '-' not in display:
        print("**************************** You win 🦾🍁!****************************\n The word was : " + chosen_word)
        game_over = True

