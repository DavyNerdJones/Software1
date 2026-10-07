class Item:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight




# ITEMS

item0 = Item("Shovel", 7)
item1 = Item("DumpsterFire", 17)
item2 = Item("WetCardboard", 28)
item3 = Item("HalfEatenBagel", 11)
item4 = Item("MoldyCrouton", 27)
item5 = Item("SoggySock", 6)
item6 = Item("BrokenGlasses", 2)


# ITEM DICTIONARY

items = {
    item0.name: item0,
    item1.name: item1,
    item2.name: item2,
    item3.name: item3,
    item4.name: item4,
    item5.name: item5,
    item6.name: item6
}




# Add the weight of every item in the backpack.

def get_total_weight(player):
    total_weight = 0

    for item_name in player.backpack:
        total_weight += items[item_name].weight

    print(f"Total weight: {total_weight}")


def check_game_end(player):

    final_rooms = [
        "Ominus_Corridor",
        "Prison_Cell",
        "Buried_Chamber"
    ]

    if player.location in final_rooms:

        print("\n==============================")
        print("        YOU REACHED THE END")
        print("==============================")

        print(f"You reached: {player.location}")

        get_total_weight(player)

        print("You collected all the trash you could!")
        print("Thanks for playing Dim Dungeon!")

        return True

    return False