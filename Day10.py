# list = used to store multiple items in a single variable

food = ["pizza", "hamburger", "hotdog", "spaghetti", "pudding"]   # create a list
print(food)  # print the list
food[0] = "sushi"  # assign new value to the first element
print(food)  # print the updated list
print(food[0])  # print the first element
print(food[-1])  # print the last element
food.append("ice cream")  # add new element
food.append("chocolate")
print(food)     # print the updated list
food.remove("hotdog")  # remove the element from the list
print(food)   # print the updated list
food.pop()   # delete or remove the last element in the list
food.insert(0, "cake")  # insert the new element in the first position
print(food)  # print the updated list
food.sort()  # sort the list
print(food)

for x in food:
    # print the element one by one
    print(x)

food.clear()  # clear the list
print(food)  # print the empty list


