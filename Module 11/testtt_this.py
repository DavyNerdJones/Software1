names = ["m" , "n" , "j" , "f" ]

print(names)
x = names.index("m")

print (x)

names.append("L")
names.remove("j")
print(names)

print(names[-1])


#for x in names:
    #print(names)






"""


import random
dice1 = dice2 = rolls = 0
while (dice1 != 6 or dice2 != 6):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    rolls = rolls + 1

print(rolls)
print(f"Rolled {rolls:d} times.")

"""