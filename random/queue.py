class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequque(self):
        if len(self.items) != 0:
            return self.items.pop()


q = Queue()
q.enqueue('1')
q.enqueue('1')
q.enqueue('3')
q.enqueue('20')
q.enqueue('34')
print(q.items)
q.dequque()
print(q.items)
q.enqueue('50')
q.enqueue('55')
print(q.items)
print(q.dequque())
print(q.items)
print(q.dequque())
print(q.items)
print(q.dequque())
print(q.items)
print(q.dequque())
print(q.items)
print(q.dequque())
print(q.items)
print(q.dequque())
print(q.items)
print(q.dequque())
print(q.items)
q.enqueue('34')
print(q.items)
q.enqueue('24')
print(q.items)
