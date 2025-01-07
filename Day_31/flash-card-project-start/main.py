from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ('Ariel', 40, 'italic')
WORD_FONT = ('Ariel', 60, 'bold')
FINISHED_FONT = ('Comic Sans', 20, 'italic')

random_card = {}
to_learn = {}

# --------- Try and Catch for file Error
try:
    file_location = '100DaysOfCode_Python/Day_31/flash-card-project-start/data/to_learn.csv'
    data = pandas.read_csv(file_location)
except FileNotFoundError:
    file_location = '100DaysOfCode_Python/Day_31/flash-card-project-start/data/french_words.csv'
    original_list = pandas.read_csv(file_location)
    to_learn = original_list.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')
    


# ------------------ CHANGE CARDS ---------------- #
def change_card():
    global random_card, timer
    window.after_cancel(timer)
    
    if len(to_learn) == 0:
        canva.itemconfig(word_text, fill='gray40', text="You've learned all Todays' words", font=FINISHED_FONT)
    else:
        random_card = random.choice(to_learn)
        canva.itemconfig(face_image, image=front_image_location)
        canva.itemconfig(language_text, fill='black', text='French')
        canva.itemconfig(word_text, fill='black', text=random_card['French'])

        timer = window.after(3000, flip_card)

# ------------------ KNOWN CARDS ---------------- #
def known_cards():
    if len(to_learn) != 0:  # Check if card list is not empty
        to_learn.remove(random_card)
        data = pandas.DataFrame(to_learn)
        data.to_csv('100DaysOfCode_Python/Day_31/flash-card-project-start/data/to_learn.csv', index=False)
        change_card()

# ------------------ FLIP CARDS ---------------- #
def flip_card():
    canva.itemconfig(language_text, fill='white', text='English')
    canva.itemconfig(word_text, fill='white', text=random_card['English'])
    canva.itemconfig(face_image, image=back_image_location)
    
    

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

timer = window.after(3000, flip_card)  # start timer for first card

back_image_location = PhotoImage(file='100DaysOfCode_Python/Day_31/flash-card-project-start/images/card_back.png')
front_image_location = PhotoImage(file='100DaysOfCode_Python/Day_31/flash-card-project-start/images/card_front.png')

canva = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
face_image = canva.create_image(400, 263, image=front_image_location)
language_text = canva.create_text(400, 190, text='', font=LANGUAGE_FONT)
word_text = canva.create_text(400, 293, text='', font=WORD_FONT)
canva.grid(row=0, column=0, columnspan=2)

right_image = PhotoImage(file='100DaysOfCode_Python/Day_31/flash-card-project-start/images/right.png')
wrong_image = PhotoImage(file='100DaysOfCode_Python/Day_31/flash-card-project-start/images/wrong.png')

wrong_button = Button(image=wrong_image, text='wrong', highlightthickness=0, command=change_card)
wrong_button.grid(row=1, column=0)

right_button = Button(image=right_image, text='right', highlightthickness=0, command=known_cards)
right_button.grid(row=1, column=1)

change_card()

window.mainloop()