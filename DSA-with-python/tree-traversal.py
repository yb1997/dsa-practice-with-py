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

class TraverseTree:
    @staticmethod
    def inorder(node, func):
        if node is None:
            return
        TraverseTree.inorder(node.left, func)
        func(node.data)
        TraverseTree.inorder(node.right, func)

    @staticmethod
    def preorder(node, func):
        if node is None:
            return
        func(node.data)
        TraverseTree.preorder(node.left, func)
        TraverseTree.preorder(node.right, func)
    
    @staticmethod
    def postorder(node, func):
        if node is None:
            return
        TraverseTree.postorder(node.left, func)
        TraverseTree.postorder(node.right, func)
        func(node.data)

    @staticmethod
    def breadth_first(node, func):
        queue = deque([node]) # deque is more efficient than list for implementing a queue, ref: https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-queues
        while len(queue) > 0:
            curr = queue.popleft()
            func(curr.data)
            if curr.left is not None: queue.append(curr.left)
            if curr.right is not None: queue.append(curr.right)

class Utility:
    @staticmethod
    def create_tree():
        left = Node(1)
        right = Node(3)
        root = Node(2, left, right)

        left.left = Node(5)
        left.right = Node(7)

        right.left = Node(9)
        right.right = Node(10)

        return root

    @staticmethod
    def perform(func):
        func(root, printer.collect)
        printer.print()
        printer.reset()


root = Utility.create_tree()
printer = TreeOutputPrinter()

print("inorder traversal")
# left -> root -> right
Utility.perform(TraverseTree.inorder)


print("preorder traversal")
# root -> left -> right
Utility.perform(TraverseTree.preorder)


print("postorder traversal")
# left -> right -> root
Utility.perform(TraverseTree.postorder)


print("breadth first traverse")
Utility.perform(TraverseTree.breadth_first)


def heapify(arr, arrLen, parentIndex):
    largestItemIndex = parentIndex
    leftChildIndex = (2 * parentIndex) + 1
    rightChildIndex = (2 * parentIndex) + 2

    if leftChildIndex < arrLen and arr[leftChildIndex] > arr[parentIndex]:
        arr[parentIndex], arr[leftChildIndex] = arr[leftChildIndex], arr[parentIndex]
        largestItemIndex = leftChildIndex

    if rightChildIndex < arrLen and arr[rightChildIndex] > arr[largestItemIndex]:
        largestItemIndex = rightChildIndex

    if largestItemIndex != parentIndex:
        arr[largestItemIndex], arr[parentIndex] = arr[parentIndex], arr[largestItemIndex]
        heapify(arr, arrLen, largestItemIndex)

def insert(arr, arrLen, item):
    arr.append(item)

    for i in range((arrLen//2) - 1, -1, -1):
        heapify(arr, arrLen, i)

def remove(arr, arrLen, item):
    pass

def buildHeap(arr, arrLen):
    for i in range((arrLen//2) - 1, -1, -1):
        heapify(arr, arrLen, i)

testArr = [1, 2, 3, 4, 5, 6, 7]

#expected -> [7, 5, 6, 4, 2, 1, 3]

buildHeap(testArr, len(testArr))
print(testArr)













