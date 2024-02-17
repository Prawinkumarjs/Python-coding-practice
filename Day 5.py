# if statement = a block of code that will execute if its  condition is true

age = int(input("How old are you?: "))

if age >= 18:
    print("You are an adult!")
else:
    print("You are a child! ")

# logical operators (and,or,not) = used to check if two or more conditional statement is true

temp = int(input("what is the temperature outside?: "))

if temp >= 0 and temp <=30:
    print("The temperature is good today!")
    print("Go Outside!...")
elif temp < 0 or temp > 30:
    print("The temperature is bad today!")
    print("Stay Inside!...")



