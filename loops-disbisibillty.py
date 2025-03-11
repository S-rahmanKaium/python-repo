a = int (input('Enter your Value here : '))
for i in range(1 , a ) :
    if i % 3 == 0 and i % 5 == 0 and i % 30 == 0:
        print(i , end=" ")
       
