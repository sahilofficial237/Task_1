# Calculator CLI App
#functions for arthimatic operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def calculator():
    print("===== Simple CLI Calculator =====")
    print("Operations: +  -  *  /")
    print("Type 'exit' to quit.\n")

    while True:
        choice = input("Enter operation (+, -, *, /) or 'exit': ").strip()

        if choice.lower() == 'exit':
            print("Exiting calculator. Goodbye!")
            break

        if choice not in ['+', '-', '*', '/']:
            print("Invalid operation. Try again.\n")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.\n")
            continue

        if choice == '+':
            print(f"Result: {add(num1, num2)}\n")
        elif choice == '-':
            print(f"Result: {subtract(num1, num2)}\n")
        elif choice == '*':
            print(f"Result: {multiply(num1, num2)}\n")
        elif choice == '/':
            print(f"Result: {divide(num1, num2)}\n")

if __name__ == "__main__":
    calculator()
