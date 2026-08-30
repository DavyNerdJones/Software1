cabin_class = "Enter the cabin class (LUX, A, B, or C): "
selection = input(cabin_class)

if selection =="LUX":
        print(f"Upper-deck cabin with a balcony.")

elif selection =="A":
        print(f"Above the car deck, equipped with a window.")

elif selection =="B":
        print(f"Windowless cabin above the car deck.")

elif selection =="C":
        print(f"Windowless cabin below the car deck.")
        
elif selection != cabin_class:
    print(f"Invalid cabin class.")