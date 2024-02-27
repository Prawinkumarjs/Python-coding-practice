# index operator [] = gives access to a sequence's element(str, list, tuples)

name = 'prawin Kumar'      # create a new  variable

if name[0]:                       # change the small letter to caps
    name = name.capitalize()
print(name)

first_name = name[0:6].upper()    # the string from 0 to 6 that is prawin and convert to caps
print(first_name)
unique_name = name[3:6].upper()   # the string from 4 to 6 that is win and convert to caps
print(unique_name)

last_name = name[7:].upper()       # the string from 7 to last that kumar and convert to caps
print(last_name)

last_character = name[-2]          
print(last_character)
