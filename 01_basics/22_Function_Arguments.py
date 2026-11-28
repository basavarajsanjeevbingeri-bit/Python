# def greet(name,dept):
#     print(f"I am {name}")
#     print(f"and I am from {dept} department")

# #Positional arguments means first name means name and second dept only 
# greet("Basavaraj","CS")


# #Keyword Arguments 
# greet(dept = "CS" , name = "Basavaraj")


# #default arguments should defined while creating the function
# def greet_default_demo(name , dept = 'ME'):  # IF you don't mention anything by default it will take ME as ur dept 
#     print(f"Hi I am {name}")
#     print(f"I am in this deparetment: {dept}")


# greet_default_demo("Basva")   


# #Arbitrary positional arguments
# def add(*numbers):
#     c = 0
#     for i in numbers:
#         c = c + i
#     print(c)
    
# add(5,7,9)
# add(10,20,30,40,50) 

#keyword arguments kwargs 
# def info_per(*args,**kwargs):
#     c = 0
#     for i in args:
#         c = c + i   
#     print(c)
    
#     print(kwargs)

# info_per(1,2,name = "Basavaraj",age = "30",dept = "CS")

#Assignment on Keyword arguments 
#multiply(2,3,-6,8)

# def multiply(*numbers_mul):
#     c = 1
#     for i in numbers_mul:
#         c = c*i
#     print(c)
    
    
# multiply(2,3,-6,8)
# multiply(2,5,8,9,0,6)