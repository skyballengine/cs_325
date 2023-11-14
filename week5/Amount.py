from copy import deepcopy


def amount(A, S):
    def amount_helper(nums, start, results_list, remainder, curr_combo, chosen_list):
        if remainder == 0:
            results_list.append(deepcopy(curr_combo))
            chosen_list = [False] * len(A)
            return

        elif remainder < 0:
            # chosen_index -= 1
            # return chosen_index
            return

        else:
            for i in range(start, len(nums)):
                if not chosen_list[i]:
                    curr_combo.append(nums[i])
                    chosen_list[i] = True
                    amount_helper(nums, i, results_list, remainder - nums[i], curr_combo, chosen_list)
                    curr_combo.pop()
                    chosen_list[i] = False



    # outer function scope variables
    results = []
    chosen = [False] * len(A)
    amount_helper(A, 0, results, S, [], chosen)


    final_results = []
    for j in results:
        j.sort()
        if j not in final_results:
            final_results.append(j)

    return final_results


# nums_list = [11, 1, 3, 2, 6, 1, 5]
# target = 8
# answer = [[3, 5], [2, 6], [1, 2, 5], [1, 1, 6]]
#
# print(amount(nums_list, target))
