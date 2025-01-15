import art
print(art.logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def display_operations():
    for symbol in operations:
        print(symbol)


should_accumulate = True
result = 0
num1 = float(input("What is the first number?: "))
tasks = []
index = 0
while should_accumulate:

    is_first_index = index == 0
    num2 = float(input("What is the next number?: "))
    display_operations()
    operation_symbol = input("Pick an operation: ")
    if operation_symbol not in operations:
        print("unknown operation!")
        continue
    if index == 0:
        result = operations[operation_symbol](num1, num2)
    else:
        result = operations[operation_symbol](result, num2)

    print(f"Result is :{result}")
    is_continue = input("Continue ? Y/N : ").lower()
    if is_continue == "n":
        print("Goodbye~")
        should_accumulate = False

    index += 1