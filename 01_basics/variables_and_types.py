"""
Variables and Data Types in Python
Learn about different data types and variable assignment.
"""

# String - text data
name = "John"
city = "New York"
print(f"Name: {name}, City: {city}")

# Integer - whole numbers
age = 25
year = 2024
print(f"Age: {age}, Year: {year}")

# Float - decimal numbers
height = 5.9
temperature = 98.6
print(f"Height: {height}m, Temperature: {temperature}°F")

# Boolean - True or False
is_student = True
is_working = False
print(f"Student: {is_student}, Working: {is_working}")

# Check data type using type()
print(f"\nData Types:")
print(f"Type of name: {type(name)}")
print(f"Type of age: {type(age)}")
print(f"Type of height: {type(height)}")
print(f"Type of is_student: {type(is_student)}")

# Type conversion
string_number = "42"
converted_number = int(string_number)
print(f"\nConverted '{string_number}' to integer: {converted_number}")

float_to_string = str(3.14)
print(f"Converted 3.14 to string: '{float_to_string}'")

# Multiple assignment
a, b, c = 10, 20, 30
print(f"\nMultiple assignment: a={a}, b={b}, c={c}")

# Swapping values
x, y = 5, 10
x, y = y, x
print(f"After swap: x={x}, y={y}")
