def foo(arr, start, end):
    if start < end:
        middle = (start + end) // 2
        foo(arr, start, middle)
        foo(arr, middle + 1, end)
    else:

        arr[start] = 2 * arr[start]


foo([1, 2, 3, 4, 5], 0, 4)