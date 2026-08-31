"""
User Input and Output
Learn how to take input from users and display output.
"""

# Basic input - always returns a string
print("=== BASIC INPUT ===")
user_name = input("What is your name? ")
print(f"Hello, {user_name}!")

# Taking numeric input
print("\n=== NUMERIC INPUT ===")
age_str = input("How old are you? ")
age = int(age_str)  # Convert string to integer
print(f"You are {age} years old")
print(f"Next year you will be {age + 1} years old")

# Taking decimal input
print("\n=== FLOAT INPUT ===")
height_str = input("What is your height in meters? ")
height = float(height_str)  # Convert string to float
print(f"Your height: {height}m")

# Multiple inputs in one line
print("\n=== MULTIPLE INPUTS ===")
inputs = input("Enter two numbers separated by space: ").split()
num1 = int(inputs[0])
num2 = int(inputs[1])
print(f"Sum: {num1 + num2}")
print(f"Product: {num1 * num2}")

# Formatted output
print("\n=== FORMATTED OUTPUT ===")
price = 19.99
quantity = 5
total = price * quantity
print(f"Price: ${price:.2f}")
print(f"Quantity: {quantity}")
print(f"Total: ${total:.2f}")

# String formatting methods
print("\n=== STRING FORMATTING ===")
person = "Alice"
score = 95.5

# f-string (modern way)
print(f"{person} scored {score}%")

# format() method
print("Student: {}, Score: {:.1f}%".format(person, score))

# % operator (older way)
print("Student: %s, Score: %.1f%%" % (person, score))

# Escape sequences
print("\n=== ESCAPE SEQUENCES ===")
print("Line 1\nLine 2")  # \n = newline
print("Tab\tSeparated\tValues")  # \t = tab
print("Quote: \"Hello\"")  # \" = double quote
print("Backslash: \\")  # \\ = backslash
