def divide(x, y):
    return x / y

try:
    print(divide(10, 0))
except ZeroDivisionError:
    print("Division by zero")
