#gallons = float(input("volume in gallons by user "))

def liters(volume):
    result = volume * 3.785
    #print(result)
    return 


def convert():


    while True:

        gallons = float(input("Enter a volume in American gallons (negative value to quit): "))

        if gallons >0:
            #print(f"American gallons is {liters(gallons)}")
            liters(gallons)
            print (liters)

        if gallons < 0:
            print("Program finished.")
            break
    return

convert()