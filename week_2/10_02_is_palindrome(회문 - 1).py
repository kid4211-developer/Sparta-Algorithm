input = "abcba"


def is_palindrome(string):
    startIndex = 0
    endIndex = len(string) -1
    if string[startIndex] != string[endIndex]:
        return False
    if startIndex == endIndex:
        return True
    return is_palindrome(string[startIndex + 1: endIndex])


print(is_palindrome(input))