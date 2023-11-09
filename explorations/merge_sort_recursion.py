# def merge(arr, start, mid, end):
#     left_arr_size = (mid - start) + 1
#     right_arr_size = end - mid
#     left_arr = [0] * left_arr_size
#     right_arr = [0] * right_arr_size
#     for i in range(0, left_arr_size):
#         left_arr[i] = arr[start + i]
#     print(left_arr)
#     for i in range(0, right_arr_size):
#         right_arr[i] = arr[mid + 1 + i]
#     print(right_arr)
#     i = 0
#     j = 0
#     k = start
#
#     while i < left_arr_size and j < right_arr_size:
#         if left_arr[i] < right_arr[j]:
#             arr[k] = left_arr[i]
#             i += 1
#         else:
#             arr[k] = right_arr[j]
#             j += 1
#         k += 1
#     print(arr)
#     while i < left_arr_size:
#         arr[k] = left_arr[i]
#         k += 1
#         i += 1
#     print(arr)
#
#     while j < right_arr_size:
#         arr[k] = right_arr[j]
#         k += 1
#         j += 1
#     print(arr)
#     return arr
#
#
# def rec_merge_sort(arr, start, end):
#     if start < end:
#         mid = start + end // 2
#         rec_merge_sort(arr, start, mid)
#         rec_merge_sort(arr, mid + 1, end)
#         merge(arr, start, mid, end)

def merge_sort(Arr, start, end):
    if (start < end):
        mid = (start + end) // 2  # Computes floor of middle value
        merge_sort(Arr, start, mid)
        merge_sort(Arr, mid + 1, end)
        merge(Arr, start, mid, end)


def merge(Arr, start, mid, end):
    # temporary arrays to copy the elements of subarray
    leftArray_size = (mid - start) + 1
    rightArray_size = (end - mid)

    leftArray = [0] * leftArray_size
    rightArray = [0] * rightArray_size

    for i in range(0, leftArray_size):
        leftArray[i] = Arr[start + i]

    for i in range(0, rightArray_size):
        rightArray[i] = Arr[mid + 1 + i]

    i = 0
    j = 0
    k = start

    while (i < leftArray_size and j < rightArray_size):
        if (leftArray[i] < rightArray[j]):
            # filling the original array with the smaller element
            Arr[k] = leftArray[i]
            i = i + 1
        else:
            # filling the original array with the smaller element
            Arr[k] = rightArray[j]
            j = j + 1
        k = k + 1

    # copying remaining elements if any
    while (i < leftArray_size):
        Arr[k] = leftArray[i]
        k = k + 1
        i = i + 1

    while (j < rightArray_size):
        Arr[k] = rightArray[j]
        k = k + 1
        j = j + 1


Arr = [2, 14, 1, 9, 10, 5, 6, 18, 11]
merge_sort(Arr, 0, 8)
print(Arr)
