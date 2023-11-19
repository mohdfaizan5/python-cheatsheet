# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

#Method1 to import a module:
import random

coin = random.choice(["head","tail"]) # here we random is module, choice is the name of the function
#                                       parenthesis () tells its function, and [] is a list                                      
#  #things to keep in mind:
#     *Here we can use any function because we have imported the whole module

#Method Instead we could be specific and more clear what we are import and which func are we using from it.
from random import choice

coin = choice(["head","tail"]) #here choice is stored in local variable
#   Things to keep in mind:
#     * Here only choice function can only be used.
#     * this can help in situation where u are using choice many times, instead of making code long we can use it.


"""Command-line Arguments"""
#       WE can give the arguments or inputs directly beside the name of the file while excecuting

#There is a module called sys(system)
import sys

sys.argv  #argumetvector - in this everything u enter after file name is taken into the program as list

#Eg: Program that prints name of the user, while giving name during runtime.

import sys

print("Hello! My name is ", sys.argv[1]) #

#We could also extract name of the program by
print("Hello! My name is ", sys.argv[0])  # 0 specifies the name of the program and further no. as other inputs

#we could also get out of a program if we dont get expected input argument vectors
if not choice:
  sys.exit("You have not given arguments with file name")



##############################################################################################################


# Core modules
import datetime     #we are importing module named datetime for extracing some functions
import time

#import specific func of a module
from datetime import date  #we extracted a specific func(date) instead of importing the whole module(datetime)
from time import time

# Pip module (pip is a package installer)
      #pip3 install camelcase 

# from camelcase import CamelCase
  #pip3 freeze = check existing / install modules

# Import custom module (we need to make a seperate file named validator then import it to there)
import validator      #we are importing a custom module named validator
from validator import validate_email    #we are extracting a func named validate_email in module validator

# # today = datetime.date.today()
# today = date.today()
# timestamp = time()

c = CamelCase() #we assigned a variable called 'c' for camelcase, inorder to make code simple
# print(c.hump('hello there world'))

email = 'test#test.com' #we are giving a input email to check whether its valid or bad
if validate_email(email):
  print('Email is valid')
else:
  print('Email is bad')
