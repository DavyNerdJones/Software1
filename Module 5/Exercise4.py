import random

computer_guess = random.randint(1,10)

print ("Try guess the number")


while True:
    user_guess = int(input("Guess a number (1-10): "))

    if user_guess > computer_guess:
        print ("Too high")
    elif user_guess < computer_guess:
        print ("Too low")
    else:
        print ("Correct")
        break
