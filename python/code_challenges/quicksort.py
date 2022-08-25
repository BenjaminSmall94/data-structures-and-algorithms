def quicksort(arr, left, right):
    if left < right:
        position = partition(arr, left, right)
        quicksort(arr, left, position - 1)
        quicksort(arr, position + 1, right)
    return arr


def partition(arr, left, right):
    pivot = arr[right]
    low = left
    for i in range(left, right):
        if arr[i] <= pivot:
            swap(arr, i, low)
            low += 1
    swap(arr, right, low)
    return low


def swap(arr, i, low):
    temp = arr[i]
    arr[i] = arr[low]
    arr[low] = temp


sorted_arr = quicksort([10, 9, 8, 7, 6, 5], 0, 5)
print(sorted_arr)
