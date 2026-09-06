import random

K = int(input("How many random points to generate"))

n = 0
count = 0
while count < K:
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    if x*x + y*y <1:
        n += 1
    count +=1

print (f"Approximation of pi: {4*n/K}")