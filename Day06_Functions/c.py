def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

operation = input("Enter operation (add, subtract, multiply, divide): ")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if operation == "add":
    print(add(a, b))

elif operation == "subtract":
    print(subtract(a, b))

elif operation == "multiply":
    print(multiply(a, b))

elif operation == "divide":
    print(divide(a, b))

else:
    print("Invalid operation")