with open("shopping_list.txt" , "r") as file:

    data = file.readlines()
    print(len(data))
