# string methods

name = "bro code"
age = 21

print(len(name))  # length of the string
print(name.find("e"))  # find the element
print(name.capitalize())  # capitalize the first letter
print(name.upper())  # upper case  all the letter in the string
print(name.lower())  # lower case all the letter in the string
print(name.isnumeric())  # check whether the string is in numeric or not
print(name.count("o"))  # count the particular letter in the string
print(name.count(""))  # count the total value is the string
print(name.replace("o", "a"))  # replace the "o" by "a"
print(name * 5)

# type casting = convert the data types of a value to another data type.


x = 1
y = 2.0
z = "3"

x = float(x)  # here the int is convert to float
y = int(y)  # here the float is convert to int
z = int(z)  # here the string is convert to int

print(x)
print(y)
print(z*3)
