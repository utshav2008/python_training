s = "ABCDCDC"
pattern = "CDC"
n = len(pattern)
match = 0
for i in range(0,len(s)):
    if s[i:i + n] == pattern:
        match += 1

print match


# #=========
# def count_substring(string, sub_string):
#     n = len(sub_string)
#     match = 0
#     for i in range(0, len(string)):
#         if string[i:i + n] == sub_string:
#             match += 1
#     return match
#
#
# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
#
#     count = count_substring(string, sub_string)
#     print(count)

