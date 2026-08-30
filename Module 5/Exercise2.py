
while True:
    inch = float(input("Enter length in inches (negative value to quit): "))

    if inch >= 0:
        print (f"{inch:0.1f} inches is {(inch * 2.54):0.2f} centimeters" )
    if inch <0:
        print ("Program ended.")
        break

