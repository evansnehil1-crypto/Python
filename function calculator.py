def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print("===== Function Calculator =====")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

try:
    choice = input("Choose an operation (1, 2, 3, 4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        result = add(num1, num2)
    elif choice == "2":
        result = subtract(num1, num2)
    elif choice == "3":
        result = multiply(num1, num2)
    elif choice == "4":
        result = divide(num1, num2)
    else:
        print("Invalid operation")
        result = None

    if result is not None:
        print("Result:", result)

except ValueError:
    print("Please enter numbers only")

except ZeroDivisionError:
    print("Cannot divide by zero")
