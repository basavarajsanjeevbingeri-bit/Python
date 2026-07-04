num = int(input("Enter a number : "))
temp = num
sum = 0 
digit = 0 

while(num > 0):
    digit = num%10
    sum = sum + digit
    num = num//10
    print("The current value is " + str(sum))


print("The Sum of the digits  is " + str(sum) + " for a number " + str(temp))