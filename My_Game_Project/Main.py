#TODO TIDY UP the notes, move to functions anything that can be moved. Change the names
#TODO make it more clear and distinct from each other. Add more rooms, make a bigger map layout.

from Actions import Item
from Actions import Player
from Actions import Room
from Actions import rest , add_item 

print("Welcome to the Dim dungeon")
age=int(input("What is your age ? "))
name=input("What is your name ? ")

print(f"Your age is {age}")
print(f"Your name is {name}")


#backpack = [] 

if age < 12:
    print("You are a minor , Exiting")

            
if age> 12:
    print ("Hello, Welcome to Dim Dungeon")

starting_item = Item("Potion" , 1)
item1 = Item("Sword_Of_Infinity" , 17)
item2 = Item("Hammer_Of_Justice" , 28)
item3 = Item("Bow_Of_Speed" , 11)
item4 = Item("Mace_Of_Wrath" , 27)

starting_room = Room("Waiting_Room" , "Here you just WAIT")

starting_room.add_room_item(starting_item.name)

room1 = Room("Dark_Cell" , "Dangerous")
room1.add_room_item(item1)

room2 = Room("Ominus_Corridor" , "Really Dark")
room2.add_room_item(item2)

room3 = Room("Sharp_Dungeon" , "Care for the knives")
room3.add_room_item(item3)

room4 = Room("Prison_Cell" , "Broken iron bars")

player1 = Player({name} , {age}, starting_room )
player1.collect_item(starting_item.name)
#found_item(starting_item)
#print(player1.location)

#print(player1.backpack)
#print(player1.name , player1.age , player1.location)




while age > 12:


            print ("\n--- MAIN MENU ---")
            print ("Available commands: 'hello', 'help', 'lopeta' , 'backpack' , 'rest' , 'equipment' , 'move , 'map' ")
            
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
                 elif commandB == "open_backpack":
                    print(player1.backpack)
            elif command == "rest":
                 commandC = int(input("How many hours do you want to rest? "))
                 rest(commandC)
            elif command == "equipment":
                 equipment()
            elif command == "map":
                 map()
            elif command == "move":
                 coommandD = input("Choose where you want to go : up , down, left , right ")
                 player1.move(coommandD) 
                 print (f"You moved to {player1.location}")
                 print(player1.backpack)
            else:
                print("Unknown command. Please try again.")



