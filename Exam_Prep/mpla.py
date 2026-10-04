"""

x = {'type' : 'fruit', 'name' : 'apple'}

for y in x.keys():
  print(y)

for z in x.values():
  print(z)

"""


"""

x = {'type' : 'fruit', 'name' : 'apple'}
x.update({'color':'green'})
#adds key color value green
print(x)

"""







#Add the key/value pair "color" : "red" to the car dictionary.

"""
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"


print(car["brand"])

"""





"""


x = {'type' : 'fruit', 'name' : 'banana'}
#What is a correct syntax for changing the name from banana to apple?

x.update({'name': 'apple'})

"""


"""

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))

"""


"""

fruits = ('apple', 'banana', 'cherry')
(x, *y) = fruits
print(y)


#(x, *y) = fruits: This uses Python's unpacking feature with the star operator (*).
#Variable x captures the first value ('apple'),
#and the starred variable y collects all remaining values into a list.

"""
"""
list1 = ['a', 'b' , 'c']
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)

print(list1)
"""

"""

fruits = ['apple', 'banana', 'cherry']
newlist = [x for x in fruits if x == 'banana']
print(newlist)

"""
"""
mylist = ['apple', 'banana', 'cherry']
i = 0
while i < len(mylist):
    print(mylist[i])
    i = i + 1

"""

"""


mylist = ["a", "b", "c"]
#mylist.remove("c")  # removes the first element that has value "c"
print(mylist)

mylist.pop(1)
print(mylist)

"""


"""

mylist = ['apple', 'banana', 'cherry']
mylist[2] = 'kiwi'
print(mylist[0])

"""
"""

mylist = ['apple', 'banana', 'cherry']
mylist[1:2] = ['kiwi', 'mango']
print(mylist[2])

fruits = ["apple", "banana", "cherry"]
fruits.insert(1,"lemon")

"""