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

def printpath(node):
    path = []
    result = []
    all_path(root, path, result)
    return result

def all_path(node, path, result):
    if node is None:
        return

    if node.left is None and node.right is None:
        result.append([*path, node.data])

    path.append(node.data)
    all_path(node.left,path,result)
    all_path(node.right,path,result)
    path.pop()

def pathsum(node,sum):
    path = []
    result = []
    path_sum = 0
    dfs(node,path,result,path_sum,sum)
    return result

def dfs(node,path,result,path_sum,sum):
    if node is None:
        return

    path_sum = path_sum + node.data
    if node.left is None and node.right is None and path_sum == sum:
        result.append([*path, node.data])

    path.append(node.data)
    dfs(node.left, path, result, path_sum, sum)
    dfs(node.right, path, result, path_sum, sum)
    path_sum = path_sum - node.data
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
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.left.left = Node(11)
    root.right.left.left = Node(8)
    root.right.right.right = Node(9)
    # print(printpath(root))
    print(pathsum(root, 18))