import random

print("Welcome to password generator tool")

letters_list = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G',
    'H', 'I', 'J', 'K', 'L', 'M', 'N',
    'O', 'P', 'Q', 'R', 'S', 'T', 'U',
    'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u',
    'v', 'w', 'x', 'y', 'z'
]

numbers_list =[
    '0', '1', '2', '3', '4',
    '5', '6', '7', '8', '9'
]

symbol_list = [ '!', '@', '#', '$', '%', '^',
    '&', '*', '(', ')', '-', '_',
    '=', '+', '[', ']', '{', '}',
    '|', '\\', ';', ':', "'", '"',
    ',', '<', '.', '>', '/', '?',
    '`', '~']

letters = int(input("Enter the number of letters should involve in ur password?\n"))

digits = int(input("Enter the number of digits should involve?\n"))

symbols = int(input("Enter the number of symbols should involve?\n"))

password_list = []
for i in range(1,letters+1):
    password_list = password_list + [random.choice(letters_list)]
    
print(password_list)


for i in range(1,digits+1):
    password_list = password_list + [random.choice(numbers_list)]
    
print(password_list)


for i in range(1,symbols+1):
    password_list = password_list + [random.choice(symbol_list)]
    
print(password_list)


random.shuffle(password_list)

print(password_list)

password = ""

for char in password_list:
    password = password + char

print("Your password is _: " , password)