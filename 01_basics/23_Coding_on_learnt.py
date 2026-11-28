import math
#Problem Statement --> How many paint can is required to paint the one wall.Given height and width by the customer
#1 can of paint covers --> 7 square meter  
height = int(input("Enter the height of one wall :  "))
width = int(input("Enter the width of one wall : "))

area = height * width
paint_can_consumed = math.ceil((area/7))  

print(f"The paint can required to complete {area} sq meter is :   {paint_can_consumed}")