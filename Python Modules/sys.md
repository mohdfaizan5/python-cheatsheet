# System Module

### Funtions

Find length of argv

```python
len(sys.argv)
```

indexing in sys.module
```python
sys.argv[0] #file name
sys.argv[1] #first thing
```

1. stdin()
    s
2. stdout()
    It is used to display output directly to the screen console.
```python
import sys
sys.stdout.write('Geeks')
```
3. stderr:
 Whenever an exception occurs in Python it is written to sys.stderr.

# Command Line Arguments
Command-line arguments are those which are passed during the calling of the program along with the calling statement. To achieve this using the sys module, the sys module provides a variable called sys.argv. It’s main purpose are:

* It is a list of command-line arguments.
* len(sys.argv) provides the number of command-line arguments.
* sys.argv[0] is the name of the current Python script.

```python
# Python program to demonstrate
# command line arguments

import sys

# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)

# Arguments passed
print("\nName of Python script:", sys.argv[0])

print("\nArguments passed:", end = " ")
for i in range(1, n):
	print(sys.argv[i], end = " ")
	
# Addition of numbers
Sum = 0

for i in range(1, n):
	Sum += int(sys.argv[i])
	
print("\n\nResult:", Sum)

```

#Sys.exit
sys.exit([arg]) can be used to exit the program. The optional argument arg can be an integer giving the exit or another type of object. If it is an integer, zero is considered “successful termination”.

Note: A string can also be passed to the sys.exit() method.

Example: 

```python
# Python program to demonstrate
# sys.exit()


import sys


age = 17


if age < 18:
	
	# exits the program
	sys.exit("Age less than 18")	
else:
	print("Age is not less than 18")

```


import sys

if sys.argv[1] == "fa":
    print("ok") 
else:
    print("not working")
