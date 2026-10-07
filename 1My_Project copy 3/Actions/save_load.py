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

# LOAD GAME


def load_game():
    if not os.path.exists(SAVE_FILE):
        print("No saved game found.")
        return None

    with open(SAVE_FILE, "r") as file:
        save_data = json.load(file)

    return save_data
