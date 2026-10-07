class Player: #project instructions to add class Player
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.backpack = []  # List of items
        self.location = location  # Current room
        self.locations = []
        


    def move(self, direction):
        if direction == "left":
            self.location = "Dark_Cell"
            #self.collect_item("Sword_Of_Infinity")
        elif direction == "right":
            self.location = "Ominus_Corridor"
            #self.collect_item("Hammer_Of_Justice")
        elif direction == "up":
            self.location = "Sharp_Dungeon"
            #self.collect_item("Bow_Of_Speed")
        elif direction == "down":
            self.location = "Prison_Cell"
            #self.collect_item("Mace_Of_Wrath")

   
   
    def collect_item(self):

        for room in self.locations:

            if room.name == self.location:

                if room.items:

                    item = room.items[0]

                    self.backpack.append(item.name)
                    room.items.remove(item)

                    print(f"You picked up: {item.name}")
                    return

                else:

                    print("There is no item in this room.")
                    return

    print("Current room not found.")



