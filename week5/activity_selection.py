def activity_selection(act, start, end):
    result = [end[0]]
    acts = [act[0]]
    i = 1
    j = 0
    while result[-1] < end[-1]:
        if start[i] >= end[j]:
            result.append(end[i])
            acts.append(act[i])
            j += 1
        i += 1
    return len(result), acts


activities = ['Golf', 'Paint', 'Cook', 'Sleep', 'Jog', 'Write Code', 'Eat']

start_times = [1, 3, 1, 3, 4, 6, 8]

end_times = [3, 4, 4, 6, 6, 9, 9]

print(activity_selection(activities, start_times, end_times))
