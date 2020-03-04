def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


## 2nd Solution
str = "abracadabra"
l = list(str)
l[5] = "k"
new_str = "".join(l)
print new_str

##Learn
## Join
## Slicing
