# name = 'Bob'


# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("first")
#         test = func(*args, **kwargs)
#         print("last")
#         return test
#     return wrapper

# @my_decorator
# def idk(name): 
#     print(f"your name is: {name}")



# def repeat(times):
#     def actual_repeat(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(times):
#                 func(*args, **kwargs)
#         return wrapper
#     return actual_repeat


# @repeat(3)
# def greet():
#     print("hi random person")


# greet()

def log_calls(enable):
    def actual_log_calls(func): 
        def wrapper(*args, **kwargs):
            if enable:
                print(f"function {func.__name__} called with argurments: {args}, {kwargs}")
                result = func(*args, **kwargs)
                print(f"funcion: {func.__name__} finished")
                return result
            else:
                return func(*args, **kwargs)
        return wrapper
    return actual_log_calls



@log_calls(enable=True)
def greet(name: str) -> str:
    print(f"hello {name}")
    return name

name = 'alice'

greet(name)