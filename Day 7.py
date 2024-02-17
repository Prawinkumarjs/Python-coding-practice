""" for loop = a statement that will execute its block of code
           a limited amount of times

           while loop = unlimited
           for loop  = limited """


for i in range(10):  # i is initial value and range between 1 to 10
    print(i+1)   # here 10 is the exclusive value

for i in range(50, 100):  # here 50 is inclusive and 100 is exclusive value
    print(i+1)

for i in range(30, 90, 3):  # here 3 in the jump in the number
    print(i)

for i in "PRAWIN":  # i in string
    print(i)

import time

for seconds in range(10, 0, -1):
    print(seconds)
    time.sleep(1)
print("Happy New Year!")
