import re
import collections
import csv

download_dir = "numbers.csv"
csv = open(download_dir, "w")
#"w" indicates that you're writing strings to the file

row_title = "minute,number_of_messages\n"
csv.write(row_title)

# for key in dic.keys():
# 	name = key
# 	email = dic[key]
# 	row = name + "," + email + "\n"
# 	csv.write(row)
#regex = r'^(.*? \d+ \d+\:\d+)\:\d+ .*? (.*?)\: .*'
regex = r'(?P<Time>^\w{1,3}\s+\d+\s+\d+\:\d+)\:\d+\s+(?P<Device>.*?)\['
#regex = r'(.*? \d+ \d+\:\d+)'
with open('syslog') as f:
    for line in f:
        print re.search(regex,line).group('Time') + " == " + re.search(regex,line).group('Device')


regexp = r'^(.*? \d+ \d+\:\d+).*'


# minutes = []
# with open('syslog') as f:
#     fh = f.read()
#     min = re.findall(regex, fh)
#     dics = collections.Counter(min)
#
#     for k, v in dics.items():
#         row = k + "," + str(v) + "\n"
    # for line in f:
    #     minutes.append(re.match(regexp, line).groups())
#
# print collections.count()
# for k,v in collections.Counter(minutes).items():
#     row = str(k) + "," + str(v) + "\n"
#     csv.write(row)

