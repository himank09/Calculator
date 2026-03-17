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


def main():
    print("Simple Python Calculator")
    print("------------------------")

    operations = {
        '1': ('Add', add),
        '2': ('Subtract', subtract),
        '3': ('Multiply', multiply),
        '4': ('Divide', divide),
    }

    while True:
        print("\nChoose an operation:")
        for key, (name, _) in operations.items():
            print(f"  {key}. {name}")
        print("  5. Quit")

        choice = input("\nEnter choice (1-5): ").strip()

        if choice == '5':
            print("Goodbye!")
            break

        if choice not in operations:
            print("Invalid choice. Please try again.")
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("Invalid number. Please enter digits only.")
            continue

        name, func = operations[choice]
        result = func(a, b)
        print(f"\n  Result: {a} {name} {b} = {result}")


if __name__ == "__main__":
    main()