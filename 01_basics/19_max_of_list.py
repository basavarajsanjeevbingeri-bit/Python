#program to find the max of number
numbers = input("Enter the numbers :  \n")
print(numbers)

number_list = numbers.split()
num = []

print(number_list)
count = len(number_list)

for i in range(count):
    num.append(int(number_list[i]))

max = num[0]

for i in range(count):
    if max<num[i]:
        max = num[i]
        print("Current Max:  ",max)
    
print("Final max is :   ",max)