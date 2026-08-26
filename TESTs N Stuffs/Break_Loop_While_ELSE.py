command = input("What do you want to do? ")
while command != "stop":
    if command == "help":
        break
    print(f"You want to { command}")
    command = input("what do you want to do  ")