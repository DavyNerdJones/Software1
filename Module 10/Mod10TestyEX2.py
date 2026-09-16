class Dog:
    def __init__(self, name, year_of_birth, sound="Woof"):
        self.name = name
        self.year_of_birth = year_of_birth
        self.sound = sound

    def bark(self, times):
        for i in range(times):
            print(f"{self.name} + barks + {self.sound}")
        return

class Hotel:
    def __init__(self):
        self.dogs = []

    def dog_checkin(self, dog):
        self.dogs.append(dog)

    def dog_checkout(self, dog):
        self.dogs.remove(dog)

    def greet_dogs(self):
        for dog in self.dogs:
            dog.bark(1)


dog1 = Dog("Max" , 2020)
dog2 = Dog("Boi" , 2022, "Yip Yip yip")

dog3 = Dog("Woof" , 2019, "WOOOOF")
dog4 = Dog ("Jack" , 1990 , "AAARG")

hotel = Hotel()

hotel.dog_checkin(dog1)
hotel.dog_checkin(dog2)
hotel.dog_checkin(dog3)
hotel.dog_checkin(dog4)



hotel.greet_dogs()
print("")
hotel.dog_checkout(dog1)

#hotel.dog_checkout(dog4)

hotel.greet_dogs()