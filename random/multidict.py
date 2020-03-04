import re
import copy
import collections

# /var/log/syslog
line = """Dec  3 00:01:54 Mac Google Chrome Helper[69194]: Couldn't set selectedTextBackgroundColor from default ()
Dec  3 00:02:05 Mac Safari[68992]: KeychainGetICDPStatus: keychain: -25300
Dec  3 00:02:05 Mac Safari[68992]: KeychainGetICDPStatus: status: off
Dec  3 00:02:06 Mac com.apple.xpc.launchd[1] (com.apple.WebKit.Networking.AC8ED90D-0AC0-4666-B213-8BE93DE51E8C[68993]): Service exited with abnormal code: 1
Dec  3 00:03:08 Mac WindowServer[68664]: CGXGetConnectionProperty: Invalid connection 20367
Dec  3 00:03:08 Mac garcon[68729]: host connection <NSXPCConnection: 0x7fc9d8f1eda0> connection from pid 68708 invalidated
Dec  3 00:03:08 Mac WindowServer[68664]: CGXGetConnectionProperty: Invalid connection 20367
Dec  3 00:04:08 Mac WindowServer[68664]: CGXGetConnectionProperty: Invalid connection 20367
Dec  3 00:04:08 Mac garcon[68729]: host connection <NSXPCConnection: 0x7fc9d8f1eda0> connection from pid 68708 invalidated
Dec  3 00:04:08 Mac WindowServer[68664]: CGXGetConnectionProperty: Invalid connection 20367
Dec  3 00:05:08 Mac WindowServer[68664]: CGXGetConnectionProperty: Invalid connection 20367
Dec  3 00:05:08 Mac WindowServer[68664]: CGXGetConnectionProperty: Invalid connection 20367
Dec  3 00:06:08 Mac garcon[68729]: host connection <NSXPCConnection: 0x7fc9d8f1eda0> connection from pid 68708 invalidated
Dec  3 00:06:08 Mac WindowServer[68664]: CGXGetConnectionProperty: Invalid connection 20367"""

# dict
#dict = collections.defaultdict() ## store time ==> count
# matches = re.findall(r'(.*\d\d:\d\d):\d\d.*', line)
# count = collections.Counter(matches)
# print(count)
# print("Minute, Count")
# for i in sorted(count, key= lambda x: x[1])[:5]:
#     print(str(i)+","+ str(count[i]))
# for k,v in sorted(dict1):
#     print(k,v)


## display in timely order
## sort based on ascending value
# print "minutes" +" , "+ "count"
# for item in sorted(order, key=order.__getitem__):
#     print item + "," + str(dict[item])


#============================================

# map dict to dict
# {'Dec 3 00:03' -> {'A':1, 'B':'2', ... , 'Z':'26'} }
map = {}
# # store init dict for later copy
acount = {}

# # init number of agent count
agents = re.findall(r'.*Mac\s(.*)\[\d*\]:?\s.*', line)
for agent in agents:
     if agent not in acount:
         acount[agent] = 0

print(acount)

# # group date and agent into ()
matches = re.findall(r'(\w+\s+\d+\s+\d\d:\d\d).*Mac\s(.*)\[\d+\]:?\s.*', line)
for match in matches:
      date = match[0]
      agent = match[1]
#     # print date + ">> "+ agent
      if date in map:
          if agent in map[date]:
              map[date][agent] =  map[date][agent] + 1
          else:
              map[date][agent] = 0
      else:
          map[date] = copy.deepcopy(acount)
          if agent in map[date]:
              map[date][agent] =  map[date][agent] + 1
          else:
              map[date][agent] = 0

print(map)
# title = "minute"
# for agent in acount:
#      title += "," + agent
# print title
#
# for date in sorted(order, key=order.__getitem__):
#      string = date
#      for agent in map[date]:
#           string += "," + str(map[date][agent])
#      print string

for date in sorted(map):
    string = date
    for agent in map[date]:
        string += "," + str(map[date][agent])
    print(string)