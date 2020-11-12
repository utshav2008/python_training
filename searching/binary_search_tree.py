##=============================
# Delete node to be covered
#==============================

class Node:
    def __init__(self, value):
        self.value = value
        self.left =  None
        self.right = None


class Bst:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, curr_node):
        if value < curr_node.value:
            if curr_node.left == None:
                curr_node.left = Node(value)
            else:
                self._insert(value, curr_node.left)
        elif value > curr_node.value:
            if curr_node.right == None:
                curr_node.right = Node(value)
            else:
                self._insert(value, curr_node.right)

    def print_tree(self):
        if self.root == None:
            print('Empty')
        else:
            self._print_tree(self.root)

    def _print_tree(self, curr_node):
        if curr_node != None:
            self._print_tree(curr_node.left)
            print(curr_node.value)
            self._print_tree(curr_node.right)

    def height(self):
        if self.root != None:
            self._height(self.root,0)
        else:
            return 0

    def _height(self, curr_node, height):
        if curr_node == None:
            return int(height)
        left_height = self._height(curr_node.left, height+1)
        right_height = self._height(curr_node.right, height+1)
        print(max(left_height,right_height))




bst = Bst()
bst.insert(10)
bst.insert(8)
bst.insert(14)
bst.insert(100)
bst.insert(65)
bst.insert(3)
bst.insert(2)
bst.print_tree()
# bst.height()