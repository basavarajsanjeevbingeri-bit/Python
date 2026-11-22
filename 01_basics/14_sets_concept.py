set1 = {10,56,89,90,'Basavaraj',True,10,1}
set2 = {} #you cannot create empty set like this why because it treats s a dictionary 
set3 = set() 
# print(type(set1))
# print(type(set2))
# print(type(set3))
set1.add(99)
print(set1)
print(len(set1))

set1.clear()
print(set1)