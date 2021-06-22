"""
Time complexity: O(n**2)
Space complexity: O(1)
"""

def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_item_index = i
        for j in range(i + 1, len(arr)):
            if arr[min_item_index] > arr[j]:
                min_item_index = j
        arr[i], arr[min_item_index] = arr[min_item_index], arr[i]


"""
Time complexity: O(n**2)
Space complexity: O(1)
"""

def bubble_sort(arr):
    size = len(arr)
    for j in range(size - 1):
        is_swapped = False
        for i in range(size - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_swapped = True
        if not is_swapped:
            break

"""
its like sorting playing cards, compare current card on your right hand(unsorted cards) with each card on the left hand side(sorted cards are on left) and keep moving the sorted cards
on the right side as long as they are greater than current card

insertion and selection are kinda same, one iterates to the left side(insertion) and the other one to the right side(selection) in inner loop

Time complexity: O(n**2)
Space complexity: O(1)
"""

def insertion_sort(arr):
    for i in range(1, len(arr)):
        curr_val = arr[i]
        j = i - 1
        while j >= 0 and curr_val < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = curr_val



"""
Time complexity: O(nlog(n))
Space complexity: O(n)
"""

def merge_sort(arr):
    def merge(arr, start, mid, end):
        i = j = 0
        k = start
        leftArr = arr[start:mid]
        rightArr = arr[mid:end]

        while i < len(leftArr) and j < len(rightArr):
            if leftArr[i] <= rightArr[j]:
                arr[k] = leftArr[i]
                i += 1
            else:
                arr[k] = rightArr[j]
                j += 1
            k += 1

        while i < len(leftArr):
            arr[k] = leftArr[i]
            i += 1
            k += 1
        
        while j < len(rightArr):
            arr[k] = rightArr[j]
            j += 1
            k += 1


    def merge_sort_core(arr, start, end):
        if  end - start > 1:
            mid = start + ((end - start)//2)
            merge_sort_core(arr, start, mid)
            merge_sort_core(arr, mid, end)
            merge(arr, start, mid, end)

    merge_sort_core(arr, 0, len(arr))

def quick_sort(arr):
    pass

def heap_sort(arr):
    pass
