print("Welcome to the Dim dungeon")
age=int(input("What is your age ? "))
name=input("What is your name ? ")

print(f"Your age is {age}")
print(f"Your name is {name}")



if age > 12:
     print ("Hello, Welcome to Dim Dungeon")

if age < 12:
    print("You are a minor , Exiting")


while True:
            print("\n--- MAIN MENU ---")
            print("Available commands: 'hello', 'help', 'lopeta' , 'inventory' , 'rest'")
            
            command = input("Enter command: ").strip().lower()
            
            if command == "lopeta":
                print("Thank you for using the program. Goodbye!")
                break
            elif command == "hello":
                print("Hello there!")
            elif command == "help":
                print("Type 'lopeta' to exit the program.")
            elif command == "inventory":
                 print("Backpack")
            elif command == "rest":
                 print("You took a nap")
            else:
                print("Unknown command. Please try again.")