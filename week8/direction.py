def get_direction(current, previous):
    x = current[0] - previous[0]
    y = current[1] - previous[1]
    coordinate = (x, y)
    match coordinate:
        case (0, 1):
            return 'R'
        case (0, -1):
            return 'L'
        case (1, 0):
            return 'D'
        case (-1, 0):
            return 'U'


print(get_direction((2, 1), (2, 0)))