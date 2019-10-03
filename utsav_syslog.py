import re
import collections
import csv

row_title = "minute,number_of_messages\n"

regex1 = r'(?P<Time>\w{1,3}\s+\d+\s+\d+\:\d+)\:'
#regex2 = r'(?P<Time>^\w{1,3}\s+\d+\s+\d+\:\d+)\:\d+\s+(?P<Device>.*?)\['
regex2 = r'(?P<Time>^\w{1,3}\s+\d+\s+\d+\:\d+)\:\d+\s+\w+\s(?P<Device>.*)\['

## For the first log parsing###

with open('syslog','r') as f:
    count = collections.Counter(re.findall(regex1,f.read()))

with open('numbers.csv','w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["minutes","number_of_message"])
    for k,v in count.items():
        row = str(k) + "," + str(v) + "\n"

## For the second log parsing ##

with open('syslog','r') as f:
    for line in f:
        print(re.match(regex2,line).group('Time') + "  " + re.match(regex2, line).group('Device'))
