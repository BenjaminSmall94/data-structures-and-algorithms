def array_binary_search(arr, val):
    min_index = 0
    max_index = len(arr) - 1
    while max_index >= min_index:
        search_index = (max_index + min_index) // 2
        print(min_index, search_index, max_index)
        if arr[search_index] == val:
            return search_index
        elif arr[search_index] < val:
            min_index = search_index + 1
        else:
            max_index = search_index - 1
    return -1
