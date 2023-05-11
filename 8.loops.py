"""# A for loop is used for iterating[to do something (set of operations) again and again]
 over a sequence (that is either a list, a tuple, a dictionary, a set, or a string)."""
import pdb
people = ['John', 'Paul', 'Sara', 'Susan']

# Simple for loop
for person in people:                   #person is keyword we are specifing to use it for further calculations.
  print(f'Current Person: {person}')    #and using person[as indivisual] for print
 
# Break[it break/ends the program after it meets the condition specified]
for person in people:
  if person == 'Sara': #if this condition satisfies then it will break the code and dont excecute further operations
    break                 #the code before is executed, in this case first john and paul are printed:
  print(f'Current Person: {person}')

# Continue
for person in people:
  if person == 'Sara':
    continue
  print(f'Current Person: {person}')


"""Range"""
# range[the limits btw which something can vary]
for i in range(len(people)):
  print(people[i])

# we can also give custom range: #we here can specifiy the limits within which is should function:
for i in range(0, 11):    #its gonna print from0 to 10 but not 11
  print(f'Number: {i}')   

#we can also give step range(which )
for _ in range(0, 11, 2):     
  faizan = True           
#for doing soming thing n. no. of times
for i in range("""#write no. of times u wanna do something"""):
  #what to do repeatedly
  print("ok")
  
for _ in range(4):   #if ur thinking to not use that variable further u can just mention _ , u or others will understand it.
  print("helo")

#How to get in or out of loop
  break #to get out of loop
  continue # to get back and start loop  


# While loops execute a set of statements as long as a condition is true.
#syntax of while loop
while something_is_true:
    #keep on doing this untill 👆 condition is true:
    #do this 
    #then this   
    count = 0                     #we are specifing a base no from which we carry forward further calculations;
    while count < 10:             #we are giving a condition from which it will create a loop
      print(f'Count: {count}')    #until which it will continue the loop
      count += 1                  #it will be adding 1 until it satisfies the above code:



#to check something is not true 
while my_condition() != True:  #writing parenthesis is must this tells check that func
      #do this untill 👆 above condition satisfies.

# or
      
while not my_condition(): #untill not getting my condition dont stop
      # do this
    print("hey")
    