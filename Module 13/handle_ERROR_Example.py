
while True:
    file_name = input("File name: ")
    try:
        with open(file_name, "r") as file:
            data = file.read()
        print(data)
        break
    except FileNotFoundError:
        print("File not found.")
    except IOError:
        print("Error occurred while handling the file.")