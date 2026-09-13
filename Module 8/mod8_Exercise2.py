name = input("name: ")

names =set()


while name != "":
    if name in names:
        print("Existing name")
    else:
        print("New name")


    names.add(name)

    name = input("name: ")

    

for name in names:
    print (names)



#Couldn't this be done with lists tuples or dictionaries ?