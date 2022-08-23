def merge_sort(arr):
    size = len(arr)

    if size > 1:
        mid = size // 2
        left = arr[0:mid]
        right = arr[mid:size]
        left = merge_sort(left)
        right = merge_sort(right)
        merge(left, right, arr)
    return arr


def merge(left, right, arr):
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
    return arr
