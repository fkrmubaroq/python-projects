# function  as a parameter
def high_order_function(fn, list):
    summation = fn(list)
    return summation

result = high_order_function(sum, [1,2,3,4,5])
print(result)

# function as a return value
square = lambda num:num ** 2
cube = lambda num:num ** 3
absolute = lambda num: num if num >= 0 else -num

def high_order_func(type):
    if type == "square":
        return square
    elif type == "cube":
        return cube
    elif type == "absolute":
        return absolute
    

result = high_order_func("square")
print("Square :",result(3))
result = high_order_func("cube")
print("Cube :",result(3))
result = high_order_func("absolute")
print("Absolute :",result(-3))

# closure function
def add_ten():
    ten = 10
    def add(num):
        return num + ten
    
    return add

closure_result = add_ten()
print("closure result : ", closure_result(3))

# creating decorator
