"""
Simple command-line calculator.
Supports addition, subtraction, multiplication, and division.
"""
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b
def power(a, b):
    return a ** b

def square_root(a, b=None):
    if a < 0:
        return "Error: Cannot square root a negative number"
    return a ** 0.5

def modulus(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a % b


def main():
    print("Simple Python Calculator")
    print("------------------------")
    history=[]

    operations = {
        '1': ('Add', add),
        '2': ('Subtract', subtract),
        '3': ('Multiply', multiply),
        '4': ('Divide', divide),
        '5': ('Power', power),
        '6': ('Square Root', square_root),
        '7': ('Modulus', modulus),
    }

    while True:
        print("\nChoose an operation:")
        for key, (name, _) in operations.items():
            print(f"  {key}. {name}")
        print("  8. History")
        print("  9. Quit")
        

        choice = input("\nEnter choice (1-9): ").strip()

        if choice == '9':
            print("Goodbye!")
            break

        if choice == '8':
            if len(history) == 0:
                print("\n  No calculations yet.")
            else:
                print("\n  Calculation History:")
                for i, entry in enumerate(history, 1):
                    print(f"  {i}. {entry}")
            continue

        if choice not in operations:
            print("Invalid choice. Please try again.")
            continue

        try:
            if choice == '6':
                a = float(input("Enter number: "))
                b = None
            else:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
        except ValueError:
            print("Invalid number. Please enter digits only.")
            continue
        
        name, func = operations[choice]
        result = func(a, b)
        print(f"\n  Result: {a} {name} {b} = {result}")
        history.append(f"{a} {name} {b} = {result}")  # ← add this line

if __name__ == "__main__":
    main()