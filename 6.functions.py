""" A function is a block of code which only runs when it is called. 
     In Python, we do not use curly brackets, we use indentation with tabs or spaces"""

import pdb
# Create function



#👉In this we are defining a simple function:
def hello():    #def means define a new function
    print("hello")
#just defining a function is not enough we also need to call them:
hello() #() parenthisis say that this is a function


#👉In this we are defining a function with a parameter
def hello(parameter):
    print(f"Hello {parameter}")

#calling a funtion with a parameter 
hello("faizan") #computer automatically assigns "faizan" as parameter and further computes faizan in the func

#👉In this we are defining a function with 2 or more parameters
def hello(parameter1, parameter2):
    print(f"Name:{parameter1}")
    print(f"Age: {parameter2}")

#calling a function with 2 parameter 
    #here we give 2 parameter while calling a function seperated with commma ","
hello("faizan","18") #computer automatically assigns faizan as name
#                                                     18 as age

#things to keep in mind

#🟢 Scope: Anything that is assigned inside the function can't be used outside the function that is scope
#🟢 return
#🟢 
#🟢
#🟢


def sayHello(name='Sam'):
    print(f'Hello {name}')


# Return values
def getSum(num1, num2):
    total = num1 + num2
    return total            #use return value in some conditions to store further.


# A lambda function is a small anonymous(doest need to have a name) function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getSumL = lambda num1, num2: num1 + num2

print(getSum(10, 3))
pdb.set_trace()