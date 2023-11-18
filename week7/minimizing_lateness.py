"""
Implement a function min_Lateness(assignments)

Sample value for assignments = [("A",2,2),("B",3,4),("C",1,6),("D",5,7)]
where A, B, C, D are name of assignments
2,3,1,5 represent time timetaken by the assignment
2,4,6,7 represent deadline

Example:
assignments = [("A",2,2),("B",3,4),("C",1,6),("D",5,7)]
(min_Lateness(assignments))

would return

(4, ['A', 'B', 'C', 'D'])

4 is the maximum min_Lateness
"""
# use itemgetter to sort by a specific index of a list
# in this case, we're sorting the list by the 2nd index of each element tuple which is the deadline for the assignment
from operator import itemgetter


def min_lateness(assignments):
    sorted_assignments = sorted(assignments, key=itemgetter(2))
    start_time = 0
    max_lateness = 0
    schedule = []
    finish_time = 0

    # for i in range(0, len(assignments)):
    #     finish_time = start_time + sorted_assignments[i][1]
    #     if finish_time > sorted_assignments[i][2]:
    #         max_lateness = max(max_lateness, (finish_time - sorted_assignments[i][2]))
    #     start_time = finish_time
    #     schedule.append(sorted_assignments[i][0])
    #
    # return max_lateness, schedule

    for i in range(0, len(assignments)):
        finish_time = sorted_assignments[i][2]
        start_time += sorted_assignments[i][1]
        schedule.append(sorted_assignments[i][0])

        if start_time > finish_time:
            max_lateness = (start_time - finish_time)

    return max_lateness, schedule


ass = [("A", 2, 2), ("B", 3, 4), ("C", 1, 6), ("D", 5, 7)]
print(min_lateness(ass))
