def power_func(x, n):
    if n == 1:
        return x
    else:
        return x * power_func(x, n - 1)


result = power_func(2, 8)
print(result)
