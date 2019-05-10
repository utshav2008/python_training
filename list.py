#There are four collection data types in the Python programming language:
  #List is a collection which is ordered and changeable. Allows duplicate members.
  #Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
  #Set is a collection which is unordered and unindexed. No duplicate members.
  #Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

frnds = ['Ravi','Gaurav','Piyush','Sushant'] # This is how you create a list
frnds1 = list()                              # initiate a list

print(frnds)   # Printing the list elements, all at once
print(frnds[2]) # Printing the element at position 2

frnds[2] = 'Utsav' # Change the value at specific index, this is allowed as its mutable
print(frnds)        # Confirm the list again and you will notice the change

#Loop
#-------
for i in frnds:     # Loop over the list
    print(i)
#-------

#If item exists
#-------
if 'Utsav' in frnds:     # Check if the name is present in the list
    print('Utsav is present in frnds')

print(len(frnds))    # Print the length of list

frnds.append('Subham')   # Adding new item to the list
print(frnds)

frnds.remove('Utsav')    # Removes item from the list using the item name
print(frnds)

frnds.pop(2)             # Removes item from given index, if no index is given it removes from the end
print(frnds)
frnds.pop()
print(frnds)

del frnds[0]             # Delete at index 0
print(frnds)

frnds.clear()            # Clears the list completely
print(frnds)

# del frnds              # Removes the list completely
# print(frnds)

frnds1 = frnds           # Copy one list to other
print(id(frnds1))        # only the reference is copied
print(id(frnds))         # both the id will be same

frnds2 = frnds.copy()    # Copy to a new list
print(id(frnds2))        # it will have a different id
