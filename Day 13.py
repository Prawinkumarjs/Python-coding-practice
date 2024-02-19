# set = collection which is unordered, unindexed. No duplicate value

utensils = {"fork", "spoon", "knife"}          # create a set
dishes = {"bowl", "plate", "fork",  "cup"}


print(utensils)     # print utensils
print(dishes)       # print dishes
utensils.add("napkin")   # add napkin to set
print(utensils)
utensils.remove("fork")    # remove fork from the set
print(utensils)
utensils.update(dishes)      # update elmt of dishes to utensils
print(utensils)
dishes.update(utensils)      # update elmt of utensils to dishes
print(dishes)

print(utensils.difference(dishes))    # find difference in utensils and dishes
print(utensils.intersection(dishes))  # intersect ie common elemt in set

dinner_table = utensils.union(dishes)    # create new variable
print(dinner_table)

for x in dinner_table:
    print(x)


utensils.clear()
print(utensils)
