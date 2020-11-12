#================
#  Best Case O(n)
#================

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hash = {}
        for i in s:
            if i not in hash:
                hash[i] = 0
            hash[i] += 1

        for i in t:
            if i not in hash:
                hash[i] = 0
            hash[i] -= 1

        for k in hash.keys():
            if hash[k] != 0:
                return Fasle
        return True


#========================
# Normal Solution O(nlogn)
#=======================

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s.replace(" ","").lower()) == sorted(t.replace(" ","").lower()):
            return True
        else:
            return False


