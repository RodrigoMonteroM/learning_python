import art


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}


def calculator():
    print(art.logo)
    stop_calculator = True
    num1 = float(input("Enter the first number: "))
    while stop_calculator:

        for symbol in operations:
            print(symbol)

        operator_symbol = input('What operation do you want?: ')
        function_operation = operations[operator_symbol]
        num2 = float(input('Enter the second number: '))
        result = function_operation(num1, num2)

        print(f"{num1} {operator_symbol} {num2} = {result}")

        continue_calculation = input("Type 'Y' if you wanna keep calculating, 'R' to reset,  or type 'N' to exit: ")

        if continue_calculation == 'y':
            num1 = result
        elif continue_calculation == 'r':
            calculator()
        elif continue_calculation == 'n':
            stop_calculator = False
        else:
            print(f'Error, {continue_calculation} is not recognized')


calculator()
