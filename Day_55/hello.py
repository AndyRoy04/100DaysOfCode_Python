from flask import Flask

app = Flask(__name__)

# decoarator to make an HTML element bold
def make_bold(func):
    def bolder(**kwargs):
        return f"<b>{func(**kwargs)}</b>"
    return bolder
# decoarator to make an HTML element emphasized
def make_emphasize(func):
    def empha(**kwargs):
        return f"<em>{func(**kwargs)}</em>"
    return empha
# decoarator to underline an HTML element
def make_underline(func):
    def under(**kwargs):
        return f"<u>{func(**kwargs)}</u>"
    return under

# print(__name__)
@app.route("/")
@make_bold
@make_emphasize
@make_underline
def hello_world():
    return """
            <h1 style='text-align: center'>Hello, World!</h1>
            <p style='text-align: center'>See me mumu</p>
            <img src='https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExdDFmNmhoOG15Y3Q0bGE4dTlwODI0bDljMTdjYWJ3eWZscDN4Nmt2dCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/14MjVpzfpuzqE/giphy.gif' style='align: center' width='300' height='500'>
            """
@app.route("/shy")
def shy():
    return "Shy, shy, shy..."\
        "<p style='text-align: center'>See me mumu</p>"
        
        

# Creating a variable path and converting it to a specified data type
@app.route("/<name>/<int:number>")
def hello_name(name, number):
    return f"Hello, {name+'_404_'}!, you are number {number}"

if __name__ == "__main__":
    # running in debug mode to auto-reload
    app.run(debug=True)
    
    
    
# ## Advanced Python Decorator Functions

# class User:
#     def __init__(self, name):
#         self.name = name
#         self.is_logged_in = False

# def is_authenticated_decorator(function):
#     def wrapper(*args, **kwargs):
#         if args[0].is_logged_in == True:
#             function(args[0])
#     return wrapper

# @is_authenticated_decorator
# def create_blog_post(user):
#     print(f"This is {user.name}'s new blog post.")

# new_user = User("Ander")
# new_user.is_logged_in = True
# create_blog_post(new_user)