# *args = parameter that will pack all arguments into a tuple
#         useful so that a function can accept a varying amount of arguments

def add(*stuff):
    added = 0
    for i in stuff:
        added += i
    return added


print(add(1, 2, 3, 4, 5, 6))


# **kwargs = parameter that will pack all arguments into a dictionary
#            useful so that a function can accept a varying amount of keyword arguments


def hello(**kwargs):
    print("Hello " + kwargs['first'] + "" + kwargs['middle'] + "" + kwargs['last'])
    print("Hello " + kwargs['first'] + " " + kwargs['last'])
    for key, value in kwargs.items():
        # print(value)
        print(value, end=" ")


hello(first="prawin", middle="kumar", last='j s ')
