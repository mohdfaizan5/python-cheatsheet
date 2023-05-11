# Python program to demonstrate
# writing to file

# Opening a file
file1 = open('myfile.txt', 'w')
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
s = "Hello\n"

# Writing a string to file
file1.write(s)

# Writing multiple strings
# at a time
file1.writelines(L)

# Closing file
file1.close()

# Checking if the data is
# written to file or not
file1 = open('myfile.txt', 'r')
print(file1.read())
file1.close()


###############################################3

# HOW TO MAKE REQUIREMENT FILE FOR A PROJECT

#install this
pip install pipreqs

# How to use just run it in a folder you want to create

#to create requirement stuff, go to that folder and execute
pipreqs ./

#################################################33

# HOW TO CONVERT ANY PY FILE TO PEP8 FORMAT
pip install autopep8

#run by file name
autopep8 --in-place --aggressive --aggressive <filename>


##################3
#HOW TO PEP8 FORMAT A FILE
autopep8 --in-place --aggressive --aggressive <FILE_NAME>

#HOW TO FORMAT A WHOLE FORDER TO PEP8 FORMAT (-R IS RECURSION)
autopep8 --in-place --aggressive --aggressive -r <folder name>

eg : autopep8 --in-place --aggressive --aggressive -r enrollment\ parser\ project/ or "enrollment parser project"


##################################33
#HOW TO USE COLOUR IN TEXT
from colorama import Fore, Style

# Change RED to desired color
print(Fore.GREEN +"\nout of the program")
# It finally resets back to normal text
print(Style.RESET_ALL)


############# How to deal with FileExistsError

import os
import shutil

path = 'path_to_my_folder'
if not os.path.exists(path):
    os.makedirs(path)
else:
    shutil.rmtree(path)           # Removes all the subdirectories!
    os.makedirs(path)