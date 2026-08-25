import random

Three_digit_code =[str(random.randint(0,9)) for _ in range (3)]
X3=Three_digit_code

Four_digits_code =[str(random.randint(1, 6)) for _ in range(4)]
X4=Four_digits_code

print("3-digit code: " + "".join(X3))
print("4-digit code: " + "".join(X4))