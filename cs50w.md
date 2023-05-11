# CS50W

### Lecture 3 (Intro to Python)

#### Types 

```python
a = None # Use when we have to telling something is lacking with value
# or telling absence of something.
```

## Context in python
* Types
* variable
* conditions
    if 
    if else
* Data structure
   1. String
   2. List - sequence of mutable values.
   3. Tupple - sequence of immutable values.
    `b = (2, 5, 20)`
   4. Sets - collection of unique values.
    `a = {1, 2, "hi"}`
   5. Dict - collction of key-value pairs
* Loop
    for loop
    while loop

* defining functions
* oop
    classes:

```python
class Point:

    #  __init__ = magic method (it calls atomatically when ever object is created)
    def __init__(self, input1, input2):
        self.x = input1
```
### Functional programming
* decorator
    It takes the function as input and returns a modified version of that function
        * In python you can pass function as input to another function or take it as a output of 
        This is called funtional programming paradigm where funtions are themself valuse
How do we tell that we are inside of something ?
    By indentation
```python
def announce(f):
    def wrapper():
        print("about to run the decorator function")
        f()
        print("Done with the function")
    return wrapper

# Using a decorator function here
@announce
def hello():
    print("Hello, world!")

hello()
```

* lamda functions
    Many times we need functions(to use returned values)
     * in dict to sort items accourding
     * some times we require some returned data to something 
    instead of creating a new function and then calling it, we can instead use lambda function
        They are anonymous functions, used when we want some function to use it only once
```python
persons = [
    {"name":"faizan", "age":19}
    {"name":"tahir", "age":18}
]
# it will throw value error when we sort without specifing any key reference
persons.sort(key= lambda person: person["name"])
                #       what_func_take: what_to_return

```
* Exceptions

sys.exit(1) # 1 means something went wrong


Vocabulary 
* parse this exception


    `




