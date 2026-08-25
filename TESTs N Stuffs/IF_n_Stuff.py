money = float(input("Enter amount of money "))

cost_of_coffee = 4


if money >= cost_of_coffee:
    print("you are not broke")
    print("buy coffee")
if money <= cost_of_coffee:
    print("you are broke")

takeout = input("Coffee to go?")

if takeout == "yes" :
    print ("coffee to goooooo")

if takeout == "no" :
    print ("coffee at kahvilla")