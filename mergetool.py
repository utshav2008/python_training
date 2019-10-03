def merge_the_tools(string, k):
    n = len(string)/k
    print n
    for i in range(0,len(string),3):
        print set(list(string[i:i+3]))




merge_the_tools("AABCAAADA",3)