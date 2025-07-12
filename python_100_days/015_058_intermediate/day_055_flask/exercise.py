# TODO: Create the logging_decorator() function 👇
def logging_decorator(function):
    def wraped(*args):
        result = function(*args)
        print(f"You called {function.__name__}{args}")
        print(f"It returned: {result}")
        return result
    return wraped


# TODO: Use the decorator 👇
@logging_decorator
def a_function(*args):
    return sum(args)
    
a_function(1,2,3)