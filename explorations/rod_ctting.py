

'''
recursive solution Time complexity - O(2^n)
source: https://www.educative.io/courses/dynamic-programming-in-python/xoG0Lmq84yn
'''
"""Given a rod of n meters and a list of prices (price[]) for different lengths of the rod, a rod of length i will 
have a price of price[i-1]. We want to sell the rod and make the maximum possible revenue. We can cut the rod into 
lengths of different sizes before selling. The price of each piece will be determined by the list of prices provided. 
What is the optimal amount of revenue we can get out of the rod given length, n and prices?"""

def rod_cutting_naive(n, prices):
    if n == 0:
        return 0
    max_val = 0
    for i in range(1, n+1):
        temp = prices[i-1] + rod_cutting_naive(n - i, prices)
        if temp > max_val:
            max_val = temp
    return max_val


print(rod_cutting_naive(4, [1, 5, 8, 9, 10]))

