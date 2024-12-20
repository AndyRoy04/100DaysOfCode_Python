# # Diving into Object Oriented Programming

# from turtle import Turtle, Screen

# skinny = Turtle()
# my_screen = Screen()
# skinny.shape('turtle')
# skinny.color('green')
# skinny.forward(100)

# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon", ['Pikachu', 'Squirtle', 'Charmander'])
table.add_column("Type", ['Electric', 'Water', 'Fire'])
table.align = 'r'
print(table)

