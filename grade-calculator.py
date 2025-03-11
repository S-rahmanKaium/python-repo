a = int(input("Enter Your Marks Here: "))

def marks () :
    if 90 <= a <= 100 :
     print("You Got 'A' " )
    elif 80 <= a <= 89 :
     print("You Got 'B'")
    elif 70 <= a <= 79 :
     print("You Got 'C'")
    elif 60 <= a <= 69 :
        print("You Got 'D'")
    elif 0 <= a <= 59 :
        print("Opps, You are FAIL DUH")
    else :
        print("Invalid Marks")

marks()

#--------------------------------------------------------------------------------
# <------ Seems Everything is going Smooth ---------->
# Will make it more complex with loops and fucntion later >>> So Hard BOILED
#---------------------------------------------------------------------------------