def feedDog(hunger_level, biscuit_size):
    result = 0
    available = [True] * len(biscuit_size)

    for i in range(len(hunger_level)):
        available_biscuits = [j for j in biscuit_size if biscuit_size[j] >= hunger_level[i] and available[j]]
        min_biscuit = min(available_biscuits) if len(available_biscuits) > 0 else None
        # print(type(min_biscuit))
        # print(min_biscuit)
        if min_biscuit:
            result += 1
        for j in range(len(biscuits)):
            if biscuit_size[j] == min_biscuit:
                available[j] = False
                break

    return result

dogs = [2, 1]
biscuits = [1, 3, 2]

print(feedDog(dogs, biscuits))
