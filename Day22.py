# read the file

with open('text.txt') as file:
    print(file.read())

print(file.closed)   # it checks whether the file is closed or not it is closed it print true or else it prints false

try:
    with open('text.tx') as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found :(")

