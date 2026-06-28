"""
Operators in Python
Learn about arithmetic, comparison, logical, and assignment operators.
"""

# Arithmetic Operators
print("=== ARITHMETIC OPERATORS ===")
a = 15
b = 4

print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Floor Division: {a} // {b} = {a // b}")
print(f"Modulus (Remainder): {a} % {b} = {a % b}")
print(f"Exponentiation: {a} ** {b} = {a ** b}")

# Comparison Operators
print("\n=== COMPARISON OPERATORS ===")
x = 10
y = 20

print(f"{x} == {y}: {x == y}")  # Equal
print(f"{x} != {y}: {x != y}")  # Not equal
print(f"{x} > {y}: {x > y}")    # Greater than
print(f"{x} < {y}: {x < y}")    # Less than
print(f"{x} >= {y}: {x >= y}")  # Greater than or equal
print(f"{x} <= {y}: {x <= y}")  # Less than or equal

# Logical Operators
print("\n=== LOGICAL OPERATORS ===")
condition1 = True
condition2 = False

print(f"True AND False: {condition1 and condition2}")
print(f"True OR False: {condition1 or condition2}")
print(f"NOT True: {not condition1}")

# Practical example with logical operators
age = 25
has_license = True
can_drive = age >= 18 and has_license
print(f"\nCan drive (age >= 18 and has license): {can_drive}")

# Assignment Operators
print("\n=== ASSIGNMENT OPERATORS ===")
num = 10
print(f"num = {num}")

num += 5  # num = num + 5
print(f"After += 5: {num}")

num -= 3  # num = num - 3
print(f"After -= 3: {num}")

num *= 2  # num = num * 2
print(f"After *= 2: {num}")

num //= 4  # num = num // 4
print(f"After //= 4: {num}")

# Membership Operators
print("\n=== MEMBERSHIP OPERATORS ===")
fruits = ["apple", "banana", "cherry"]
print(f"'apple' in {fruits}: {'apple' in fruits}")
print(f"'grape' in {fruits}: {'grape' in fruits}")
print(f"'orange' not in {fruits}: {'orange' not in fruits}")

# Identity Operators
print("\n=== IDENTITY OPERATORS ===")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(f"list1 is list2: {list1 is list2}")  # Different objects
print(f"list1 is list3: {list1 is list3}")  # Same object
print(f"list1 == list2: {list1 == list2}")  # Same values
