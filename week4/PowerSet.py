# powerset function
from copy import deepcopy
# from showcallstack import showcallstack


# ls = [1, 2, 3]

def powerset(inputSet):
    result = []
    powerset_helper(len(inputSet) - 1, [], inputSet, result)
    return result


def powerset_helper(pointer, choices_made, input, result):
    # base case
    # showcallstack()
    if pointer < 0:
        result.append(deepcopy(choices_made))
        return

    # add element to choices_made
    choices_made.append(input[pointer])

    powerset_helper(pointer - 1, choices_made, input, result)

    choices_made.pop()

    powerset_helper(pointer - 1, choices_made, input, result)

# print(powerset(ls))
