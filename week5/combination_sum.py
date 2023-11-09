'''
Implement a function combination_sum([2,3,6,7], 7 )

Example: combination_sum([2,3,6,7], 7 ) should print [[2, 2, 3], [7]]
'''
from copy import deepcopy


def combination_sum(nums, total):
    def combination_sum_helper(nums, start, results, remainder, curr_combo):
        if remainder == 0:
            results.append(deepcopy(curr_combo))
            return

        elif remainder < 0:
            return

        else:
            for i in range(start, len(nums)):
                curr_combo.append(nums[i])
                combination_sum_helper(nums, i, results, remainder - nums[i], curr_combo)
                curr_combo.pop()

    results = []
    combination_sum_helper(nums, 0, results, total, [])
    return results


print(combination_sum([2, 3, 6], 7))
