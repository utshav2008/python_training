# Strings are immutable and can not be changed

a = "Hello, World!"     # String literals in python are surrounded by either single quotation marks, or double quotation marks.

print(a)                # Print the string
print(a[1])             # Print character at position 1
print(a[2:5])           # Does the slicing and prints the characters from position 2 to 4

print(len(a))           # Get the length of String
print(a.strip())        # Removes any whitespaces from the beginning or the end

print(a.lower())        # Convert all characters to lower
print(a.upper())        # Converts all characters to upper

print(a.replace('H','J')) # It creates a new string as the string are immutable
print(a)                  # This proves that the original string was not changed

print(a.split(','))     # This is used to split the strings with a given separator

#==============

x = input("Enter your name:") # Take input from the user
print("Hello, ", x)           # one way of printing
print("Hello, {}".format(x))  # Other way pf printing and this should be preferred

