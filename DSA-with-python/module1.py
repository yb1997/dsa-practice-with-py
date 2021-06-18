def heapify(arr, arrLen, parentIndex):
    largestItemIndex = parentIndex
    leftChildIndex = (2 * parentIndex) + 1
    rightChildIndex = (2 * parentIndex) + 2

    if leftChildIndex < arrLen and arr[leftChildIndex] > arr[parentIndex]:
        largestItemIndex = leftChildIndex

    if rightChildIndex < arrLen and arr[rightChildIndex] > arr[largestItemIndex]:
        largestItemIndex = rightChildIndex

    if largestItemIndex != parentIndex:
        arr[largestItemIndex], arr[parentIndex] = arr[parentIndex], arr[largestItemIndex]
        heapify(arr, arrLen, largestItemIndex)

def insert(arr, item):
    arr.append(item)

    if len(arr) > 1:
        i = len(arr) - 1
        while i > 0:
            parentIndex = i // 2
            if arr[parentIndex] < arr[i]:
                arr[parentIndex], arr[i] = arr[i], arr[parentIndex]
            i = parentIndex



def remove(arr = [], item = None):
    removeIndex = arr.index(item)

    for i in range((len(arr)//2) - 1, -1, -1): # start from last non-leaf node and keep heapifying till root node
        heapify(arr, arrLen, i)

def buildHeap(arr, arrLen):
    for i in range((arrLen//2) - 1, -1, -1):
        heapify(arr, arrLen, i)

testArr = [1, 2, 3, 4, 5, 6, 7]

#expected -> [7, 5, 6, 4, 2, 1, 3]

buildHeap(testArr, len(testArr))
print(testArr)

