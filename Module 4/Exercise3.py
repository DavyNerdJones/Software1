gender =input("Enter biological gender (male/female): ")
hemoglobin_value =float(input("Enter hemoglobin value (g/l):"))

gender = gender.lower()

if gender == "male" and (134 <= hemoglobin_value and hemoglobin_value <= 167):
    print(" Your hemoglobin is normal.")
elif gender == "male" and (167 < hemoglobin_value):
    print(" Your hemoglobin is high.")
elif gender == "male" and (hemoglobin_value < 134):
    print(" Your hemoglobin is low.")
elif gender =="female" and (117 <= hemoglobin_value and hemoglobin_value <= 155):
    print(" Your hemoglobin is normal.")
elif gender =="female" and (hemoglobin_value < 134):
    print(" Your hemoglobin is low.")
elif gender =="female" and (hemoglobin_value > 167):
    print(" Your hemoglobin is high.")
if (gender!= "male" and gender != "female" ):
    print("invalid gender")