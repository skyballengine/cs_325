def kthElement(arr1, arr2, k):
    # temporary arrays to copy the elements of subarray
    left_array_size = len(arr1)
    right_array_size = len(arr2)
    new_arr = [0] * (right_array_size + left_array_size)

    i = 0
    j = 0
    x = 0

    while i < left_array_size and j < right_array_size:
        if arr1[i] < arr2[j]:
            # filling the original array with the smaller element
            new_arr[x] = arr1[i]
            i = i + 1
        else:
            # filling the original array with the smaller element
            new_arr[x] = arr2[j]
            j = j + 1
        x = x + 1

    # copying remaining elements if any
    while i < left_array_size:
        new_arr[x] = arr1[i]
        x = x + 1
        i = i + 1

    while j < right_array_size:
        new_arr[x] = arr2[j]
        x = x + 1
        j = j + 1

    return new_arr[k - 1]


