def prime_number(number):
    prime_key = True
    if number <= 1: #Enhanced approach <= 1 
        prime_key = False
    elif number == 2:
        prime_key = True 
    else: 
        for i in range(2,int(number ** 0.5)+1):
            if number % i == 0:
                prime_key = False
                break
    print(f"The number {number} is : {prime_key}")

n = int(input("Enter the range upto define Prime number "))
prime_number(n)