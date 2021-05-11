from collections import deque


class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

class TreeOutputPrinter:
    output = []
    def collect(self, data):
        self.output.append(str(data))
    def print(self):
        print(",".join(self.output))
    def reset(self):
        self.output.clear()

def inorder_traverse(node, func):
    if node is None:
        return
    inorder_traverse(node.left, func)
    func(node.data)
    inorder_traverse(node.right, func)

def preorder_traverse(node, func):
    if node is None:
        return
    func(node.data)
    preorder_traverse(node.left, func)
    preorder_traverse(node.right, func)

def postorder_traverse(node, func):
    if node is None:
        return
    postorder_traverse(node.left, func)
    postorder_traverse(node.right, func)
    func(node.data)

def breadth_first_traverse(node, func):
    queue = deque([node]) # deque is more efficient than list for implementing a queue, ref: https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-queues
    while len(queue) > 0:
        curr = queue.popleft()
        func(curr.data)
        if curr.left is not None: queue.append(curr.left)
        if curr.right is not None: queue.append(curr.right)

def create_tree():
    left = Node(1)
    right = Node(3)
    root = Node(2, left, right)

    left.left = Node(5)
    left.right = Node(7)

    right.left = Node(9)
    right.right = Node(10)

    return root

def perform(func):
    func(root, printer.collect)
    printer.print()
    printer.reset()

root = create_tree()
printer = TreeOutputPrinter()

print("inorder traversal")
# left -> root -> right
perform(inorder_traverse)


print("preorder traversal")
# root -> left -> right
perform(preorder_traverse)


print("postorder traversal")
# left -> right -> root
perform(postorder_traverse)


print("breadth first traverse")
perform(breadth_first_traverse)






