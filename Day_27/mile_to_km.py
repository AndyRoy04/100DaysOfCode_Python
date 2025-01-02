from tkinter import *

window = Tk()
window.title('Mile to Km Converter')
window.minsize(width=250, height=150)
window.config(padx=30, pady=30)

# Function to convert Miles to Km
def milesToKm():
    if my_entry.get() == '' or type == str:
        conversion_label.config(text='Invalid input')
    else:
        miles = float(my_entry.get())
        kilometer = miles * 1.60934
        conversion_label.config(text=f'{round(kilometer, 2)}')

# Getting the users entry
my_entry = Entry(width=10)
my_entry.insert(END, string='')
my_entry.grid(column=1, row=0)

# Displaying the Miles text
miles_label = Label(text='Miles')
miles_label.grid(column=2, row=0)

# Displaying the text that states the conversion
text_label = Label(text='is equal to')
text_label.grid(column=0, row=1)

# Displaying the conversion result in Km
conversion_label = Label(text='0')
conversion_label.grid(column=1, row=1)
conversion_label.config(padx=5, pady=5)

# Displaying the Km text
kilometers_label = Label(text='Km')
kilometers_label.grid(column=2, row=1)

# Button to execute the conversion
calculate_button = Button(text='Calculate', command=milesToKm)
calculate_button.grid(column=1, row=2)

window.mainloop()