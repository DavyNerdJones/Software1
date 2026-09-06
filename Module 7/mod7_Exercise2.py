import random

sides = int(input("Enter number of sides: "))

def roll_dice(sides):
    return random.randint(1, sides)

def high_roll(sides):
    result = 0
    while result != sides:
        result = roll_dice(sides)
        print(result)

high_roll(sides)


# Got an error "missing 1 required positional argument:" if i didn't have "sides" after the functions.
#why ?