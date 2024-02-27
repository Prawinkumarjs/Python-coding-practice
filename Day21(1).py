# file detection

import os

path = "C:\\Users\\prawi\\PycharmProjects\\Helloworld\\File and Exceptional handling\\Folder"

if os.path.exists(path):
    print("That location exists! ")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isfile(path):
        print("That is a directory! ")
else:
    print("That location doesn't exists! ")

