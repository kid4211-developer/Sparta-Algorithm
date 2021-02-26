finding_target = 18
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    endIndex = len(array) - 1
    startIndex = 0
    current_guess = (startIndex + endIndex) // 2
    while startIndex <= endIndex:
        if array[current_guess] == target:
            return True
        elif array[current_guess] < target:
            startIndex = current_guess + 1
        else:
            endIndex = current_guess - 1
        current_guess = (startIndex + endIndex) // 2
    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)