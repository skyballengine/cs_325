"""
Implement a function makechange_topdown( coins, amount). It should return the minimum number of coins needed to make change.

Example: makechange_topdown([1,3,5] , 9 ) should return 3
"""

import sys


def makechange_topdown_helper(coins, amount, countmemo=None):
    countmemo = [0] * (amount + 1)
    for coin in coins:
        temp_coincount = makechange_topdown_helper(coins, amount - coin, countmemo)
        minimum_coins = sys.maxsize
        if temp_coincount >= 0 and temp_coincount < minimum_coins:
            minimum_coins = 1 + temp_coincount
            