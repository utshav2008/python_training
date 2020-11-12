class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def isLeaf(node):
    return node.left is None and node.right is None

def printLeafToRootPaths(node, path):

    # base case
    if node is None:
        return

    # include current node to path list
    path.append(node.data)

    # if leaf node is found, print the path present in the list
    # in reverse order (leaf to root node)
    if isLeaf(node):
        print(path)

    # recur for left and right subtree
    printLeafToRootPaths(node.left, path)
    printLeafToRootPaths(node.right, path)

    # remove current node after left and right subtree are done
    path.pop()

def findLeafToRootPaths(node):

    # Deque to store left to root path
    path = []

    # call recursive function
    printLeafToRootPaths(node, path)



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
    findLeafToRootPaths(root)