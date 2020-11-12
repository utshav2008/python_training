class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(data)

    def reverse(self):
        cur = self.head
        prev = None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
# ll.print_list()
ll.reverse()
ll.print_list()

