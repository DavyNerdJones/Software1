try:
    with open("save.txt", "r") as file:
        data = file.read()
except FileNotFoundError:
    print("File not found.")
except IOError:
    print("Error occurred while handling the file.")



import os

try:
    os.remove("saaaaave")
except Exception as e:
    print(e)