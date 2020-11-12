# Data structure to store a Binary Tree node
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def printnodes(node):
    path = []
    nodes(node, path)
    print(path)

def nodes(node, path):
    if node is None:
        return

    if node.right is None and node.left is None:
        path.append(node.data)
    # nodes(node.right,path)
    # path.append(node.data)
    nodes(node.right, path)
    nodes(node.left, path)



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
    printnodes(root)