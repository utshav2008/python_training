#=========
# O(n)
#=======

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {'(':')','{':'}','[':']'}
        for paran in s:
            if paran in brackets:
                stack.append(paran)
            elif len(stack) == 0  or brackets[stack.pop()] != paran:
                return False
        return len(stack) == 0