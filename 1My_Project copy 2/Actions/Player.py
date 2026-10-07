class Player: #project instructions to add class Player
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.backpack = []  # List of items
        self.location = location  # Current room
        self.locations = []
        


    def move(self, direction):

        if self.location == "Waiting_Room":

            if direction == "left":
                self.location = "Dark_Cell"

            elif direction == "up":
                self.location = "Sharp_Dungeon"

            elif direction == "right":
                self.location = "Forgotten_Tunnel"

            else:
                print("You cannot go that way.")
                return

        elif self.location == "Dark_Cell":

            if direction == "right":
                self.location = "Ominus_Corridor"

            else:
                print("You cannot go that way.")
                return

        elif self.location == "Sharp_Dungeon":

            if direction == "up":
                self.location = "Prison_Cell"

            else:
                print("You cannot go that way.")
                return

        elif self.location == "Forgotten_Tunnel":

            if direction == "right":
                self.location = "Buried_Chamber"

            else:
                print("You cannot go that way.")
                return

        else:

            print("You are at the end of this route.")

   
   
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



