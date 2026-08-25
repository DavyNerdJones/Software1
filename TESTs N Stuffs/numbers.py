import random

first = -9
second = 12_456_123_180
third = 4.973
fourth = -4 + 2j

print(first)
print(second)
print(third)
print(fourth)
print(fourth.real)
print(fourth.imag)
print()
print(third + 1)


digits =[str(random.randint(1, 6)) for _ in range(4)]

print("".join(digits))

"""
X = "".join(digits)
print(X)
"""