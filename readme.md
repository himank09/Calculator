# Python Calculator

A simple command-line calculator built in Python.

## Features
- Addition, subtraction, multiplication, and division
- Input validation — handles letters and symbols gracefully
- Division by zero protection
- Loops until you choose to quit

## How to run
```bash
python calculator.py
```

## How to run tests
```bash
python -m unittest test_calculator.py -v
```

## Project structure
```
calculator/
├── calculator.py       # core logic and main program
├── test_calculator.py  # unit tests
└── README.md           # this file
```

## Example
```
Simple Python Calculator
------------------------
Choose an operation:
  1. Add
  2. Subtract
  3. Multiply
  4. Divide
  5. Quit

Enter choice (1-5): 1
Enter first number: 10
Enter second number: 5

  Result: 10.0 Add 5.0 = 15.0
```

