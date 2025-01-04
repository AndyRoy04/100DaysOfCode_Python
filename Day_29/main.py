from tkinter import *


window = Tk()
window.title('Miscellaneous')
window.config(width=500, height=400, bg='gray45')

r = Label(width=30, height=5, bg='red')
r.grid(column=0, row=0)

g = Label(width=30, height=5, bg='green')
g.grid(column=1, row=1)

b = Label(width=60, height=5, bg='blue')
b.grid(column=0, row=2, columnspan=2)



window.mainloop()