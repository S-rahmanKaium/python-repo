set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
set6 = {1,4,3}
# set5 = set1.union(set2,set3,set4) 
set1.update(set2,set3)
  
# set = set2.intersection(set6) 
set = set2 & set6   #Intersection could be written like this 
set0 = set6.difference(set2)

set5 = set1 | set2 | set3 | set4  #This is also use as union !
print(set5)
print(set1)
print(set) 
print(set0)