class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def printallnodes(self, node):
        if node == None:
            return

        self.printallnodes(node.left)
        print(node.value)
        self.printallnodes(node.right)

    def printlevel(self, node):
        q = []



if __name__ == '__main__':

    """ Construct below tree
               1
            /     \
           /       \
          2          3
         / \        / \
        4   5      6   7
       /          /     \
      11         8       9
    """

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.left.left = Node(11)
    root.right.left.left = Node(8)
    root.right.right.right = Node(9)
    b = BinaryTree()
    b.printallnodes(root)
