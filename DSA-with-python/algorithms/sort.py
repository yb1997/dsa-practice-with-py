"""
Time complexity: O(n**2)
Space complexity: O(1)
"""

def selection_sort(list):
    for i in range(len(list) - 1):
        min_item_index = i
        for j in range(i + 1, len(list)):
            if list[min_item_index] > list[j]:
                min_item_index = j
        list[i], list[min_item_index] = list[min_item_index], list[i]


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

def insertion_sort(list):
    for i in range(1, len(list)):
        curr_val = list[i]
        j = i - 1
        while j >= 0 and curr_val < list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = curr_val

def merge_sort(list):
    pass

def quick_sort(list):
    pass

def heap_sort(list):
    pass
