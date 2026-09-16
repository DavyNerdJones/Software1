class Elevator:
    def __init__(self, bottom_floor , top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor


    def floor_up(self):
        if  self.current_floor < self.top_floor:
            self.current_floor += 1
            print("sssss")
        return

    def floor_down(self):
        if  self.current_floor > self.bottom_floor:
            self.current_floor -=1
        return

    def go_to_floor(self, target_floor):
        if  target_floor < self.bottom_floor or target_floor > self.top_floor:
            return
        
        while self.current_floor < target_floor:
            self.floor_up()
            print(self.current_floor)
            if self.current_floor == target_floor:
                break
                    
        while self.current_floor > target_floor:
            self.floor_down()
            if self.current_floor == target_floor:
                break




h = Elevator(1,1000000)
h.go_to_floor(999999)


"""

needs the break 
or the moodle takes too long and disaproves haHA"
if self.current_floor == target_floor:
                break
                
"""