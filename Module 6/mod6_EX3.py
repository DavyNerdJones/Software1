import math


num = int(input("Enter an integer: "))
if num <= 1:
    print(num, "is not a prime number.")
else:
    for number in range(2, num):
        if num % number == 0:
            print(num, "is not a prime number.")
            break
    else:
        print(num, "is a prime number.")