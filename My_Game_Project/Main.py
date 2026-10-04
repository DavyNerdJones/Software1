#TODO Make the save file a list so it can add more player saves and load from there.
#TODO Add more rooms, make a bigger map layout.
#TODO Add healthpoint, dmg to weapons.

from Actions import Item
from Actions import Player
from Actions import Room
from Actions import rest , add_item 

import json
import os

SAVE_FILE = "savegame.json"

def save_game(player):
    save_data = {
        "name": player.name,
        "age": player.age,
        "location": player.location,
        "backpack": player.backpack
    }

    with open(SAVE_FILE, "w") as file:
        json.dump(save_data, file)

    print("Game saved successfully!")


def load_game():
    if not os.path.exists(SAVE_FILE):
        print("No saved game found.")
        return None

    with open(SAVE_FILE, "r") as file:
        save_data = json.load(file)

    return save_data

item0 = Item("Potion" , 1)
item1 = Item("Sword_Of_Infinity" , 17)
item2 = Item("Hammer_Of_Justice" , 28)
item3 = Item("Bow_Of_Speed" , 11)
item4 = Item("Mace_Of_Wrath" , 27)

starting_room = Room("Waiting_Room" , "Here you just WAIT")
starting_room.add_room_item(item0)

room1 = Room("Dark_Cell" , "Dangerous")
room1.add_room_item(item1)

room2 = Room("Ominus_Corridor" , "Really Dark")
room2.add_room_item(item2)

room3 = Room("Sharp_Dungeon" , "Care for the knives")
room3.add_room_item(item3)

room4 = Room("Prison_Cell" , "Broken iron bars")
room4.add_room_item(item4)

list_of_rooms = [room1 , room2, room3, room4]

with open("intro.txt", "r") as file:
    intro = file.read()
    print(intro)

with open("instructions.txt", "r") as file:
    instructions = file.read()
    print(instructions)

print("Welcome to the Dim dungeon")
#age=int(input("What is your age ? "))  BEFORE TRYING TO IMPLEMENT LOAD/ SAVE FILE
#name=input("What is your name ? ") BEFORE TRYING TO IMPLEMENT LOAD/SAVE FILE

if os.path.exists(SAVE_FILE):
    choice = input("A saved game was found. Load it? (yes/no): ").strip().lower()

    if choice == "yes":
        name = input("Give username ")
        with open("savegame.json", "r") as file:
           data = json.load(file)
           data['name'] 
        if  data["name"] == name:
            save_data = load_game()
            age = save_data["age"]

            print(f"Welcome back, {name}!")
        else:
            age = int(input("What is your age? "))
            name = input("What is your name? ")
    else:
        age = int(input("What is your age? "))
        name = input("What is your name? ")
else:
    age = int(input("What is your age? "))
    name = input("What is your name? ")




#print(f"Your age is {age}")
#print(f"Your name is {name}")

if age < 12:
    print("You are a minor , Exiting")
    exit()

print (f"Hello {name}, Welcome to Dim Dungeon")

player = Player(name , age, starting_room.name )
player.locations = list_of_rooms


#print(room1.__dict__.keys())

player.collect_item(item0.name)
#found_item(starting_item)
#print(player1.location)

#print(player1.backpack)
#print(player1.name , player1.age , player1.location)



def main_menu(player):
    while True:


            print ("\n--- MAIN MENU ---")
            print ("Available commands: 'hello', 'help', 'lopeta' , 'backpack' , 'rest' , 'equipment' , 'move , 'new_game' , 'save_game' , 'load_game' ")
            
            command = input("Enter command: ").strip().lower()
            
            if command == "lopeta":
                print("Thanks for playing. Until next time!")
                break
            elif command == "save_game":
                save_game(player)

            elif command == "load_game":
                save_data = load_game()

                if save_data is not None:
                    player.name = save_data["name"]
                    player.age = save_data["age"]
                    player.location = save_data["location"]
                    player.backpack = save_data["backpack"]

                    print(f"Welcome back, {player.name}!")
                    print(f"You are currently in: {player.location}")
                    print(f"Backpack: {player.backpack}")

            elif command == "hello":
                print("Hello there!")
            elif command == "help":
                print("Type 'lopeta' to exit the program.")
            elif command == "backpack":
                 commandB = input("Choose an action: add_item or open_backpack ")
                 if commandB == "add_item":
                    add_item()
                 elif commandB == "open_backpack":
                    print(player.backpack)
            elif command == "rest":
                 commandC = int(input("How many hours do you want to rest? "))
                 rest(commandC)
            elif command == "equipment":
                 equipment()
            elif command == "map":
                 map()
            elif command == "move":
                 coommandD = input("Choose where you want to go : up , down, left , right ")
                 print(player.backpack)


                 print (f"You moved to {player.location}")
                 player.move(coommandD)


                 
                 print(player.backpack)

            else:
                print("Unknown command. Please try again.")

main_menu(player)



