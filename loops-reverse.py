# a = int(input("Enter your nmber here : "))
# for i in range(a , 0 , -1) :
#     print(i)
    

n = int(input("Enter a number: "))

while n > 0:
    print(n , end="' : '")
    n -= 1  # Decrease n by 1 in each iteration
    