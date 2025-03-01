from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

DARK = 'gray15'
GRAY2 = 'gray27'
LIGHT = 'snow'
FONT = ('Arial', 10)
BLUE = 'RoyalBlue4'

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
                'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 
                'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for letter in range(randint(8, 10))]
    password_list += [choice(numbers) for number in range(randint(2, 4))]
    password_list += [choice(symbols) for symbol in range(randint(2, 4))]
        
    shuffle(password_list)
    string_password = ''.join(password_list)

    if len(password_entry.get()) > 0:
        password_entry.delete(0, END)
    password_entry.insert(0, string_password)
    pyperclip.copy(string_password)

# ---------------------------- SEARCG PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get().title()   # This line converts the website into title case format
    
    try:
        with open('100DaysOfCode_Python/Day_29/password-manager-start/password_handler.json', 'r') as website_data:
            data = json.load(website_data)
    except FileNotFoundError:
        messagebox.showerror(title='Error', message='No data file found')
    else:
        if len(website) == 0:
            messagebox.showerror(title='Error', message='Please enter a website')
        elif website in data:
            messagebox.showinfo(title=website, message=f"Username: {data[website]['username']}\n"
                                f"Password: {data[website]['password']}")
            website_entry.delete(0, END)
        else:
            messagebox.showinfo(title=website, message='No details found for this website.')

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    data_dictionary = {
        website.title(): {      # This line converts the website into title case format
            'username': username,
            'password': password
        }
    }
    
    if website == '' or username == '' or password == '':
        messagebox.showinfo(title='Oops', message="Please don't leave any fields blank!")
    else:
        try:
            with open('100DaysOfCode_Python/Day_29/password-manager-start/password_handler.json', 'r') as data_entered:
                data = json.load(data_entered)  #  Loading the old data from the json file 
                data.update(data_dictionary)    #  updating old json data with new data
        except FileNotFoundError:
            with open('100DaysOfCode_Python/Day_29/password-manager-start/password_handler.json', 'w') as data_entered:
                json.dump(data_dictionary, data_entered, indent=4)  # saving updated data
        else:
            with open('100DaysOfCode_Python/Day_29/password-manager-start/password_handler.json', 'w') as data_entered:
                json.dump(data, data_entered, indent=4, sort_keys=True)  # saving updated data
        finally:                
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Buddy')
window.config(padx=50, pady=50, bg=DARK)

canvas = Canvas(width=200, height=200, bg=DARK, highlightthickness=0)
bg_image = PhotoImage(file='100DaysOfCode_Python/Day_29/password-manager-start/logo.png')
canvas.create_image(100, 100, image=bg_image)
canvas.grid(row=0, column=1)

# Website label and entry
website_label = Label(text='Website: ', fg=LIGHT, bg=DARK, font=FONT)
website_label.grid(row=1, column=0)

website_entry = Entry(width=33, fg=LIGHT, bg=GRAY2, borderwidth=0)
website_entry.focus()
website_entry.grid(row=1, column=1)

# Username/Email label and entry
username_label = Label(text='Email/Username: ', fg=LIGHT, bg=DARK, font=FONT)
username_label.grid(row=2, column=0)

username_entry = Entry(width=43, fg=LIGHT, bg=GRAY2, borderwidth=0)
username_entry.insert(END, 'passwordbuddy25@gmail.com')  # Placeholder with your default username or email address
username_entry.grid(row=2, column=1, columnspan=2)

# Password label and entry
password_label = Label(text='Password: ', fg=LIGHT, bg=DARK, font=FONT)
password_label.grid(row=3, column=0)

password_entry = Entry(width=33, fg=LIGHT, bg=GRAY2, borderwidth=0)
password_entry.grid(row=3, column=1)

# Search Button
search_button = Button(text='Search', width=7, fg=LIGHT, bg=BLUE, command=find_password)
search_button.grid(row=1, column=2)

# Generate Password button
generate_password_button = Button(text='Generate', fg=LIGHT, bg=BLUE, command=generate_password)
generate_password_button.grid(row=3, column=2)

# Save password Button
add_button = Button(text='Add', width=36, fg=LIGHT, bg=BLUE, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()