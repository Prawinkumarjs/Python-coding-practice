# user input function method

name = input("what is your name ? : ")   # get the input as default as string
# age = input("How old are you ? : ")   # get the input as string
# age = float(input("How old are you ? : "))  # get the input as float
age = int(input("How old are you ? : "))   # get the input as integer
# age = int(age) + 1  # converting string into integer and add by 1
age = age + 1   # normal increment
height = float(input("How tall are you ? : "))  # get the input as float

print("Hello " + name)  # print the name by string method
print("You are " + str(age) + " years old")  # print the age by typecasting method
print("You are " + str(height) + " cm tall")  # print the height by typecasting method

# math function

import math

pi = 3.14
si = -23
x = 1
y = 2
z = 3

print(round(pi))  # rounding off the number that is pop up the number after the decimal point
print(math.ceil(pi))  # rounding off the number to the nearest great number
print(math.floor(pi))  # rounding  off the number to the nearest smallest number in the set
print(abs(si))  # gives the absolute value
print(pow(pi, 2))  # gives the power to the value
print(math.sqrt(9))  # gives the square root value
print(max(x, y, z))  # give the maximum value
print(min(x, y, z))  # give the minimum value


