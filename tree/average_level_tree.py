from collections import deque

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    # def average(self, root):
    #     res = []
    #     q = deque()
    #     q.appendleft(root)
    #     while len(q):
    #         a = []
    #         size = len(q)
    #         while size != 0:
    #             cur = q.pop()
    #             a.append(cur.value)
    #             if cur.left:
    #                 q.appendleft(cur.left)
    #             if cur.right:
    #                 q.appendleft(cur.right)
    #             size -= 1
    #         avg = sum(a)/len(a)
    #         res.append(avg)
    #     return res

    def average(self, root):

        q = []
        result = []
        q.insert(0,root)
        while len(q) > 0:

            N =  len(q)
            temp = []
            for i in range(N):
                node = q.pop()
                temp.append(node.value)
                if node.left:
                    q.insert(0,node.left)
                if node.right:
                    q.insert(0,node.right)
            result.append(temp)
        print(result)


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(10)
tree.root.right.right = Node(6)
tree.average(tree.root)


