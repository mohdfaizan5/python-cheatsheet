"""# A List is a collection which is ordered and changeable. Allows duplicate members."""

#The first item in the list is 0 indexed
#

#create a list
#1)method
num = [1, 2 ,3 ,4, 4]
fruits = ["orrange", "melon", "apple"]
#2)using a constructor
num2 = list((1, 2, 3 ,4 ,4))

#print or work on 2 or more items in a list
print(fruits[0],[2])
#get a particular value
print(fruits[2])

#get len of a list
print(len(fruits))

#append(add) to a list
fruits.append("Mangoes")

#remove from list
fruits.remove("apple")

#insert into position
fruits.insert(2, "strawberry")

#remve from pop(particular position) 
fruits.pop(0)

#reverse the list
fruits.reverse()

#sort list
fruits.sort()

# reverse the sort
fruits.sort(reverse=True)

#insert in position
fruits.insert(2, "graphes")

#remove at particular position
fruits.pop(2)

#change value
fruits[0] = "blue berries"

print(fruits)

#Extend function

