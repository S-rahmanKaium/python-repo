#List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

list = ['Apple' ,'Orange' ,'Watermelon', 'Pineapple', 'Blackberry', 'Starawberry'] 
list1 = [] 

for i in list :
    if 'te' in i :
        list1.append(i)
print(list1)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)   #Comperihenson VERSION
