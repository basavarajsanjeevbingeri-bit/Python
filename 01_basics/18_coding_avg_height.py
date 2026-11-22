heights = input("Enter the heights of a student separated by comma\n")

print(heights)


height_splitted = heights.split(',')

print(height_splitted)

count = len(height_splitted)
print(count)

sum =0
for i in range(count):
        sum = sum + int(height_splitted[i])
        print("Current sum is  ",sum )

avg = sum/count #round(sum/count)
print("Average is : " , avg)
