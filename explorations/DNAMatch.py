# Given two DNA strings find the length of the longest common string alignment between
# them (it need not be continuous). Assume empty string does not match with anything.
# Example: DNA string1: ATAGTTCCGTCAAA ; DNA string2: GTGTTCCCGTCAAA


def dna_match_topdown(DNA1, DNA2):
    n = len(DNA1)
    m = len(DNA2)
    arr_2d = [[-1 for x in range(m+1)] for y in range(n+1)]
    return dna_match_topdown_helper(DNA1, DNA2, n, m, arr_2d)

def dna_match_topdown_helper(DNA1, DNA2, n, m, arr_2d):
    # base cases
    if n == 0 or m == 0:
        return 0
    # if entry exists
    if arr_2d[n][m] != -1:
        return arr_2d[n][m]
    # if match add 1 to table
    if DNA1[n-1] == DNA2[m-1]:
        arr_2d[n][m] = 1 + dna_match_topdown_helper(DNA1, DNA2, n-1, m-1, arr_2d)
        return arr_2d[n][m]
    else:
        arr_2d[n][m] = max(dna_match_topdown_helper(DNA1, DNA2, n-1, m, arr_2d), dna_match_topdown_helper(DNA1, DNA2, n, m-1, arr_2d))
        return arr_2d[n][m]

def dna_match_bottomup(DNA1, DNA2):
    len_1 = len(DNA1)
    len_2 = len(DNA2)

    arr_2d = [[0 for x in range(len_2 + 1)] for y in range(len_1 + 1)]

    for i in range(len_1 + 1):
        for j in range(len_2 + 1):
            if i == 0 or j == 0:
                arr_2d[i][j] = 0
            elif DNA1[i - 1] == DNA2[j - 1]:
                arr_2d[i][j] = arr_2d[i - 1][j - 1] + 1
            else:
                arr_2d[i][j] = max(arr_2d[i - 1][j], arr_2d[i][j - 1])
    return arr_2d[len_1][len_2]

print(dna_match_bottomup("TAGTTCCGTCAAA", "GTGTTCCCGTCAAA"))
print(dna_match_topdown("TAGTTCCGTCAAA", "GTGTTCCCGTCAAA"))
