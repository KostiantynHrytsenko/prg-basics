with open("pets.txt") as file:
    content = file.read()
    words = content.split()
    print(len(words))