class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def display(self):
        cur = self.head
        elem = []
        while cur.next != None:
            cur = cur.next
            elem.append(cur.data)
        print(elem)

    def insert(self, data, index):
        new_node = Node(data)
        cur = self.head
        i=0
        while i != index:
            cur = cur.next
            i+=1
        next_node = cur.next
        cur.next = new_node
        new_node.next = next_node

    def erase(self,index):
        cur = self.head
        i = 0
        while i != index:
            last = cur
            cur = cur.next
            i+=1
        last.next = cur.next


l1 = LinkedList()
l1.append(12)
l1.append(13)
l1.append(14)
l1.insert(26,0)
l1.display()
l1.erase(1)
l1.display()
# l1.length()
# l1.insert(55,1)
# l1.insert(5,2)
# l1.insert(65,3)
# l1.display()
# l1.erase(1)
# l1.erase(2)
# l1.erase(3)
# l1.display()



