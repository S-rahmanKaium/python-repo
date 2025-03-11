def Tracker():
    while True:
        a = input("Enter Your Number Here (or type 'exit' to stop): ")

        if a.lower() == 'exit':  # Allow user to quit manually
            print("Goodbye! 🚀")
            break

        try:
            if 'j' in a:
                a = complex(a)
                print("This is a Complex Value")

            else:
                a = int(a)
                if a < 0:
                    print("This is a Negative value")
                elif a > 0:
                    print("This is a Positive Value")
                else:
                    print("This is nothing but ZERO")

        except ValueError:
            print("Shit! You Typed Wrong Data_Type >>> Fix IT!")
            break  # Exit loop on invalid input

# Call the function
Tracker()
