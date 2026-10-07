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



def add_item():              #Adds item to backpack, from where, don't know yet
    pr1 = input("Add to your backpack ")
    backpack.append(pr1)
    print(f"{pr1} has been added to your backpack")
    
def open_backpack():

    print(f"Your backpack contains: {backpack}")


def equipment():
    pass


def map():
    print("Opens map.\n Choose where you want to go.")