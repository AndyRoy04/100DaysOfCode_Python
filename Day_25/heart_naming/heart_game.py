import turtle
import pandas

screen = turtle.Screen()
screen.title('Hearth Naming Game')
image = '100DaysOfCode_Python/Day_25/heart_naming/heart_name.gif' # Setting a new backgroud to ba an image
screen.addshape(image) # Adding the background image to turtles shape
turtle.shape(image)

def write_to_screen(state, x, y, color):
    '''Write the state at the specified location to the screen'''
    name = turtle.Turtle()
    name.hideturtle()
    name.penup()
    name.color(color)
    name.goto(x, y)
    name.write(state, align='center', font=('comic sans', 14, 'normal'))

STATE_DATA = pandas.read_csv('100DaysOfCode_Python/Day_25/heart_naming/hearth_parts.csv') # Convering CSV to pandas
HEART_LIST = STATE_DATA.parts.to_list()
X_COOR_LIST = STATE_DATA.x.to_list()
Y_COOR_LIST = STATE_DATA.y.to_list()

game_on = True
correct_parts = []
title_text = 'Guess the Part of the heart'

while game_on:
    answer_part = screen.textinput(title=title_text, prompt='Enter a Part of the heart :').title()

    if answer_part == 'Exit' or len(correct_parts) == len(HEART_LIST):   # Secrete key to exit the infinite loop
        game_on = False
    if answer_part == 'Correct Me':    # Secrete key to get the correction
        for name in HEART_LIST:
            if name not in correct_parts:
                i = HEART_LIST.index(name)  # Getting the index of the wrong state
                write_to_screen(name, X_COOR_LIST[i], Y_COOR_LIST[i], color='red')
            # write_to_screen(HEART_LIST[i], X_COOR_LIST[i], Y_COOR_LIST[i], color='red')
        break
    if answer_part in HEART_LIST:     # Checking if the user guessed something right
        if answer_part not in correct_parts:      # Checking if the user choice already exists
            correct_parts.append(answer_part)
            index = HEART_LIST.index(answer_part)   # Getting the index of the correct state
            write_to_screen(HEART_LIST[index], X_COOR_LIST[index], Y_COOR_LIST[index], color='black')
    
    title_text = f'{len(correct_parts)}/{len(HEART_LIST)} Parts Correct' 
    
turtle.mainloop()