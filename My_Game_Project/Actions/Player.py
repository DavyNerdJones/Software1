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
            self.collect_item("Sword_Of_Infinity")
        elif direction == "right":
            self.location = "Ominus_Corridor"
            self.collect_item("Hammer_Of_Justice")
        elif direction == "up":
            self.location = "Sharp_Dungeon"
            self.collect_item("Bow_Of_Speed")
        elif direction == "down":
            self.location = "Prison_Cell"
            self.collect_item("Mace_Of_Wrath")

   
   
    def collect_item(self, item):
        """Picks up an item from the current room and adds it to inventory. Well hopefully."""
        room_item = item

        if room_item:
            #self.location.remove_item(room_item)
            self.backpack.append(room_item)
            #self.location.item = None  # Remove the item from the room
            print(f"You picked up: {item}")
        else:
            print(f"There is no item with a Name : '{item}' here.")
