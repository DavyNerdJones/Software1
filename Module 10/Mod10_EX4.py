import random
class Car:
    def __init__(self, reg_number, max_speed):
        self.license_plate = reg_number
        self.maximum_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        if self.current_speed + change >= self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed + change <= 0:
            self.current_speed = 0
        else:
            self.current_speed += change

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

class Race:
    def __init__(self, name, distance, cars):
            self.name = name
            self.distance = distance
            self.cars = cars

    def hour_passes(self):
            for car in self.cars:
                car.accelerate(random.randint(-10, 15))
                car.drive(1)

    def print_status(self):

        for car in self.cars:

            print(f"The car {car.license_plate} speed is {car.current_speed} and has driven this distance: {car.travelled_distance}")

    def race_finished(self):
        for car in self.cars:

            if car.travelled_distance >= self.distance:
                return True
            else:
                 return False



#kept it as def race for so long, NOTE TO SELF read description

#should ask for this, didn't quite get it.


#for car in cars:
    #print(f"The car {car.license_plate} speed is {car.current_speed} and has driven this distance: {car.travelled_distance}")

#HAD TO while "ALL cars" , moodle exceeded time limit error