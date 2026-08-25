talents = float(input ( "Enter talents: "))
pounds = float(input ("Enter pounds: "))
lots = float(input ("Enter lots: "))


talents_grams = talents*20*32*13.3
pounds_grams = pounds*32*13.3
lots_grams = lots*13.3


total_grams = talents_grams + pounds_grams + lots_grams
kilograms = int(total_grams/1000)
remaining_grams = total_grams %1000

print("The weight in modern units: ")
print(f"{kilograms} kilograms and {remaining_grams:.2f} grams.")