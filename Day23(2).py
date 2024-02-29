# delete a file

import os

# path = "C:\\Users\\prawi\\PycharmProjects\\Helloworld\\File and Exceptional handling\\Folder\\text2.txt"
path = "C:\\Users\\prawi\\PycharmProjects\\Helloworld\\File and Exceptional handling\\Folder\\empty_folder"


try:
    # os.remove(path)     # delete a file
    os.rmdir(path)        # delete an empty directory
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete that")
else:
    print(path + " was deleted")

