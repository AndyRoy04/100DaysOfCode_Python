import subprocess
import sys
import random
from tkinter import *
from paragraphs import SAMPLE_TEXTS

# ___ Setting the windows dimensions _____
window = Tk()
window.title("Typing Speed Test")
window.minsize(width=500, height=450)
window.maxsize(width=1000, height=800)
window.config(padx=50, pady=25)

# The countdown function
def countdown():    
    global time_left, timer_id
    if time_left > 0:
        timer_label.config(text=f"Time Left: {time_left} s")
        time_left -= 1
        timer_id = window.after(1000, countdown)   #recalling the funtion every single second
    else:
        enter_pressed()
                  
# function to stop the time
def stop_timer():
    global timer_id
    if timer_id is not None:
        window.after_cancel(timer_id)
        timer_id = None  # Reseting the ID    
            
# Starting the counter when any key is been pressed
def any_key_pressed(event):     
    global timer_started
    if not timer_started:
        timer_started = True
        countdown()
        user_entry.bind("<Return>", enter_pressed)  # when the enter key is pressed

# Restarting the whole program.
def restart_program():
    window.destroy()
    script = sys.argv[0]  # getting full path of current running script
    subprocess.Popen([sys.executable, script])
    sys.exit()
    
# Performing calculations after the enter key has been pressed
def enter_pressed(event=None):
    global sample_words, typed_words, correct_words, wrong_words, time_left, restart_button
        
    stop_timer()    # Stopping the countdown
    text_label.config(text='')  # Clear the screen on enter key
    wrong_words_list = []
    
    initial_time = 60
    time_elapsed = initial_time - time_left

    if time_elapsed == 0:
        text_label.config(text=f"Your Typing Speed is : {time_elapsed} WPM", font=("Consolas", 22, "bold"))  
    else:
        typed_text = user_entry.get("1.0", END).strip()
        typed_words = typed_text.split()
        
        timer_label.config(text=f"Completed in : {time_elapsed} s")
        
        for sample_word, typed_word in zip(sample_words, typed_words):
            if sample_word == typed_word:
                correct_words += 1
            else:
                wrong_words += 1 
                wrong_words_list.append(typed_word)
        
        characters_typed = len(typed_text)
        time_in_mins = time_elapsed / 60
            
        raw_WPM = (characters_typed / 5) / time_in_mins   # total typing speed without errors.   
        actual_speed = round(raw_WPM - (wrong_words / time_in_mins))   #  total typing speed with errors.
        if correct_words == 0:
            actual_speed = 0
       
        text_label.config(text=f"Your Typing Speed is : {actual_speed} WPM", font=("Consolas", 22, "bold"))
        
        if wrong_words > 0:
            wrong_label = Label(window, text="Wrong Words: " + ", ".join(wrong_words_list), 
                        font=("Helvetica", 14), fg="red", wraplength=900)
            wrong_label.grid(column=1, row=3, pady=40)
    
    user_entry.destroy()
        
    restart_button = Button(text="Restart", command=restart_program)
    restart_button.grid(column=1, row=4, pady=30)
  
# Global Variables
time_left = 60
timer_started = False
correct_words = 0
wrong_words = 0
timer_id = None

# random sample from our paragraphs module
random_sample = random.choice(SAMPLE_TEXTS)     
sample_words = random_sample.split()

# Printing the Time left to the screen
timer_label = Label(window, text="Time Left: 60 s", font=("Helvetica", 10, "bold"))
timer_label.grid(column=1, row=0, pady=15)

# Printing sample to screen
text_label = Label(text=random_sample, wraplength=900, font=("Consolas", 22, "bold"))   
text_label.grid(column=1, row=1)

# Getting the users entry
user_entry = Text(height=10, width=80, font=("Helvetica", 14, "bold"))
user_entry.focus()
user_entry.bind("<Key>", any_key_pressed)   # when any key is pressed
user_entry.insert(END, '')
user_entry.grid(column=1, row=2, pady=30)
user_entry.config(padx=10, pady=10)

window.mainloop()