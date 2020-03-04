class Computer(object):

    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram

    def arch(self):
        print("CPU is" + self.cpu + "and RAM is" + str(self.ram))



c1 = Computer("core",8)
c2 = Computer("core2",10)
#
# c1.arch()
# c2.arch()

print(id(c1))
print(id(c2))