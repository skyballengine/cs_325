'''
Implement a function lcs_BF(str1, str2)

Sample input & output: lcs_BF("abcde", "ac") should return 2
'''


def long_poss_subseq_brute_for(str1, str2):
    if len(str1) == 0 or len(str2) == 0:
        return 0
    else:
        if str1[0] == str2[0]:
            return 1 + long_poss_subseq_brute_for(str1[1:], str2[1:])
        else:
            return max(long_poss_subseq_brute_for(str1[1:], str2), long_poss_subseq_brute_for(str1, str2[1:]))


print(long_poss_subseq_brute_for("abcdeasdfgasdi", "acsdfgasdf"))
