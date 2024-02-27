# function = a block of code which is executed only when it is called.

def hello():            # def is the keyword for function & create a function
    print("Hello! ")     # print hello!
    print("Have a nice day!")


# call the function
hello()


def helloo(name):            # call the function by name and matching argument
    print("hello! " + name)     # print hello! + argument [name]
    print("Have a nice day!")


# call the function with argument
helloo("Prawin")  # argument 1
helloo("Dude")  # argument 2


def hello(name):
    print("Hello " + name)
    print("Have a nice Day!")


my_name = "Bro"
hello(my_name)


# call the function by pass the two arguments
def helo(first_name, last_name):
    print("Hello! " + first_name + " " + last_name)
    print("Have a nice day! ")


helo("Prawin", "Kumar")    # function(arg1, arg 2)
print("NEXT")
# always keep mind!!!
# when you call the function always give two line empty space (Only for pycharm)


# return statement = Function send python values/object back to the caller.
#                    These values/objects are known as the function's return values.


def multiply(number_1, number_2):      # function with argument 1, 2
    result = number_1 * number_2       # multiple and store the value
    return result                      # return the value


x = multiply(1, 4)     # assign a variable and call the function with arg 1, 2
print(x)               # print the value


# simplified code
def multiply(number1, number2):
    return number1 * number2


x = multiply(6, 9)
print(x)


# own content
def add(a, b):
    return a + b


num_1 = int(input("Enter the number 1 : "))
num_2 = int(input("Enter the number 2 : "))
result = add(num_2, num_1)
print("The Answer is : " + str(result))
