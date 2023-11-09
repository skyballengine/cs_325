def merge_sort(arr, start, end):
    print(arr)
    mid = len(arr) // 2
    print(f"Mid: {mid}")
    # temp arrays a and b
    left_arr_size = mid - start
    print(left_arr_size)
    right_arr_size = end - mid + 1
    print(right_arr_size)
    left_arr = [0] * left_arr_size
    right_arr = [0] * right_arr_size

    for i in range(0, left_arr_size):
        left_arr[i] = arr[start + i]
    print(left_arr)
    for i in range(0, right_arr_size):
        right_arr[i] = arr[mid + i]
    print(right_arr)
    i = 0
    j = 0
    k = start

    while i < left_arr_size and j < right_arr_size:
        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    print(arr)
    while i < left_arr_size:
        arr[k] = left_arr[i]
        k += 1
        i += 1
    print(arr)

    while j < right_arr_size:
        arr[k] = right_arr[j]
        k += 1
        j += 1
    print(arr)
    return arr


print(merge_sort([2, 10, 11, 1, 13, 5], 0, 5))
