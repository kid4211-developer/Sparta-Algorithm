finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]


def is_exist_target_number_binary(target, numbers):
    # 이진 탐색은 일정한 규칙으로 정렬되어 있는 데이터을 가지고 실행 가능 ( 배열.sort() )
    checkArray = sorted(numbers)
    endIndex = len(checkArray) - 1
    startIndex = 0
    current_guess = (startIndex + endIndex) // 2
    while startIndex <= endIndex:
        if checkArray[current_guess] == target:
            return True
        elif checkArray[current_guess] < target:
            startIndex = current_guess + 1
        else:
            endIndex = current_guess - 1
        current_guess = (startIndex + endIndex) // 2
    return False


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)