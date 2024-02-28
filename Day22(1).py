# write a file

with open('text.txt', 'w') as file:
    print(file.write('Prawin'))
with open('text.txt') as file:
    print(file.read())
with open('text.txt', 'a+') as file:
    print(file.write('\n Kumar'))
with open('text2.txt') as file:
    print(file.read())

with open('text.txt', 'w+') as file:
    print(file.write('Prawin kumar'))
    print(file.read())
print(file.closed)


text = "hey!\n This is some text about you \n By prawin"

with open('text1.txt', 'w') as file:
    file.write(text)
    # print(file.read())

