"""
stable algorithm : when a collection is sorted with a stable sorting algorithm,
items with the same sort keys preserve their order after the collection is sorted
"""
"""
algo mechanism:
The sorted part contains the first element of the array and other unsorted subpart contains the rest of the array. The first element in the unsorted array is compared to the sorted array so that we can place it into a proper sub-array.

It focuses on inserting the elements by moving all elements if the right-side value is smaller than the left side.

It will repeatedly happen until the all element is inserted at correct place
"""


def insertionSort(arr):
    for step in range(1, len(arr)):
        key = arr[step]
        j = step - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1

        arr[j + 1] = key


list = [9, 5, 1, 4, 3]
insertionSort(list)
print('Sorted Array :')
print(list)

#it is stable algorithm
#time complexity : best case O(n) and worst case(n^2)
#space complexity : O(1)