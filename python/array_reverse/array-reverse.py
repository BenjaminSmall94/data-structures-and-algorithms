inputArray = [89, 2354, 3546, 23, 10, -923, 823, -12]

# Recursion
#
# outputArray = []
#
#
# def array_reverse(array, i):
#     if i < len(array):
#         array_reverse(array, i + 1)
#         outputArray.append(array[i])
#     if i == 0:
#         print(outputArray)


def array_reverse(array):
    outputArray = []
    for i in range(len(array), 0, -1):
        outputArray.append(array[i - 1])
    return outputArray


print(array_reverse(inputArray))
