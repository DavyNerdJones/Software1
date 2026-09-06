import random

def roll_dice():
    return random.randint(1, 6)

def high_roll():
    result = 0
    while result != 6:
        result = roll_dice()
        print(result)

high_roll()


#Note to self, couldn't this be done in less ?