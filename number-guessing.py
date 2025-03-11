a = 7 
b = int(input("Enter Your Guess Here : "))

if a == b :
    print("Yo ho ho ho ,You win PAL !")
elif 4 <= b <= 6 or 8 <= b <= 10 : 
    print("Ufffsss ,TOOOOO Close")
elif b > 15 :
    print("Too High , you need some chill in life DUH")
elif b < 3 : 
    print("Too LOw , you need some bit in life DuH")
else : 
    print("Nice Try , Better Luck Next time")