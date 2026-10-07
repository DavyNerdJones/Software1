from Actions import Item
from Actions import Player
from Actions import Room
from Actions import rest #add_item
from Actions import get_total_weight
from Actions import show_current_room
from Actions import save_game , load_game
from Actions import check_game_end
import json
import os

SAVE_FILE = "savegame.json"


# ITEMS

item0 = Item("Shovel", 7)
item1 = Item("DumpsterFire", 17)
item2 = Item("WetCardboard", 28)
item3 = Item("HalfEatenBagel", 11)
item4 = Item("MoldyCrouton", 27)
item5 = Item("SoggySock" , 6)
item6 = Item("BrokenGlasses" , 2)



# Store all items in a dictionary so they can
# be found using their name

items = {
    item0.name: item0,
    item1.name: item1,
    item2.name: item2,
    item3.name: item3,
    item4.name: item4,
    item5.name: item5,
    item6.name: item6
}

# ROOMS


starting_room = Room(
    "Waiting_Room",
    "Here you just WAIT"
)

starting_room.add_room_item(item0)


room1 = Room(
    "Dark_Cell",
    "Dangerous"
)

room1.add_room_item(item1)


room2 = Room(
    "Ominus_Corridor",
    "Really Dark"
)

room2.add_room_item(item2)


room3 = Room(
    "Sharp_Dungeon",
    "Care for the knives"
)

room3.add_room_item(item3)


room4 = Room(
    "Prison_Cell",
    "Broken iron bars"
)

room4.add_room_item(item4)


room5 = Room(
    "Forgotten_Tunnel",
    "A cold and narrow tunnel."
)
room5.add_room_item(item5)

room6 = Room(
    "Buried_Chamber",
    "The final chamber is filled with old trash."
)

room6.add_room_item(item6)

list_of_rooms = [
    starting_room,
    room1,
    room2,
    room3,
    room4,
    room5,
    room6
]

# =========================
# INTRO
# =========================

with open("intro.txt", "r") as file:
    intro = file.read()
    print(intro)


with open("instructions.txt", "r") as file:
    instructions = file.read()
    print(instructions)


print("Welcome to the Dim dungeon")


# =========================
# LOAD / NEW GAME
# =========================

save_data = None

if os.path.exists(SAVE_FILE):

    choice = input(
        "A saved game was found. Load it? (yes/no): "
    ).strip().lower()

    if choice == "yes":

        save_data = load_game()

        if save_data is not None:
            name = save_data["name"]
            age = save_data["age"]
            location = save_data["location"]

            print(f"Welcome back, {name}!")
            print(f"You are currently in: {location}")
            

        else:
            age = int(input("What is your age? "))
            name = input("What is your name? ")
            location = starting_room.name

    else:

        age = int(input("What is your age? "))
        name = input("What is your name? ")
        location = starting_room.name

else:

    age = int(input("What is your age? "))
    name = input("What is your name? ")
    location = starting_room.name


# =========================
# AGE CHECK
# =========================

if age < 12:
    print("You are a minor, Exiting")
    exit()


# =========================
# CREATE PLAYER
# =========================

print(f"Hello {name}, Welcome to Dim Dungeon")

player = Player(
    name,
    age,
    location
)

player.locations = list_of_rooms
#show_current_room(player)

#player.locations = list_of_rooms


# =========================
# GIVE ITEMS
# =========================

if save_data is not None:

    # Load the backpack from the save file
    player.backpack = save_data["backpack"]

    print(f"Your backpack: {player.backpack}")

else:

    # Only give the Shovel when starting a NEW game
    player.collect_item()
    show_current_room(player)

# =========================
# MAIN MENU
# =========================

def main_menu(player):

    while True:

        print("\n--- MAIN MENU ---")

        print(
            "Available commands: "
            "'hello', "
            "'help', "
            "'lopeta', "
            "'backpack', "
            "'rest', "
            "'pickup ,"
            "'move', "
            "'save_game', "
            "'load_game'"
        )

        command = input("Enter command: ").strip().lower()


        # =========================
        # EXIT
        # =========================

        if command == "lopeta":

            print("Thanks for playing. Until next time!")

            break

        # =========================
        # SAVE
        # =========================

        elif command == "save_game":

            save_game(player)

        # =========================
        # LOAD
        # =========================

        elif command == "load_game":

            save_data = load_game()

            if save_data is not None:

                player.name = save_data["name"]
                player.age = save_data["age"]
                player.location = save_data["location"]
                player.backpack = save_data["backpack"]

                print(f"Welcome back, {player.name}!")
                print(f"You are currently in: {player.location}")
                print(f"Backpack: {player.backpack} ")

        # =========================
        # HELLO
        # =========================

        elif command == "hello":

            print("Hello there!")


        # =========================
        # HELP
        # =========================

        elif command == "help":

            print("Type 'lopeta' to exit the program.")


        # =========================
        # BACKPACK
        # =========================

        elif command == "backpack":

            commandB = input(
                "Choose an action: add_item or open_backpack: "
            )

            if commandB == "add_item":

                add_item()

            elif commandB == "open_backpack":

                print(player.backpack)
                get_total_weight(player)

        # =========================
        # REST
        # =========================

        elif command == "rest":

            commandC = int(
                input("How many hours do you want to rest? ")
            )

            rest(commandC)

        # =========================
        # MOVE
        # =========================

        elif command == "move":

            commandD = input(
        "Choose where you want to go: "
        "up, down, left, right: "
        ).strip().lower()

            old_location = player.location

            player.move(commandD)

            if player.location != old_location:

                print(f"You moved to {player.location}")
                show_current_room(player)
                print(f"Your backpack: {player.backpack}")


        # =========================
        # Picks up trash from the current room.
        # =========================

        elif command == "pickup":

            player.collect_item()

            get_total_weight(player)

            if check_game_end(player):
                break

    else:

        print("Unknown command. Please try again.")

# =========================
# START GAME
# =========================

main_menu(player)
