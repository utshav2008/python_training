string_list = ["apple", "banana", "orange", "grape", "kiwi", "melon", "strawberry", "pineapple", "peach", "plum",
               "blueberry", "raspberry", "pear", "apricot", "cherry", "mango", "papaya", "watermelon", "fig", "coconut"]

END = len(string_list)
i = 0

while i <= END-3:
    print(string_list[i:i+3])
    i += 1
print(string_list)