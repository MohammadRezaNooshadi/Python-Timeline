"""
Challenge: Iterative Number Analyzer
Write a Python script that takes a single numerical input from the user and performs basic evaluation:
1. Prompt the user to enter a number.
2. Check whether the number is positive, negative, or zero.
3. If the number is non-zero, determine whether it is even or odd.
"""
while True:
    try:
        num = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

if num != 0:
    if num % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")