class Room: #project instructions to add class Room
    def __init__(self, name, description ):
        self.name = name
        self.description = description
        self.items = [] #can hold many items

    def add_room_item(self, item):
        self.items.append(item)


    def get_room(self, name):
        return name.items