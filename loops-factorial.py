def factorial () :
    a = int(input('Enter Your Value : ')) 
    Factorial  = 1 
    for i in range (1 , a+1) :
        Factorial*= i 
    print(f'Factorial Result for {a} is {Factorial}')
factorial()