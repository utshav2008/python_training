myDict = {'ravi': 10, 'rajnish': 9,
        'sanjeev': 15, 'yash': 2, 'suraj': 32}


sorted_dict = dict(sorted(myDict.items(), key = lambda x: x[0]))
print(sorted_dict)