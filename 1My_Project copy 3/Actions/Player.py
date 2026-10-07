class Player: #project instructions to add class Player
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.backpack = []  # List of items
        self.location = location  # Current room
        self.locations = [] # Contains all rooms the player can visit in a list.
                            # Doesn't show them to player
        

      # Function that is used to move the player to another room.
      #The connections are "bound" to "force" diffferent paths.
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

   


    #Pick up the first item in the current room (hence the [0] , initial plan was maybe still is)
    #to add another item [1] to each room that would be picked up only after [0] was
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

        print("Current room not found.") #Had this before making the routes forced
                                        #Not brave enough to touch it atm



