"""

class Item:
    number_of_items = 0
    def __init__(self, name, description , price):
        self.name = name
        self.description = description
        self.price = price
        self.number_of_items += 1


item1=Item("Sword_Of_Infinity", "Sword", 100)

print(item1.name , item1.price)
print(Item.number_of_items)
"""













"""
class Player:
    def __init__(self, name, level, player_id):
        self.name = name
        self.level = level
        self.player_id = player_id
        self.items = []
    def level_up(self):
        self.level += 1
    def add_item(self,item):
        self.items.append(item)

player4 = Player("Sam", 1, 112233)
player4.add_item("sword")
print(player4.items)


player4.level_up()
print(player4.level)

"""

class Field:
    def __init__(self, field_id, name, description):
        self.field_id = field_id
        self.name = name
        self.description = description



field1 = Field(2 , "geo" , "rock")
field2 = Field(4 , "diamond", "gem")

print(field1.name)



