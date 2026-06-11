# without decorator
def greeting():
    return "welcome to python"

def uppercase_decorator(fn):
    def wrapper(text):
        func = fn(text)
        action = func.upper()
        return action
    return wrapper

@uppercase_decorator
def say_with_uppercase(text):
    return text

print("say : ", say_with_uppercase("Aswaja"))

def split_string_decorator(fn):
    def wrapper(text):
        func = fn(text)
        action = func.split()
        return action
    return wrapper


@split_string_decorator
@uppercase_decorator
def say_good_bye_to(text):
    return "Good bye to :" + text

print(say_good_bye_to("Fikri"))

numbers = [1,2,3,4,5]
def square(x):
    return x ** 2

number_square = map(lambda x:x ** 2, numbers)

print("number square" , list(number_square))
