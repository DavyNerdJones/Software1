menu_list = "Select option : \n1. add \n2. substract \n3. multiply \n0. exit\n"
selection = input(menu_list)

while selection !="0":

    first_number=float(input("first number: "))
    second_number=float(input("second number "))

    if selection =="1":
        print(f"Result: {first_number + second_number}")

    if selection =="2":
        print(f"Result: {first_number - second_number}")

    if selection =="3":
        print(f"Result: {first_number * second_number}")


    menu_list = "Select option: \n1. add \n2. substract \n3. multiply \n0. exit\n"
    selection = input(menu_list)