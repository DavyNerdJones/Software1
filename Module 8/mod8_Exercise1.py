seasons_of_the_year = ("winter" , "spring" , "summer" , "autumn")

def get_season(month):

    if month in range(1, 3) or month ==12:
        return seasons_of_the_year[0]
    elif month in range(3, 6):
        return seasons_of_the_year[1]
    elif month in range(6, 9):
        return seasons_of_the_year[2]
    elif month in range(9, 12):
        return seasons_of_the_year[3]
    else:
        return ("Please enter a number between 1 and 12.")

    
month = int(input("Enter the number of a month (1-12): "))

if month >= 1 and month <= 12:
    print(f"You entered: {month}")
    print(f"The season is {get_season(month)}.")
else:
    print(f"You entered: {month}")
    print(get_season(month))


"""
NOTE TO SELF else:
        return ("Please enter a number between 1 and 12.")


in the function doesnt work with else print "blub bluh"        
needs the return, or it returns "NONE" along with the print "bluh bluh"
"""