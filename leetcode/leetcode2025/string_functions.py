### **1. Manipulating Case**
str.upper()  
#Converts all characters to uppercase.
"hello".upper()  # Output: 'HELLO'

str.lower()  
#Converts all characters to lowercase.  
"HELLO".lower()

str.capitalize()  
#Capitalizes the first character of the string.  
"hello world".capitalize()

str.title()  
"hello world".title()  # Output: 'Hello World'

str.swapcase()
"Hello World".swapcase()  # Output: 'hELLO wORLD'


### **2. Checking String Properties**
str.isalpha() 
"hello".isalpha()  # Output: True

str.isdigit()
"123".isdigit()  # Output: True

str.isalnum()  
"hello123".isalnum()  # Output: True

str.isspace()  
"   ".isspace()  # Output: True


str.startswith(substring)  
"hello".startswith("he")  # Output: True


str.endswith(substring) 
"hello".endswith("lo")  # Output: True

### **3. Finding and Replacing**
str.find(substring)
"hello world".find("world")  # Output: 6

str.index(substring)  
"hello world".index("world")  # Output: 6

str.count(substring)  
"hello hello".count("hello")  # Output: 2

str.replace(old, new)
"hello world".replace("world", "Python")  # Output: 'hello Python'

### **4. Splitting and Joining**
str.split(separator)
"hello world".split(" ")  # Output: ['hello', 'world']

str.splitlines()
"hello\nworld".splitlines()  # Output: ['hello', 'world']

str.join(iterable)
", ".join(["hello", "world"])  # Output: 'hello, world'

### **5. Stripping Whitespace**
str.strip()
"  hello  ".strip()  # Output: 'hello'

str.lstrip()
"  hello".lstrip()  # Output: 'hello'

str.rstrip()
"hello  ".rstrip()  # Output: 'hello'

### **6. Formatting**
str.format()
"Hello, {}".format("World")  # Output: 'Hello, World'

### **7. Encoding and Decoding**
str.encode()
"hello".encode("utf-8")  # Output: b'hello'

bytes.decode()
b'hello'.decode("utf-8")  # Output: 'hello'


### **Most Commonly Used in Day-to-Day Coding**
# - **`split()`** and **`join()`** for breaking and combining strings.
# - **`strip()`, `lstrip()`, `rstrip()`** for removing unwanted spaces.
# - **`replace()`** for substitutions.
# - **`startswith()` and `endswith()`** for checking patterns.
# - **`upper()`, `lower()`** for case conversion.
# - **`find()` and `count()`** for locating and counting substrings.