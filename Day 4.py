""" slicing = create a substring by extracting elements from another string
           indexing[] or slice()
           [start : stop : step]
            inclusive: exclusive """

# indexing operation

name = "Prawin Kumar"

fname = name[:6]
lname = name[6:]
first_name = name[3:6]
firstname = name[3:6:2]
funky_name = name[::2]
reversed_name = name[::-1]

print(fname)
print(lname)
print(first_name)
print(firstname)
print(funky_name)
print(reversed_name)

# slicing operation

website1 = "http://google.com"
website2 = "http://wikipedia.com"


sliced = slice(7, -4)

print(website1[sliced])
print(website2[sliced])

