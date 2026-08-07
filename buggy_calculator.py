# A calculator script with intentional bugs for testing

def add(a, b)
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    result = a * b
    retrun result   # typo here

def divide(a, b):
    return a / 0   # will always crash with ZeroDivisionError

class Calculator:
    def __init__(self)
        self.history = []

    def calculate(self, op, a, b):
        if op == "add"
            return add(a, b)
        elif op = "subtract":   # assignment instead of comparison
            return subtract(a, b)
        else:
            return None

print("Starting calculator...")
calc = Calculator()
print(calc.calculate("add", 5, 3))
print(divide(10, 2))
undefined_variable_used_here
