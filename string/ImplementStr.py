source = 'source'
target = 'target'

class ImplementStr:

    def StrStr(self, source, target):
        for i in range(len(source)):
            if source[i:len(target)+1] == target:
                return i
        return -1


implement = ImplementStr()
print(implement.StrStr(source,target))