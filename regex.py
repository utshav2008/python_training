import re

nameage = """
Janica is 22 and Theon is 33
Gabrial is 44 and Joey is 21
"""

# ages = re.findall(r'\d{1,3}',nameage)
# name = re.findall(r'[A-Z][a-z]*',nameage)
#
# ageDict = {}
# x=0
#
# print(name)
# print(ages)
# # for eachname in name:
# #     ageDict[eachname] = ages[x]
# #     x+=1
# #
# # print(ageDict)

str = "we need to inform him with the information"
for i in re.finditer("inform",str):
    print(i.span())