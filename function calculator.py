def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print("===== Function Calculator =====")
print("Add")
print("Subtract")
print("Multiply")
print("Divide")

try:

    choice = input("Choose a operation (+, -, * or /): ")

    num1 = float(input("Enter first number: "))

    num2 = float(input("Enter second number: "))

    if choice == "+":
        result = add(num1, num2)

    elif choice == "-":
        result = subtract(num1, num2)

    elif choice == "*":
        result = multiply(num1, num2)

    elif choice == "/":
        result = divide(num1, num2)

    else:
        print("Invalid operation")

except ValueError:
    print("Please enter numbers only")

except ZeroDivisionError:
    print("You cannto divide by zero")