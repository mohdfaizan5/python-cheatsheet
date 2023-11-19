# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

#
# Create dict
from re import I


dict_name = {
    "key" : "value",    #other key should be seperated with comma ","
    "key1" : "value1",
    "key2" : "value2"
}
  
#when we print on only with dict name
for i in dict_name:
    print(i) #it will just print keys over here

#if we want to print keys along with value then,
print(dict_name, dict_name[i] )


person = {
    'first_name': 'John',  
    'last_name': 'Doe',
    'age': 30
}

"""What if you have to store large no. of data:"""
#i)First create a list
#ii) Then add dictionaries in those ones
students = [
    {"name":"faizan", "age":"18", "isMale":True}
    {"name":"tahir", "age":"17", "isMale":True}
    {"name":""}
]
#how to extract only names of students
for student in students:
    print(students["name"])
    
#how to extract names with isMale
for student in students:
    print(students["name"], students["isMale"] sep=", ") #here sep seprates the 2 words by ", " by default its 1 space
    

# Use constructor
# person2 = dict(first_name='Sara', last_name='Williams')

# Get specific value 
print(person['first_name'])
#other method(get method)
print(person.get('last_name'))

# Add key/value
person['phone'] = '555-555-5555'

# Get dict keys
print(person.keys())

# Get dict items
print(person.items())

# Copy dict
person2 = person.copy()
person2['city'] = 'Boston'

# Remove item
del(person['age'])
#other way with pop
person.pop('phone')

# Clear
person.clear() #just empties the dic 

# Get length
print(len(person2))

# List of dict
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 25}
]

print(people[1]['name'])

values()
The values() method gets the values of the dictionary:

>>> pet = {'color': 'red', 'age': 42}
>>> for value in pet.values():
...     print(value)
...
# red
# 42
keys()
The keys() method gets the keys of the dictionary:

>>> pet = {'color': 'red', 'age': 42}
>>> for key in pet.keys():
...     print(key)
...
# color
# age
There is no need to use .keys() since by default you will loop through keys: