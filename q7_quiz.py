arr = [5, 4, 3, 2, 1]


def bubble_sort(a):
    for i in range(len(a), 0, -1):
        print(f"iter i: {i}")
        for j in range(0, i - 1):
            print(f"iter j: {j}")
            if a[j] > a[j + 1]:
                # print("yes")
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp
    return print(a)

bubble_sort(arr)
