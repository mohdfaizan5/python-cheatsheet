# Abstraction

    Abstraction is a simplification of potentially simply complicated idea



# Different types of errors

1. Syntax error:
    
2. Type error:
3. Indentation error: 
4. Index error 
         (it is comman when ur working with lists)
5. NameError: name 'user' is not defined.
6. UnboundLocalError: local variable 'end_of_game' referenced before assignment

# COMMENTs
      They are known as psudo code this means u can write anything you want


# Operators:

arthemetic operators:
  modules operator(%) = prints the remainder of 2 int
  exponent operator(**) = prints something to its power 
                            ex: 2**3 = 2*2*2 = 8
  argumented assignment operator(+=) / (-=) / (*=)
            intead of writing : x = 5
                                x = 3 + x
            we could write:     x += 3
            

Operator precedence   
        In this mathematical(arthemetical) operator equation excecute based on the priority and order
    #we can change this by appling parenthesis() to the operation we want to excecute first


Comparism Operators 
        #it gives boolean output 
    > and <
    >= and <=
    equality operator ==
    not equality operator !=

logical operators
        #It is used to process complex mathemetical operations
    AND = If both conditions gets satisfied then it gives true
    OR  = If even one condition gets satisfied then it gives true
    NOT = which inverses any value it gives.
    
None
#you can use this when u want noting to be done or there is nothing specify over there
None

#day4 python 

*randomizations(pseudo-random generator)
*modules
    random.randint(x,y) to get a random no between x and y
    random.random()
    random.seed()	

*lists
name-of-list= ["item1", "item2" v]


nested list 
	A list inside a list is called nested list

#creating a list
fruits = ["apples", "mangoes", "banana", "melons"]
vegs = ["ladies-finger", "potato", "tomato"]

#creating a nested list
both = [fruits, vegs]
#if u print those u will get list under list

#day 6
Functions

#making own func except[print(), len(), char()]
def my_function():      #def = defining func #my_function() = name of the func with parenthesis #: it says everything that comes after that needs to be indented completed
    print("Hello")
    print("world11")   
    #
#its not only enough to make a func, whenever u need u need t define it.
#calling the func
my_function()
#name_of_func and #() under parenthesis give 

    #use case
    #instead of writing blocks of code again and again and confuse all

Functions as Input:
#		This means functions that allow input.
def name_of_func(input_value):
	do something with input value
def my_func(name_input):
	print(f"Name: {name_input}")

#calling that function by giving it some input value
my_func("faizan")
#during this process a variable has been assigned:
something   =   123
	  👇		   👇
#	parameter	 Argument

Function with more than 1 input
def func_name(parameter1, parameter2):
	#do something with parameter1
	#do something with parameter2

#arguments
Positional Arguments

def func_name1(a,b,c):
	#do this a
	#do this b ,etc
func_name1(1,2,3)
#here a -> 1 , b -> 2, c -> 3
#this might be lot confusing in some conditions so we have keyword arguments

Keyword argument
#instead of just giving value we are also provide what belongs what
def func_name1(a,b,c):
	#do this a
	#do this b ,etc
func_name1(a=1,b=2,=3)


How to round a number
#method1
import math
math.ceil(no_that_needsToBeRounded) #this could be the no or an variable specifiing it

#method2
round(no_to_round)



what does print() without parameters or arguments mean?
print() #this means it takes my cursor of input to next new line




Slice

Take a slice of a list means take a subset of a data structure like a list
  * We can start from a index and end where ever u want.

for fruit in fruits[1:]: #here
    
#This is only called when the program runned by its name only (it wont work when its called as module.)
if __name__ == "__main__":
    print("name is called")