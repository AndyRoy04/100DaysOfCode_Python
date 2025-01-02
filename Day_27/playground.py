# # Dealing with Advanced Keywords Arguments
# def foo(a, b=4, c=6):
#     print(a, b, c)

# foo(20, c=6)


# def add(*args):
#     # Sum the loop n1 and n2
#     result = 0
#     for n in args:
#         result += n
#     return result
        
# print(add(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40))

def calculate(n, **kwargs):
    print(kwargs['name'])
    print(int(kwargs['age']*1.5))
    
calculate(3, name='John Doe', age=30, city='New York')