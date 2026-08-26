cabin_class = "Enter the cabin class : (LUX, A, B, or C)\n"
selection = input(cabin_class)


if selection =="LUX":
        print(f"Enter the cabin class LUX: Upper-deck cabin with a balcony.")

elif selection =="A":
        print(f"Enter the cabin class A: Above the car deck, equipped with a window.")

elif selection =="B":
        print(f"Enter the cabin class B: Windowless cabin above the car deck.")

elif selection =="C":
        print(f"Enter the cabin class C: Windowless cabin below the car deck.")

elif selection != cabin_class:
    print(f"Invalid cabin class.")
