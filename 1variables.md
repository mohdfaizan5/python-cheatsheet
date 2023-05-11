# Variables:
   A Variable is a container for a value, which can be of various types. They are also called return types.


## Variable Rules:

  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a charactor or an underscore
  - Can have numbers but, can't start with one

  **Example:**
```py
x = 1           #int
y = 2.5         #float
name = "Faizan" #strz
z = True        #bool --> *First letter start with caps *else it will be str
age = 250       #int
is_married = True #bool
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']  #list
person_info = {
   'firstname':'Asabeneh',
   'lastname':'Yetayeh',
   'country':'Finland',
   'city':'Helsinki'
   }                        #dict
```



# Casting(Type conversions)
Casting: Converting one data type to another data type. We use _int()_, _float()_, _str()_, _list_, _set_
  When we do arithmetic operations string numbers should be first converted to int or float otherwise it will return an error. If we concatenate a number with a string, the number should be first converted to a string. We will talk about concatenation in String section.


x = str(x) #converting a int   --> str
y = int(y) #converting a float --> int


## Numbers

Number data types in Python:

1. Integers: Integer(negative, zero and positive) numbers
   Example:
   ... -3, -2, -1, 0, 1, 2, 3 ...

2. Floating Point Numbers(Decimal numbers)
   Example:
   ... -3.5, -2.25, -1.0, 0.0, 1.1, 2.2, 3.5 ...

3. Complex Numbers
   Example:
   1 + j, 2 + 4j, 1 - 1j


#Overriding behaviour of the Assignment Operator
x = 1 # variable x is assigned to 1
x = 2 # x is now 2 and no longer 1

 #Precedence of Arithmetic Operators — basically BODMAS / PEDMAS rule stating whether addition, multiplication, brackets come first etc


#it can be written in other way as Multiple Assignment

x, y, name, z = 1, 2.5, "faizan", True

#basic math operation

a = x + y

## Built-in Functions:

### print()
    An argument is a value which we can be passed or put inside the function parenthesis
    
