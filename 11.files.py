# Python has functions for creating, reading, updating, and deleting files.

# Open a file
myFile = open('myfile.txt', 'w')

# Get some info
print('Name: ', myFile.name)
print('Is Closed : ', myFile.closed)
print('Opening Mode: ', myFile.mode)

# Write to file
myFile.write('I love Python')
myFile.write(' and JavaScript')
myFile.close()

# Append to file
myFile = open('myfile.txt', 'a')
myFile.write(' I also like PHP')
myFile.close()

# Read from file
myFile = open('myfile.txt', 'r+')
text = myFile.read(100)
print(text)

# BEST way to work with files is
with open("file_name", "action(r,a,w)") as file:

  # This store each and every line in lines as list items
  lines = file.readlines()


## Dealing with csv with error handling

table = []
try:
    with open(sys.argv[1],"r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            table.append(row)

except FileNotFoundError:
    sys.exit("File does not exist")

