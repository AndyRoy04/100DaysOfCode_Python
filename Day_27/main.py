from tkinter import *

# Function to handle button click event
def button_click():
    input_text = my_entry.get()
    my_label.config(text=input_text,font=('comics sans', 30))

window = Tk()
window.title('My GUI with Tkinter')
window.minsize(600, 400)

# Label
my_label = Label(text='Hello GUI', font=('Arial', 24))
my_label.configure(text='My GUI World')
my_label.grid(column=0, row=0)


# Button
my_button = Button(text='Click me', command=button_click)
my_button.grid(column=1, row=1)

# New Button
new_button = Button(text='New Button')
new_button.grid(column=2, row=0)

# Entry
my_entry = Entry(width=10)
my_entry.insert(END, string='Figaro')
my_entry.grid(column=3, row=2)








window.mainloop()
