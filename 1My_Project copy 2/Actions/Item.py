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


def get_total_weight(player):
    total_weight = 0

    for item_name in player.backpack:
        total_weight += items[item_name].weight

    print(f"Total weight: {total_weight}")