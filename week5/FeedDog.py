def feedDog(hunger_level, biscuit_size):
    hunger_level_ls = list(hunger_level)
    result = 0
    available = [True] * len(biscuit_size)

    for i in range(len(hunger_level_ls)):
        available_biscuits = []
        for j in range(len(biscuit_size)):
            if biscuit_size[j] >= hunger_level_ls[i] and available[j]:
                available_biscuits.append(biscuit_size[j])
        if len(available_biscuits) > 0:
            min_biscuit = min(available_biscuits)
        else:
            min_biscuit = None
        # print(type(min_biscuit))
        # print(min_biscuit)
        if min_biscuit:
            result += 1
        for k in range(len(biscuit_size)):
            if biscuit_size[k] == min_biscuit:
                available[k] = False
                break

    return result


# hunger_level = [2, 11, 5, 15, 12, 27]
# biscuit_size = [29, 1, 5, 3, 14, 10, 2]
#
# print(feedDog(hunger_level, biscuit_size))
#
# dogs = [2, 1]
# biscuits = {1, 3, 2}
#
# print(feedDog(dogs, list(biscuits)))
#
# dogs = [1, 2, 3]
# biscuits = [1, 1]
#
# print(feedDog(dogs, biscuits))
#
# dogs = [2, 1]
# biscuits = [1, 3, 2]
#
# print(feedDog(dogs, biscuits))
