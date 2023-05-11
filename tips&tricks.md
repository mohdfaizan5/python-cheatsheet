# Python Tips & Tricks:

### 1.Easy variables
```python
a, b = 3, "name"
```
### 2. Change colour of output
```python
# use "\033[96m" change 96 to different no for colours
print("\033[91mThis is RED")
#but changes upcomming all text
```

### 3.

### 5.Useage of complex numbers
```python
num1 = 999999999
num2 = 999_999_999
#both are the same
```

### 6. Use webbrowser module to open webpage
```python
import webbrowser
webbrowser.open("www.google.com")

```

### 7. String concatinating tips
```python
import webbrowser
webbrowser.open("www.google" ".com")
#both work the same
```

### 8.Multiline string

```python
print("This is\
    faizan")
  #OR
strng = """This is 
faizan""" # To print in same line we can use \
```

### 9.Use in operator instead of forloop
```python
mail = "xyz@fmail.com"
if "@" in mail:
    print("Valid")

```