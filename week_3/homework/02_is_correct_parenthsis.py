s = "(())(())"


def is_correct_parenthesis(string):
    open_parentheses = 0
    close_parentheses = 0
    for parentheses in string:
        if parentheses == "(":
            open_parentheses += 1
        else:
            close_parentheses += 1
            if open_parentheses < close_parentheses:
                return False
    if open_parentheses != close_parentheses:
        return False
    return True


print(is_correct_parenthesis(s))