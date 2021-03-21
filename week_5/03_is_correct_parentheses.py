# 괄호 짝 검증 코드 : 3주차 homework - 2 참조
from collections import deque
balanced_parentheses_string = "()))((()"


def is_correct_parentheses(string):  # 올바른 괄호인지 확인
    stack = []
    for s in string:
        if s == '(':
            stack.append(s)
        elif stack:
            stack.pop()
    return len(stack) == 0


# 2. 입력된 문자열을 '균형잡힌 괄호 문자열' u / v 로 분리함
# 단, u는 '균형잡힌 괄호 문자열' 더 이상 분리할 수 없어야 하고, v는 빈 문자열이 될 수 있음
def separate_to_u_v(string):
    queue = deque(string)
    left, right = 0, 0
    u, v = "", ""
    while queue:
        char = queue.popleft()
        u += char
        if char == '(':
            left += 1
        else:
            right += 1
        if left == right:
            break
    v = ''.join(list(queue))
    return u, v


def reverse_parenthesis(string):
    reversed_string = ""
    for char in string:
        if char == '(':
            reversed_string += ')'
        else:
            reversed_string += '('
    return reversed_string


# 균형작입 괄호 문자열 : '(' 와 ')'의 개수가 같다
def change_to_correct_parenthesis(string):
    # 1. 입력이 빈 문자열인 경우, 빈 문자열 반환
    if string == "":
        return ""

    # 2. 입력된 문자열을 '균형잡힌 괄호 문자열' u / v 로 분리함
    u, v = separate_to_u_v(string)

    # 3. 문자열 u가 '올바른 괄호 문자열'이라면 문자열 v에 대해 1단계부터 다시 수행함
    # 3-1. 수행한 결과는 u에 이어붙인다.
    if is_correct_parentheses(u):
        return u + change_to_correct_parenthesis(v)
    # 4. 문자열 u가 올바른 괄호 문자열이 아니라면 아래과정을 수행함
    else:
        return "(" + change_to_correct_parenthesis(v) + ")" + reverse_parenthesis(u[1: -1])


def get_correct_parentheses(balanced_parentheses_string):
    if is_correct_parentheses(balanced_parentheses_string):
        return balanced_parentheses_string
    else:  # 균형잡힌 문자열인 경우
        return change_to_correct_parenthesis(balanced_parentheses_string)


print(get_correct_parentheses(balanced_parentheses_string))  # "()(())()"가 반환 되어야 합니다!
