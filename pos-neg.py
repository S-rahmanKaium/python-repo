
def Tracker () :
    a = input("Enter Your Number Here : ")

    try :
         if 'j' in a :
              a = complex(a) 
              print("This is a Complex Value")
        
         else :
              a = int(a)
              if a < 0 :
                   print("This is a Negative value")
              elif a > 0 :
                  print("his is a Positive Value")
              else :
                 print("This is nothing , but ZERO")
    except ValueError:
         print('Shit ! You Typed Wrong Date_Type >>> Fix IT!')
 
Tracker()
Tracker()
Tracker()
Tracker()
Tracker()
#----------- ----------------------------------------------------------
# <------ Fucked up , Finally i did it yo ho ho ho ----->
# Try and Except belongs to Except Error handling this is not far way from TOPIC >>>> Conditional Statement 
#---------------------------------------------------------------------