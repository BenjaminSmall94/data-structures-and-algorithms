def insert_shift_array(arr, val):
    if not arr:
        return [val]
    newArr = []
    for index, num in enumerate(arr):
        if index == (len(arr) + 1) // 2:
            newArr.append(val)
        newArr.append(num)
    print(newArr)
