import re
import operator
from collections import defaultdict

#import collections

dict = defaultdict(int)
with open('access_log') as f:
    matches = (re.findall(r'(\d*.\d*.\d*.\d*)\s-',f.read()))
    for match in matches:
        if match in dict:
             dict[match] = dict[match] + 1
        else:
            dict[match] = 1
#iplist = []
for key in sorted(dict, key=dict.get, reverse=True)[:10]:
    #iplist.append(key)
    print(key, dict[key])


# ##### BASH
# #  ~/myworkspace/python/swiggy  cat access_log | awk '{print $1}' | sort | uniq -c | sort -nr | head -10
#  290 76.97.16.122
#  161 217.16.8.81
#  137 178.131.1.247
#  125 94.23.245.128
#  121 95.229.208.133
#  110 217.16.3.142
#   97 192.188.242.80
#   95 91.121.147.225
#   86 94.199.178.9
#   71 216.119.135.66




# with open('access_log') as fh:
#     for line in fh:
#         pattern = re.search(r'(\d*.\d*.\d*.\d*)\s-\s-\s\[.*]\s["](.*)["]',line)
#         print(pattern.group(1) + "=>" + pattern.group(2))




# //cat access_log | awk '{print $7}' | sort | uniq -c | sort -nr | head -10
#  141 //index2.php?option=com_google&controller=../../../../../../../../../../../../../../../../../../../../../../../..//proc/self/environ%0000
#  104 //index.php?option=com_smestorage&controller=../../../../../../../../../../../../../../../../../../../../../../../../proc/self/environ%0000
#   99 //index.php?option=com_jeformcr&view=../../../../../../../../../../../../../../../../../../../../../../../../proc/self/environ%0000
#   96 //index.php?option=com_joomlapicasa2&controller=../../../../../../../../../../../../../../../../../../../../../../../../proc/self/environ%0000
#   78 //index.php?option=com_shoutbox&controller=../../../../../../../../../../../../../../../../../../../../../../../../proc/self/environ%0000
#   75 //index.php?option=com_jresearch&controller=../../../../../../../../../../../../../../../../../../../../../../../../proc/self/environ%0000
#   73 //index.php?option=com_rpx&controller=../../../../../../../../../../../../../../../../../../../../../../../../proc/self/environ%0000
#   72 //index.php?option=com_ninjarsssyndicator&controller=../../../../../../../../../../../../../../../../../../../../../../../../proc/self/environ%0000
#   58 //index.php?option=com_weberpcustomer&controller=../../../../../../../../../../../../../../../../../../../../../../../../proc/self/environ%0000
#   54 //index.php?option=com_jvehicles&controller=../../../../../../../../../../../../../../../../../../../../../../../../proc/self/environ%0000