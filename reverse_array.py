arr = [1, 2, 3, 4, 5, 6, 7, 8]


def reverse_array(ls):
    n = len(ls)
    i = (n - 1) // 2
    j = n // 2
    while i >= 0 and j <= (n - 1):
        temp = ls[i]
        ls[i] = ls[j]
        ls[j] = temp
        i -= 1
        j += 1
        print(ls)
    return ls


reverse_array(arr)
