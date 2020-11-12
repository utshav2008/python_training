class Solution:
    """
    @param source:
    @param target:
    @return: return the index
    """

    def strStr(self, source, target):
        # Write your code here
        if len(target) == 0:
            return 0

        if len(source) == 0:
            return -1

        for i in range(len(source)):
            if source[i:(i + len(target))] == target:
                return i
            else:
                return -1