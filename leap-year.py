a = int(input("Enter Your Year: "))

if a % 4 == 0 and a % 100 != 0 or a % 400 == 0 :
    print("This is a Leap-Year")
else :
    print("This is not a Leap Year")
