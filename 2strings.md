# STRINGS:
 
Strings in python are immutable (we cannot change them, whenever we make changes it creates new string in memory)
  Strings in python are surrounded by either single or double quotation marks. 


a string in python is like a object:
```python
name = "Faizan"
age = 18
```

 Concatination:
```python
print("Hello my name is "+ name + " I'm " + str(age))
```
 this cannot be excecuted with performing concatination: as it requires
                                                        the same data type: age --> str(age)
   You can also do this with using 2 arguments:
print("hello ", name) here inside parenthesis is 1 argument and other 1 is name
            if you add other argument in this manner then a space is added by default.
 
What if we want to use "" in the print func??
you can use \ backslash over there
```python


```
print("Faizan\"is mayname")   \ is escape charactor

String Formatting

 1)Arguments by position:
```python


```
print("Hello my name is {name} and I'm {age}".format(name=name, age=age))

 2)F-strings(formating strings)
```python


```
print(f"Hello my name is {name} and am {age}")

String Methods

s = "hello woRld"


method / function for a variable
    when we add dot(.) after a variable we could add functions that are specific to variable type 
```python


```
         dir(variable_name)

 capitalize string (only first letter gets capitalize)
```python


```
print(s.capitalize())

To remove whitespace(spaces) between strings
```python


```
print(s.strip)
  
make all upper[convert all alphabets to uppercase]
```python

```
print(s.upper())

make all lower
```python

```
print(s.lower())

swap case[changes upper -> lower & lower -> upper]
```python

```
print(s.swapcase())

get length [variable should inside the parenthesis]
```python

```
print(len(s)) it returns length of all existing alphanumeric charactors as well as spaces

 Count func
 sub = 'h'
print(s.count("l")) it returns the count of a particular letter

replace
```python

```
print(s.replace('woRld', "everyone"))



 Starts with
```python

```
print(s.startswith('hello'))

 Ends with
```python

```
print(s.endswith('d'))

 Split into a list  revise
```python

```
print(s.split())

 Find position
```python

```
print(s.find('r')) it returns the index of that letter
 python is a case sensitive lang:
     if we pass 'R' here
     it will give '-1' which means it doesn't exist

 Is all alphanumeric
```python

```
print(s.isalnum())

 Is all alphabetic
```python

```
print(s.isalpha())

 Is all numeric
```python

```
print(s.isnumeric())


how to rep;ace a letter form a word :
       -string slicing:

syntax: | string = string[:position] + character + string[position+1:]
```python

```
string = "Mohd_aizan"
position = 5
to_replace_with = "F"

string = string[:position] + to_replace_with + string[position+1:]
```python

```
print(string)


  '''
  This is a 
  multiline comment
  or docstring (used to define a functions purpose)
  can be single or double quotes
  '''