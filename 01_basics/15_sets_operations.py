set1 = {'Rama','Lakshamana','Sita'}
set2 = {'Sita','Hanumanta','Jambavanta','Rama','Lakshamana'}
set3 = {'Krishna','Karna','Lakshamana','Hanumanta'}

#Union concept 
# print(set1.union(set2))
# print(set1 | set2)
# print(set1.union(('krishnadevaraya','Immadi Pulakeshi')))
#print(set1 | ('Tulasi','Tulajabhavani')) #It will give error 
# set1.update(set2)
# print("Final version of set1 ")
# print(set1)

#Intersection Concept 
# set3 = set1.intersection(set2)
# print(set3)
# print(set1 & set2)

#difference concept 
# print(set1.difference(set2))
# print(set1.difference(('Lakshamana','Urvashi')))
# print(set1.difference(set2,set3))
# set1.difference_update(set2)
# print(set1)

#symmetric difference concept 
# print(set1.symmetric_difference(set2))
# #print(set1.symmetric_difference(set2,set3)) # not allowed because it takes only one argument 
# print(set1 ^ set2)
# set2.symmetric_difference_update(set3)
# print(set2)

#disjoint concept 
#print(set1.isdisjoint(set2))

# #subset concept 
# print(set1.issubset(set2))
# print(set1 <= set2)

#superset concept 
# print(set2.issuperset(set1))
# print(set2>=set1)

#clear concept 
# set2.clear() clear the set content not the set 
# print(set2)

#del concept
del set2  # delete the set itself 
print(set2) #NameError: name 'set2' is not defined