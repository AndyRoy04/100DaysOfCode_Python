from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
GREEN = "green4"
RED = "tomato"
ORANGE = "OrangeRed4"
BLUE = "#00ffff"
DARK = 'gray15'
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)  #how to cancel timer
    canvas.itemconfig(timer_text, text='00:00')
    timer_label.config(text='Timer', fg=GREEN)
    check_mark.config(text='')
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_time = WORK_MIN * 60
    short_break_time = SHORT_BREAK_MIN * 60
    long_break_time = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        countdown(long_break_time)    # Get long break
        timer_label.config(text='Break', fg=BLUE)
    elif reps % 2 == 0:
        countdown(short_break_time)    # Get short break
        timer_label.config(text='Break', fg=RED)
    else:
        countdown(work_time)   # Work normal minutes
        timer_label.config(text='Work', fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_mins = math.floor(count / 60) # minutes
    count_secs = count % 60 # seconds
    if count_secs < 10:
        count_secs = f'0{count_secs}'
    
    canvas.itemconfig(timer_text, text=f'{count_mins}:{count_secs}')   # How to configure a canvas text (Save in an attribute before changing)
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)    # Save time in variable if we need to cancel it later on
    else:
        start_timer()
        marks = ''
        working = math.floor(reps/2) # Number of times we should be working
        
        for i in range(working):
            marks += '✓'
        check_mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro Timer')
window.config(padx=100, pady=50, bg=DARK)

# --- Timer Text ---#
timer_label = Label(text='Timer', bg=DARK, fg=GREEN, font=(FONT_NAME, 50))
timer_label.grid(column=1, row=0)

# Apple and in text
canvas = Canvas(width=200, height=224, bg=DARK, highlightthickness=0)
tomato_img = PhotoImage(file='100DaysOfCode_Python/Day_28/pomodoro-start/tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

# --- Buttons ---#
start_button = Button(text='Start', command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', command=reset_timer)
reset_button.grid(column=2, row=2)

# --- Check Mark ---#
check_mark = Label(fg=ORANGE, bg=DARK, font=(FONT_NAME, 15, 'bold'))
check_mark.grid(column=1, row=3)


window.mainloop()