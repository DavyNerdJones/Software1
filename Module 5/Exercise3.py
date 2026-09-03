number = input("Enter a number (or press Enter to quit): ")


numbers = []

while number != "":
    numbers.append(float(number))
    number = input("Enter a number (or press Enter to quit): ")


numbers.sort(reverse=True)
for n in numbers [:1]:
    print(f"Smallest number: {(numbers[-1])} \nLargest number: {(numbers[0])}")