myDict = {'ravi': 10, 'rajnish': 9,
        'sanjeev': 15, 'yash': 2, 'suraj': 32, 'ram':24}


# sorted_dict = dict(sorted(myDict.items(), key = lambda x: x[0]))
# for key, val in sorted_dict.items():
#     print(key, val)

num_list = [(8,4),(3,4),(5,6),(1,2)]
# num_list.sort(key=lambda x:x[1],reverse=True)
# print(num_list)

print(sorted(num_list,key=lambda x:x[1]))