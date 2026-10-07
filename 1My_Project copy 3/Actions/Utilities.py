def rest(hour):
      if 0 < hour and hour <= 6:
        print(f"You rested {hour} hours and healed for 10 HP")   

      elif 6 < hour and hour <= 12:
        print(f"You rested {hour} hours and healed for 20 HP")   

      elif 12 < hour and hour <= 18:
            print(f"You rested {hour} hours and healed for 30 HP")

      elif 18 < hour and hour <= 24:
            print(f"You rested {hour} hours and healed for 40 HP")
      else: print("Invalid number, enter a number between 1 and 24")

def show_current_room(player):
    # Find the room where the player currently is.
    #for room in player.locations

    for room in player.locations:

        if room.name == player.location:

            print(f"\nYou are in: {room.name}")
            print(room.description)

            # Only show this message if there
            # are still items in the room.

            if room.items:
                print("There is something here.")

            return




















"""
def add_item():              #Adds item to backpack, from where, don't know yet
    pr1 = input("Add to your backpack ")
    backpack.append(pr1)
    print(f"{pr1} has been added to your backpack")



def equipment():
    pass


def map():
    print("Opens map.\n Choose where you want to go.")


def get_total_weight(player):

    total_weight = 0

    for item_name in player.backpack:
        total_weight += items[item_name].weight

    print(f"Total weight: {total_weight}")


"""