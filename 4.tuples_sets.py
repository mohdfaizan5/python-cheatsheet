"""# A Tuple is a collection which is ordered and unchangeable(uneditable). Allows duplicate members."""

# Create tuple [we use parnethases() in]
fruits = ('Apples', 'Oranges', 'Grapes')

# Using a constructor
fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

# Single value needs trailing comma(if , not mentioned it takes as str)
fruits2 = ('Apples',)

# Get value
print(fruits[1])

# Can't change value
fruits[0] = 'Pears'

# Delete tuple
del fruits2

# Get length
print(len(fruits)) 


"""# A Set is a collection which is unordered and unindexed. No duplicate members."""

# Create set
fruits_set = {'Apples', 'Oranges', 'Mango'}

# Check if in set
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Grape')

# Remove from set
fruits_set.remove('Grape')

# Add duplicate[doesn't add or show up any error when we try to add a already existing item]
fruits_set.add('Apples')

# Clear set [u didnt delete the tuple, u just clear the items]
fruits_set.clear()

# Delete
del fruits_set

print(fruits_set)
