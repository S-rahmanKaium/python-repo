thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dict = thisdict.copy()   #Copy Dict .copy() methods 
for x , y in thisdict.items() :
    print(x, y)

print(dict)