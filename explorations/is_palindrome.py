def is_palindrome(str):
    ori_str = str.replace(" ", "").lower()
    # print(ori_str)
    if len(ori_str) <= 2:
        return True
    else:
        if ori_str[0] == ori_str[-1]:
            new_str = ori_str[1:-1]
            return is_palindrome(new_str)
    return False


print(is_palindrome("racecar"))
print(is_palindrome("Do geese see God"))
print(is_palindrome("williw"))
