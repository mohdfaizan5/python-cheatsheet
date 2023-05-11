# If/ Else conditions are used to decide to do something based on something being true or false
import pdb
x = 21
y = 20

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

# Simple if
if x > y:  #this condition work on boolean answer, if True it excecutes the below code 
  print(f'{x} is greater than {y}')

# If/else
if x > y:
  print(f'{x} is greater than {y}')
else:
  print(f'{y} is greater than {x}')  

#👉we can also write it other way
  
print("ok") if x != y else print("not ok")
#other way of writing#return True if x == y else False 

#we can also use match here
name = input("Enter a name") 
match name:       #it compares match in the variable name
  case "Faizan" | "knight" | "rider" :
    print("Great")
  case "Tahir":  #case check
    print("Ok")   
  #if we want to write else the just add _
  case _:
    print("bad")
 
# elif
    #if the above code becomes true below elif statements will be skipped
if x > y:
  print(f'{x} is greater than {y}')
elif x == y:    #if the above condition was true it would have not come down
  print(f'{x} is equal to {y}')  
else:
  print(f'{y} is greater than {x}')  

# Nested if
if x > 2:
  if x <= 10:
    print(f'{x} is greater than 2 and less than or equal to 10')
    

# Logical operators (and, or, not) - Used to combine conditional statements

# and
if x > 2 and x <= 10:
    print(f'{x} is greater than 2 and less than or equal to 10')

# or
if x > 2 or x <= 10:
    print(f'{x} is greater than 2 or less than or equal to 10')

# not
if not(x == y):
  print(f'{x} is not equal to {y}')


# Membership Operators (not, not in) - Membership operators are used to test if a sequence is presented in an object

numbers = [1,2,3,4,5]

#  in
if x in numbers:        #it checks wheather x(what u want) is present in numbers(the list u specify)
  print(x in numbers)

# not in
if x not in numbers:    #it checks wheather x(what u want) should not be present in numbers(the list u specify)
  print(x not in numbers)

# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
      #bollean results
# is 
if x is y:
  print(x is y)
pdb.set_trace()
# is not
if x is not y:
  print(x is not y)