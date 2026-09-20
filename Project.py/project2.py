print("Welcome to the Dim dungeon")
age=int(input("What is your age ? "))
name=input("What is your name ? ")

print(f"Your age is {age}")
print(f"Your name is {name}")



if age < 12:
    print("You are a minor , Exiting")

            
if age> 12:
    print ("Hello, Welcome to Dim Dungeon")




backpack = []


def add_item():
    pr1 = input("Add to your backpack ")

    backpack.append(pr1)
    print(f"{pr1} has been added to your backpack")
    
def open_backpack():

    print(f"Your backpack contains: {backpack}")

def rest(hour):
      if 0 < hour and hour <= 6:
        print(f"You rested {hour} hours and healed for 10 HP")   

      elif 6 < hour and hour <= 12:
        print(f"You rested {hour} hours and healed for 20 HP")   

      elif 12 < hour and hour <= 18:
            print(f"You rested {hour} hours and healed for 30 HP")

      elif 18 < hour and hour <= 24:
            print(f"You rested {hour} hours and healed for 40 HP")
      else: print("Invalid number, enter a number between 1 and 24")
           

def equipment():
    pass

def map():
    print("Opens map.\n Choose where you want to go.")

while age > 12:

            

            


            print ("\n--- MAIN MENU ---")
            print ("Available commands: 'hello', 'help', 'lopeta' , 'backpack' , 'rest' , 'equipment' , 'map' ")
            
            command = input("Enter command: ").strip().lower()
            
            if command == "lopeta":
                print("Thanks for playing. Until next time!")
                break
            elif command == "hello":
                print("Hello there!")
            elif command == "help":
                print("Type 'lopeta' to exit the program.")
            elif command == "backpack":
                 commandB = input("Choose an action: add_item or open_backpack ")
                 if commandB == "add_item":
                    add_item()
                    open_backpack()
                 elif commandB == "open_backpack":
                    print(backpack)
            elif command == "rest":
                 commandC = int(input("How many hours do you want to rest? "))
                 rest(commandC)
            elif command == "equipment":
                 equipment()
            elif command == "map":
                 map()
            else:
                print("Unknown command. Please try again.")



