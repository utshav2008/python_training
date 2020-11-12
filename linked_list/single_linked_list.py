class Node:

    def __init__(self, value):
        self.value =  value
        self.next = None


class LinkedList:

    def __init__(self, value):
        self.head = Node(value)

    def insert(self, value):
        '''
        Inserting in a linked list
        :param value:
        :return:
        '''
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
        cur_node.next = Node(value)

    def print_list(self):
        '''
        printing the items in a linked list
        :return:
        '''
        cur_node = self.head
        while cur_node:
            print(cur_node.value)
            cur_node = cur_node.next
            # print(cur_node.value)


l = LinkedList(1)
l.insert(2)
l.insert(4)
l.insert(5)
l.insert(6)
l.print_list()
