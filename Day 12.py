# tuple = collection which is ordered and unchangeable
#         used to group together related data

student = ("Prawin", 21, "male")

print(student)
print(student.count('Prawin'))
print(student.index('male'))

for x in student:
    print(x)

if "Prawin" in student:
    print("Prawin is here!")
else:
    print("Prawin is not here")
