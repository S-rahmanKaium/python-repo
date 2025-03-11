a = int(input("Enter Your First value: "))
b = input("Enter Your Operation sign:")
c = int(input("Enter YOur Second Value: "))

if b == '+' :
    print(f"Result = {a + c} ") 
elif b == '-' :
    print(f"Result = {a - c}")
elif b == '*' :
    print(f"Result = {a * c}")
elif b == '/' :
    if c == 0 :
        print("Invalid Value , Try Another")
    else :
        print(f"Result = {a / c}")
    
else :
    print("System is on Developing Phase , Try again Later")