class Book :

    def __init__(self, author, status = free):
        self.author = author
        self.status = status


    def borrow(self):
        if self.status == "on loan":
            print(f"book already on loan, can't be borrowed")
        else: self.status = "on loan"
        print ("book borrowed succesfully")



book1 = Book("Maria")

print (f"The author of the book is {book1.author}")






book1.borrow()
book1.borrow()




print(f"License plate: {car1.license_plate} \nMaximum speed: {car1.maximum_speed} km/h\nCurrent speed: {car1.current_speed} km/h \nTravelled distance: {car1.travelled_distance} km")