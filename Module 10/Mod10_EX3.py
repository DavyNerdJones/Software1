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


class Building:
    def __init__(self, bottom_floor, top_floor, elevator):
            self.bottom_floor = bottom_floor
            self.elevators = []
            self.top_floor = top_floor
            for i in range(elevator):
                self.elevators.append(Elevator(bottom_floor, top_floor))

        
    def run_elevator(self, elevator_number, target_floor):
        self.elevators[elevator_number].go_to_floor(target_floor)

    def fire_alarm(self):
        for elevator in self.elevators:
            elevator.go_to_floor(self.elevators[0].bottom_floor)


"""
building = Building(1, 10, 3)
building.run_elevator(0, 5)
building.run_elevator(1, 8)
building.run_elevator(2, 3)
building.fire_alarm()

"""





# Test Building with multiple elevators
#building = Building(1, 10, 3)
#building.run_elevator(0, 5)
#building.run_elevator(1, 3)
#building.run_elevator(2, 8)

# Test single elevator building
##small_building.run_elevator(0, 4)

# Test larger building
#office = Building(1, 6, 5)
#office.run_elevator(0, 4)
#office.run_elevator(4, 2)





#h = Elevator(1,1000000)
#h.go_to_floor(999999)
