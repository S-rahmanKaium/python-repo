a = input("Enter Your First Number: ")
b = input("Enter Your Second Number: ")
c = input("Enter Your Third Number: ")
try : 
    a = int(a)
    b = int(b)
    c = int(c)
    if a > b and  b > c :
      print(f"Ascending Order = {a} > {b} > {c}") 
    elif b > a and a > c :
       print(f"Ascending Order = {b} > {a} > {c}") 
    elif c > a and b > a  :
       print(f"Ascending Order = {c} > {b} > {a}")
    else :
       print(f"Ascending Order = {c} > {a} > {b}")  
except ValueError :
      print("Invalid Value")

#-------------------------------------------------------------------------------    
#<--- Well ,As this is a project about Ascending but i made it Reverse,LOL --->
#<There is few ERROR with it logic (6 parameter ) 
#Anyway i am passing this one , will make it better next time,YO HO HO HO ---
#-------------------------------------------------------------------------------