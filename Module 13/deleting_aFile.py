import os

if os.path.exists("save.txt"):
    print("file exists")
else:
    print("file doesn't exist")


if os.path.exists("save.txt"):
    os.remove("save.txt")
else:
    print("File not found.")