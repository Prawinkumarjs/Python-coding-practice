# dictionary = A changeable, unordered collection of unique key:value pair
#              Fast because they use hashing, allow us to access a value quickly

capital = {'USA': 'Washington DC',
           'India': 'New Delhi',       # creating a new dictionary with key : Values
           'China': 'Beijing',         # assign a variable capital
           'Russia': 'Moscow',
           'Japan': 'Tokyo'}

print(capital)     # print the dictionary
print(capital['Russia'])   # call the value by keys
# get method                   # its get the value from dictionary whether it found or not
print(capital.get('Germany'))

capital.update({'Srilanka': 'Cylon'})   # update the dict
print(capital)

capital.update({'USA': "Las vegas"})
print(capital.values(), capital.keys())

capital.pop('China')              # delete the key: values from dict
print(capital)


print(capital.keys())           # print dict keys alone dict_keys(['USA', 'India', 'Russia', 'Japan', 'Srilanka'])
print(capital.values())         # print dict values alone dict_values(['Las vegas', 'New Delhi', 'Moscow', 'Tokyo', 'Cylon'])
print(capital.items())          # print dict with key and values dict_items([('USA', 'Las vegas'), ('India', 'New Delhi'), ('Russia', 'Moscow'), ('Japan', 'Tokyo'), ('Srilanka', 'Cylon')])

for x in capital.items():       # print dict in normal form  ex ('USA', 'Las vegas')
    print(x)

for key,value in capital.items():  # print dict by keys: value method  ex Srilanka Cylon
    print(key, value)

capital.clear()    # clear the dict
print(capital)     # print empty dict with {}
