# keyword arguments = arguments preceded by an identifier when we pass them to a function
#                     The order of the arguments doesn't matter, unlike positional arguments
#                     Python knows the names of the arguments that our function receives

def hello(first, middle, last):
    print("Hello " + first + " " + middle + " " + last)


hello("J S ", "Prawin", "Kumar")
hello(last="J S ", middle="Kumar", first="Prawin")    # keyword argument


# nested function calls = function calls inside other function calls
#                         innermost function calls are resolved first
#                         returned value is used as argument for the next outer function


num = (input("Enter a number: "))
num = float(num)
num = abs(num)
num = round(num)
print(num)

# the above code can be expressed in terms of nested function
print(round(abs(float(input("Enter a number :")))))


# variable scope = The region that a variable is recognized
#                  A variable is only available from inside the region it is created.
#                  A global and locally scoped versions of a variable can be created

name = "PrawinKumar"     # global scope (available inside & outside functions)


def display_name():
    # name = "Prawin"      # local scope (available only inside this function)
    print(name)


display_name()
print(name)


def display_name():
    name = "Prawin"      # local scope (available only inside this function)
    print(name)


display_name()


"""
python follows the rule
L = Local
E = Enclosing
G = Global
B = Built-in

"""
