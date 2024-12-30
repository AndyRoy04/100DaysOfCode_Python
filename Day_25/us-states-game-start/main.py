import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S States Game')
image = '100DaysOfCode_Python/Day_25/us-states-game-start/blank_states_img.gif' # Setting a new backgroud to ba an image
screen.addshape(image) # Adding the background image to turtles shape
turtle.shape(image)

# Function to write the states at the desired location
def write_to_screen(state, x, y, color):
    '''Write the state at the specified location to the screen'''
    name = turtle.Turtle()
    name.hideturtle()
    name.penup()
    name.color(color)
    name.goto(x, y)
    name.write(state, align='center', font=('Arial', 8, 'normal'))

STATE_DATA = pandas.read_csv('100DaysOfCode_Python/Day_25/us-states-game-start/50_states.csv') # Convering CSV to pandas
STATES_LIST = STATE_DATA.state.to_list()
X_COOR_LIST = STATE_DATA.x.to_list()
Y_COOR_LIST = STATE_DATA.y.to_list()

game_on = True
correct_states = []
title_text = 'Guess the State'

while game_on:
    answer_state = screen.textinput(title=title_text, prompt='Enter a States name :').title()

    if answer_state == 'Exit' or len(correct_states) == len(STATES_LIST):   # Secrete key to exit the infinite loop
        game_on = False
    if answer_state == 'Correct Me':    # Secrete key to get the correction
        for state in STATES_LIST:
            if state not in correct_states:
                position = STATES_LIST.index(state) 
                write_to_screen(STATES_LIST[position], X_COOR_LIST[position], Y_COOR_LIST[position], color='red')
        break
    if answer_state in STATES_LIST:     # Checking if the user guessed something right
        if answer_state not in correct_states:      # Checking if the user choice already exists
            correct_states.append(answer_state)
            index = STATES_LIST.index(answer_state)   # Getting the index of the correct state
            write_to_screen(STATES_LIST[index], X_COOR_LIST[index], Y_COOR_LIST[index], color='black')
    
    title_text = f'{len(correct_states)}/{len(STATES_LIST)} States Correct'      # Updating the score text


missing_states = []
for state in STATES_LIST:
    if state not in correct_states:
        missing_states.append(state)

missing_states_data = pandas.DataFrame(missing_states)
missing_states_data.to_csv('100DaysOfCode_Python/Day_25/us-states-game-start/missing_states.csv')  # Saving the missing states to a new file

# print(missing_states_data)
turtle.mainloop()