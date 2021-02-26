input = "accba"


def is_palindrome(string):
    startIndex = 0
    endIndex = len(string) - 1
    while endIndex >= startIndex:
        print(string[startIndex], string[endIndex])
        if string[startIndex] == string[endIndex]:
            startIndex = startIndex + 1
            endIndex = endIndex - 1
        else:
            return False
    return True


print(is_palindrome(input))