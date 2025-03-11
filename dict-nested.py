thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964 ,
  'child1' : {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964} ,
  'child2' : {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964} ,
  'child3' : {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964} ,
  'child4' : {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964} ,

}
# for i in thisdict.values() :      ------ No More Today --------
#     print(i)
print(thisdict["child1"]['year'])

#---- More Practice in future (Aj ke liye filhal itnahi) --------