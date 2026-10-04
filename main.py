#calculator
def add_numbers(a: float, b: float) -> float:
    return a + b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a / b
