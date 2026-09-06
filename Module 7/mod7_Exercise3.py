#gallons = float(input("volume in gallons by user "))

def gallons_to_liters(volume):
    result = volume * 3.785
    #print(result)
    return result


def convert():


    while True:

        gallons = float(input("Enter a volume in American gallons (negative value to quit): "))

        if gallons >0:
            fdewufge = gallons_to_liters(gallons)
            print(f"{gallons} American gallons is {fdewufge:.2f} liters.")


        if gallons < 0:
            print("Program finished.")
            break
    return

convert()

#Note to self, moodle is FANTASTIC