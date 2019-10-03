name = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}

#adding new item in the dictionary
name['Utsav'] = 28

#Print keys in the dictionary
for k in name:
    print(k)
#or
for k in name.keys():
    print(k)

#Print values in the dictionary
for v in name.values():
    print(v)

# Print key and value of the dictionary
for k,v in name.items():
    print(k,v)

# Sort the dictionary based on keys
for k in sorted(name):
    print(k)

# Sort the dictionary based on values
for key, value in sorted(name.items(), key=lambda item: item[1]):
    print("%s: %s" % (key, value))

# Sort the dictionary based on values in reverse order
for key, value in sorted(name.items(), key=lambda item: item[1], reverse=True):
    print("%s: %s" % (key, value))
