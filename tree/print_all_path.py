from collections import deque

# Data structure to store a Binary Tree node
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# Function to check if given node is a leaf node or not
# def isLeaf(node):
#     return node.left is None and node.right is None
#

def pathsum(root):
    path = []
    result = []
    pathsum = 18
    all_path(root, path, result, pathsum, path_sum=0)
    return result

def all_path(root, path, result, pathsum, path_sum):
    if root is None:
        return
    path_sum = root.data + path_sum
    if root.left is None and root.right is None and path_sum == pathsum:
        result.append([*path, root.data])

    path.append(root.data)
    all_path(root.left, path, result, pathsum, path_sum)
    all_path(root.right, path, result, pathsum, path_sum)
    path_sum = path_sum - root.data
    path.pop()


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
    # root.left.right.right = Node(10)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.left.left = Node(11)
    root.right.left.left = Node(8)
    root.right.right.right = Node(9)

    # print all root to leaf paths
    # print(pathsum(root,18))
    # print(all_path(root,[],[]))
    print(pathsum(root))