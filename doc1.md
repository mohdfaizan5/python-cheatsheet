Python:

## 1. What is Array?

See mostly no difference, but in an array we keep static value as we don’t change data type for consistency

```py
import array as arr
my_array = arr.array('d', [1.1, 2.2, 3.3])  # Specify data type ('d' for doubles)
```

### List?

List is a versatile data structure for storing collections of elements.

```py
my_list = [1, 2.5, "hello"] # Can mix data types
```
## 2. Function:

Functions in python are sequences of code or reusable blocks of code that perform a specific task within a program. They are designed to make your code more modular, organized, and easier to maintain. Here's a breakdown of key aspects of functions in Python:

```py
def function_name(parameters):
  """Function documentation (optional)"""
  # Code block defining the function's behavior
  return output (optional)
```

## 3a. Create a file

```py
def create_file_and_add_record(filename, record):

  with open(filename, 'w') as file:
    file.write(record)
  print(f"Record added to '{filename}' successfully.")


filename = "my_data.txt"
record = "Line 1\nLine 2\n"
create_file_and_add_record(filename, record)

```

### 3b. Read and modify a record

```py
def read_and_modify_record(filename, search_phrase, replacement):
    with open(filename, 'r+') as file:
      lines = file.readlines()
      modified = False
      for i, line in enumerate(lines):
          if search_phrase in line:
              lines[i] = line.replace(search_phrase, replacement)
              modified = True
      if modified:
          file.seek(0)
          file.truncate()  # Clear file contents
          file.writelines(lines)
          print(f"Record modified in '{filename}'.")
      else:
          print(f"Search phrase '{search_phrase}' not found in '{filename '.")

# Example usage:
filename = "my_data.txt"
search_phrase = "Line 1"
replacement = "Line 1 (modified)"
read_and_modify_record(filename, search_phrase, replacement)


```


### 3c. Read and delete a record 

```py
def read_and_delete_record(filename, search_phrase):

  with open(filename, 'r+') as file:
    lines = file.readlines()
    modified = False
    new_lines = []
    for line in lines:
      if search_phrase not in line:
          new_lines.append(line)
          modified = True
    if modified:
      file.seek(0)
      file.truncate()  # Clear file contents
      file.writelines(new_lines)
      print(f"Record containing '{search_phrase}' deleted from '{filename}'.")
    else:
      print(f"Search phrase '{search_phrase}' not found in '{filename}'.")

# Example usage:
filename = "my_data.txt"
search_phrase = "Line 2"
read_and_delete_record(filename, search_phrase)

```
