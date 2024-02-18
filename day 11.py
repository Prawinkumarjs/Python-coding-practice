# 2D lists = a list of list

drinks = ["coffee", "soda", "tea"]  # creating new list 1
dinner = ["pizza", "hamburger", "hotdog"]  # creating new list 2
dessert = ["cake", "ice cream"]  # creating new list 3

food = [drinks, dinner, dessert]  # assign the list 1,2,3 to the new variable

print(food)  # print the list
print(food[0])  # print list 1
print(food[0][1])  # print list 1 element 1
print(food[1][-1])   # print list 2 last element
