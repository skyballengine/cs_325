# nums = [7, 2, 5, 8, 6]

# def mis_helper(nums, i, ls, max_sum):
#     if i <= 0:
#         return 0
#     # ls.append(nums[i])
#
#     max_sum = nums[i] + mis_helper(nums, i - 2, ls)
#     return ls
#
#
# def mis(nums):
#     i = len(nums)
#     new_ls = []
#     max_sum = 0
#     return mis_helper(nums, i, new_ls, max_sum)
#
# print(mis([7, 2, 5, 8, 6]))

def max_independent_set(nums):
    result = []
    memo = {-2: 0, -1: 0}
    n = len(nums)
    chosen = [True] * n

    for i in range(n):
        memo[i] = max(memo[i - 1], nums[i] + memo[i - 2])

        if memo[i] == memo[i - 1]:
            chosen[i] = False

    j = n - 1
    while j >= 0:
        if chosen[j]:
            result.append(nums[j])
            j -= 1
        j -= 1

    return result


print(max_independent_set([7, 2110, 5, 8, 6, 3, 6, 8, 10]))
