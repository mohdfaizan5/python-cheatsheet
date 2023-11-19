#WHAT WE DID UNTILL NOW WITHOUT USING CLASSES IS PROCEDURAL PROGRAMMING

"""# A class is like a blueprint for creating objects. An object has properties and 
methods(functions) associated with it. Almost everything in Python is an object"""
 
# Create class
class User:

  # Constructor [constructor is an func which runs when initiated in a class]
  def __init__(self, name, email, age):
    self.name = name
    self.email = email
    self.age = age
    
    # Adding Encapsulation of variables... Encapsulation is the concept of making the 
    # variables non-accessible or accessible upto some extent from the child classes
    
    self._private = 1000 # Encapsulated variables are declares with '_' in the constructor.

  def greeting(self):
      return f'My name is {self.name} and I am {self.age}'

  def has_birthday(self):
      self.age += 1
 
 #function for encap variable
  def print_encap(self):
      print(self._private)

# Extend class
class Customer(User):
  # Constructor
  def __init__(self, name, email, age):
      User.__init__(self, name, email, age) #Called proper parent class constructor to make this as proper child inehriting all methods.
      self.name = name
      self.email = email
      self.age = age
      self.balance = 0

  def set_balance(self, balance):
      self.balance = balance

  def greeting(self):
      return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'

#  Init user object
brad = User('Brad Traversy', 'brad@gmail.com', 37)
# Init customer object
janet = Customer('Janet Johnson', 'janet@yahoo.com', 25)

janet.set_balance(500)
print(janet.greeting())

brad.has_birthday()
print(brad.greeting())

#Encapsulation -->
brad.print_encap()
brad._private = 800 #Changing for brad
brad.print_encap()


# Method inherited from parent
janet.print_encap() #Changing the variable for brad doesn't affect janets variable --> Encapsulation
janet._private = 600
janet.print_encap()

#Similary changing janet's doesn't affect brad's variable.
brad.print_encap()


# Self is the method where this object is being called
    #eg: if you create a class "Car" and create a object you don't need to specify the object name for using this

##################################################3333

""" Classes has Attributes(properties) and methods"""

# Attributes are basically variables, that are associated with model objects
    # eg: waiter.is_holding_plate = True
    #     waiter.tables_responsible = [3,4]

# Methods are basically functions, that serve a particular model object as they 
# and come under same class, rather than some free floating functions
    # eg: 

##BASIC WORKING
#  IN OOP WE ARE TRYING TO MODEL REAL WORLD OBJECTS AND THOSE OBJECTS HAVE 
# THINGS(ATTRIBUTE) AND THEY CAN DO THINGS(methods(FUNCTIONS))
    #* it is as combining some piece of data and some funtionality 
        #all together in the same thing
    #* they are called the blue prints

 #eg: here "waiter" is a class and "henry" , "berly" as objects


class CarBlueprint:
    pass

baleno = CarBlueprint()
#object   #class

#OBJECT ATTRIBUTES:
baleno.doors
#object #it attribute

#OBJECT METHODS
baleno.stop() # "." = dot notation
#object #method
        #same as attribute but with parenthesis ()

#FIELDS
baleno.colour = "pale blue"
baleno.seats = 4
    #Since colour and seats are attacted to objects we call them "fields: Data attached to an object"

#ACCESSING THE DATA
print(baleno.colour) #don't capitalize name of field

##CLASS FEATURES
    #METHODS
    #INITIALIZATION
    #HELP TEXT

#INIT METHOD
class User:
    """This is a help text when ever user calls help(ClassName) this is gonna pop 
    up as guidelines and along with it it will print all other methods of that class
     with guidelines """
    def __init__(self): #init = initialization a.k.a "constructor" in other lang 
                       # self is first arg used as reference to 
      pass


