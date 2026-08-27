print("Hello")

print('"Hello" , \nsaid Dave')

print ('"I\'m Dave"')


print (5)
print (10)


name = input('Enter your name: ')
print("Nice to meet you, " + name + "!")


points = 50  # points is now 50
print(points)  # prints: 50

points = 120  # now points is 120
print(points)  # prints: 120

#Error to the bottom lines
#player_name = Geeeeorge
#print ("+player_name")

import random
rounds = 0
total_rolls = 0

while rounds < 100000:
    dice1 = dice2 = rolls = 0
    while (dice1 != 6 or dice2 != 6):
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
	rolls = rolls + 1
    #print(f"Rolled {rolls:d} times.")
    rounds = rounds + 1
    total_rolls = total_rolls + rolls

average_rolls = total_rolls/rounds
print(f"Average rolls required: {average_rolls:6.2f}")