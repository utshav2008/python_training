class Node:

    def __init__(self, value):

        self.value = value
        self.next = None
        self.previous = None


class DoublyLinkedList:

    def __init__(self, value):
        self.head = Node(value)

    def insert(self, value):
        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
        curr_node.next = Node(value)

    def insert_at(self, at_node, data):

        new_node = Node(data)
        curr_node = self.head
        while curr_node.next:
            if curr_node.value == at_node:
                next_node = curr_node.next
                curr_node.next = new_node
                new_node.next = next_node
            curr_node = curr_node.next


    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.value)
            curr_node = curr_node.next




d = DoublyLinkedList(1)
d.insert(3)
d.insert(4)
d.insert(5)
d.insert_at(4,55)
d.insert(6)
d.insert(7)
d.insert_at(6,100)
d.print_list()