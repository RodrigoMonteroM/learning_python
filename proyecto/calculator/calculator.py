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


operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    num1 = float(input("What's the first number?: "))
    for symbol in operation:
        print(symbol)
    stop_calculator = True
    while stop_calculator:

        operation_symbol = input('Pick an operation:  ')
        calculation_function = operation[operation_symbol]
        num2 = float(input("What's the next number?: "))

        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        continue_calculating = input("type 'Y' if you want to keep calculating or to restart type 'r', otherwise type "
                                     "'N'")

        if continue_calculating == 'y':
            num1 = answer
        elif continue_calculating == 'r':
            calculator()
        else:
            stop_calculator = False


calculator()
