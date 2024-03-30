def find_max_string(s):
    l = 0
    max_length = 0
    string_set = set()
    for r in range(len(s)):
        while s[r] in string_set:
            l += 1
            string_set.remove(s[l])
        string_set.add(s[r])
        max_length = max(max_length, r-l+1 )            
    return max_length

print(find_max_string('abcabbad'))