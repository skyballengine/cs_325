def hanoi(n, start, end):
    if n == 1:
        print(f"{start} -> {end}")
    else:
        other = 6 - (start + end)
        hanoi(n - 1, start, other)
        print(f"{start} -> {end}")
        hanoi(n - 1, other, end)


hanoi(3, 1, 3)

'''
Implement function hanoi(n, source, temp, target)
returns source, temp, target


sample input: hanoi(5, [5,4,3,2,1], [], [])
output: [], [], [5, 4, 3, 2, 1]

Explanation: firstPeg is source, second Peg is temp, third peg is target. The discs got moved from source to target.
'''

def hanoi(n, source, temp, target):
    print(source, temp, target)
    if n > 0:
        # move n-1 disks from source to temp:
        hanoi(n - 1, source, target, temp)
        # move disk from source peg to target peg
        if source:
            target.append(source.pop())
            print(source, temp, target)
        # move n-1 disks from temp to target
        hanoi(n - 1, temp, source, target)


source = [3, 2, 1]
target = []
temp = []
hanoi(len(source), source, temp, target)