# while loop = a statement that will execute its block or code,
#              as long as it's condition remains true

name = ""

while len(name) == 0:
    name = input("Enter your Name : ")

print("HELLO " + name)

named = None

while not named:
    named = input("Enter your Name : ")

print("HELLO " + named)
