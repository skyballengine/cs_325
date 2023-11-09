def peasant_mult(a, b):
    if a == 0:
        return 0
    a_p = a // 2
    b_p = b + b
    prod = peasant_mult(a_p, b_p)
    if a % 2 == 1:
        prod += b
    return prod


x = peasant_mult(5, 6)
print(x)
