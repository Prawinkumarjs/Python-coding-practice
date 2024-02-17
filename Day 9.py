# Loop control statements = change a loops execution from its normal sequence

# break = used to terminate the loop entirely
# continue = skips to the next iteration of the loop.
# pass = does nothing, acts as a placeholder


# example for break stmt

while True:
    name = input("Enter your name : ")
    if name != "":
        break


# eg for continue stmt

phone_number = "123-456-7890"

for i in phone_number:
    if i == "-":
        continue
    print(i, end="")


# eg for pass stmt

for i in range(1, 21):
    if i == 11:
        pass
    else:
        print(i)
