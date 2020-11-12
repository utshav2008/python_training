class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root, "")
        elif traversal_type == "levelorder":
            return self.levelorder_print(tree.root)

        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False

    def preorder_print(self, start, traversal):
        """Root->Left->Right"""
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        """Left->Root->Right"""
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        """Left->Right->Root"""
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal = self.inorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal

    # def levelorder_print(self, start):
    #     if start is None:
    #         return
    #
    #     queue = Queue()
    #     queue.enqueue(start)
    #
    #
    #     # traversal =
    #     while len(queue) > 0:
    #         print(str(queue.peek()))
    #
    #         node = queue.dequeue()
    #
    #         if node.left:
    #             queue.enqueue(node.left)
    #         if node.right:
    #             queue.enqueue(node.right)

    # def levelorder_print(self, start):
    #
    #     if start is None:
    #         return
    #
    #     queue_ = []
    #     queue_.insert(0,start)
    #     final = []
    #     while len(queue_) > 0:
    #         node = queue_.pop()
    #         final.append(node.value)
    #         if node.left:
    #             queue_.insert(0,node.left)
    #         if node.right:
    #             queue_.insert(0,node.right)
    #     return final
    # def levelorder_print(self, start):
    #     if start == None:
    #         return
    #     q = []
    #     q.insert(0, start)
    #     ret_list = []
    #     while len(q) > 0:
    #         temp = []
    #         N = len(q)
    #         while N>0:
    #             cur = q.pop()
    #             temp.append(cur.value)
    #             if cur.left:
    #                 q.insert(0,cur.left)
    #             if cur.right:
    #                 q.insert(0,cur.right)
    #             N -= 1
    #         avg = sum(temp)/len(temp)
    #         ret_list.append(avg)
    #     return ret_list
    def levelorder_print(self, start):
        if start == None:
            return
        q = []
        q.insert(0,start)
        while len(q) > 0:
            temp = []
            n = len(q)
            while n>0:
                node = q.pop()
                temp.append(node.value)
                if node.left:
                    q.insert(0,node.left)
                if node.right:
                    q.insert(0,node.right)
                n -= 1
            temp

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(32)
print(tree.levelorder_print(tree.root))
# print(tree.print_tree("levelorder"))
