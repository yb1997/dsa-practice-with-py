
# Max-Heap data structure in Python

def heapify(arr, arraySize, parentIndex):
    largestNodeIndex = parentIndex
    leftChildIndex = 2 * parentIndex + 1
    rightChildIndex = 2 * parentIndex + 2 
    
    if leftChildIndex < arraySize and arr[parentIndex] < arr[leftChildIndex]:
        largestNodeIndex = leftChildIndex
    
    if rightChildIndex < arraySize and arr[largestNodeIndex] < arr[rightChildIndex]:
        largestNodeIndex = rightChildIndex
    
    if largestNodeIndex != parentIndex:
        arr[parentIndex],arr[largestNodeIndex] = arr[largestNodeIndex],arr[parentIndex]
        heapify(arr, arraySize, largestNodeIndex)

def insert(array, newNum):
    size = len(array)
    if size == 0:
        array.append(newNum)
    else:
        array.append(newNum);
        for i in range((size//2)-1, -1, -1):
            heapify(array, size, i)

def deleteNode(array, num):
    size = len(array)
    i = 0
    for i in range(0, size):
        if num == array[i]:
            break
        
    array[i], array[size-1] = array[size-1], array[i]

    array.remove(num)
    
    for i in range((len(array)//2)-1, -1, -1):
        heapify(array, len(array), i)
    
arr = []


insert(arr, 3)
insert(arr, 4)
insert(arr, 9)
insert(arr, 5)
insert(arr, 2)

print ("Max-Heap array: " + str(arr))

deleteNode(arr, 4)
print("After deleting an element: " + str(arr))



def buildMaxHeap(arr):
    size = len(arr)
    for i in range((size//2) - 1, -1, -1): # start from last non-leaf node and keep heapifying till root node
        heapify(arr, size, i)

testData = [1, 2, 3, 4, 5, 6, 7]

#expected -> [7, 5, 6, 4, 2, 1, 3]

buildMaxHeap(testData)




