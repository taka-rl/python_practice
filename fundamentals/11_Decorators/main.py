# example1
def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    return nested_function


inner_function = outer_function()
inner_function()

'''
Output
I'm outer
I'm inner
'''

# example2
import time


def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        # Do something before
        function()
        # Do something after
    return wrapper_function


@delay_decorator
def say_hello():
    print("Hello")


@delay_decorator
def say_bye():
    print("Bye")


def say_greeting():
    print("How are you?")


say_hello()
say_greeting()

decorated_function = delay_decorator(say_greeting)
decorated_function()

# example3
"""
A decorator in Python is a function that takes another function as an argument, 
adds some functionality (or modifies the behavior), 
and returns a new function without modifying the original function itself. 
It's a powerful tool that allows you to wrap functionality around an existing function in a clean and reusable way.

"""


def speed_calc_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
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
"""
or it's equivalent to writing:
fast_function = speed_calc_decorator(fast_function)
slow_function = speed_calc_decorator(slow_function)
This means that when you call fast_function() or slow_function(), 
you're actually calling the wrapper function inside speed_calc_decorator.
"""

"""
What is func(*args, **kwargs)?
In Python, *args and **kwargs are used to pass a variable number of arguments to a function.
*args: 
This allows you to pass any number of positional arguments to a function. 
These arguments are received as a tuple inside the function.

**kwargs:
This allows you to pass any number of keyword arguments to a function.
These are received as a dictionary inside the function.
"""


def test_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Arguments passed to {func.__name__}: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        return result
    return wrapper


@test_decorator
def example_function(a, b, c=10):
    return a + b + c


example_function(1, 2, c=20)
# the output is as follows:
# Arguments passed to example_function: args=(1, 2), kwargs={'c': 20}
# Then func(*args, **kwargs) translates to example_function(1, 2, c=20).

"""
Summary:
*args is used to accept any number of positional arguments (like a, b).
**kwargs is used to accept any number of keyword arguments (like c=10).
In decorators, func(*args, **kwargs) is a way of forwarding any arguments passed to the decorated function 
to the original function, ensuring the decorator works regardless of the function signature.
"""

# example4


class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in:
            function(args[0])
    return wrapper


@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")


new_user = User("angela")
create_blog_post(new_user)

new_user.is_logged_in = True
create_blog_post(new_user)

