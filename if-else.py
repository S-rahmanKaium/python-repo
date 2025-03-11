a = float(input("Enter Your Value For 'a': "))
b = float(input("Enter Your Value For 'b': "))
c = float(input("Enter Your Value For 'c': "))

if a == b == c:
    print("Crap, Same Values")
elif a > b and a > c:
    print("A is The Greater One")
elif b > a and b > c:
    print("B is The Greater One")
elif c > a and c > b:
    print("C is The Mastermind")
elif a == b > c:
    print("A ---- The Greater One")
elif b == c > a:
    print("B for Boss the GREATER")
elif c > a == b:
    print("Joker Play, hahaha")
else:
    print("Unexpected Case, Check Input!")
