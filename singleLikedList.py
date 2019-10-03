class Node:

    def __init__(self,data=None):
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

    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        print(total)

    def display(self):
        elems = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            elems.append(cur.data)
        print(elems)

    def get(self,index):
        cur_index = 0
        cur = self.head
        while True:
            cur = cur.next
            if cur_index == index:
                return cur.data
                cur_index += 1

    def erase(self,index):
        cur_index = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_index == index:
                last_node.next = cur_node.next
                return
            cur_index += 1

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




my_list = LinkedList()
my_list.display()
my_list.append(12)
my_list.append(14)
my_list.append(6)
my_list.display()
my_list.erase(0)
my_list.display()