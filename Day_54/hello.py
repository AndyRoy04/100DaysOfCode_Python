# from flask import Flask

# app = Flask(__name__)

# print(__name__)
# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

# if __name__ == "__main__":
#     app.run()


# # # DECORATOR FUNCTIONS
# # def decorator_function(function):
# #     def wrapper_function():
# #         print("Something is happening before the function is called.")
# #         function()
# #     return wrapper_function

# # @decorator_function
# # def say_hello():
# #     print("Hello!")

# # say_hello()


# --------- Python decarator for calculating execution time of 2 functions ------------------ #

import time
current_time = time.time()
print(current_time) # seconds since Jan 1st, 1970 

# Write your code below 👇

def speed_calc_decorator(func):
    def wrapper(**kwargs):
        start_time = time.time()
        result = func(**kwargs)
        end_time = time.time()
        print(f"{func.__name__} run speed: {end_time - start_time}s")
        return result
    return wrapper

@speed_calc_decorator
def fast_function():
  for i in range(1000000):
    i * i
        
@speed_calc_decorator
def slow_function():
  for i in range(10000000):
    i * i
    
fast_function()
slow_function()