# variable = a container for a value. Behaves as the value that it contains
# type of data types
first_name = "Bro"
last_name = "code"  # character that is string
full_name = first_name + " " + last_name  # str method
print("hello" + " " + full_name)

age = 21  # integer
age += 1
print(age)
print(type(age))
print("your age is " + str(age))  # str type casting with integer

height = 250.5  # float
print("Your height is :" + str(height) + "cm")  # str type casting with float
print(type(height))

human = True  # boolean
print(human)
print(type(human))
print("Are you a human :" + str(human))

# multiple assignment =  allows us to assign multiple  variables at the same time in one line of code


# name = "bro"
# age = 21
# attractive = True

name, age, attractive = "bro code", 21, True  # different value for different variable

print(name)
print(age)
print(attractive)

Spongebob = Patrick = Sandy = 30  # same value for different variable

print(Spongebob, Patrick, Sandy)

