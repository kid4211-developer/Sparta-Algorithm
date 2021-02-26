

finding_target = 18
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    endIndex = len(array)
    startIndex = 0
    funcResult = False
    for index in array:
        checkIndex = (endIndex + startIndex) // 2
        print("checkIndex :", checkIndex)
        if array[checkIndex] == target:
            funcResult = True
            break
        else:
            if checkIndex == 0 or checkIndex == (len(array) - 1):
                break
            else:
                if array[checkIndex] > target:
                    endIndex = checkIndex
                else:
                    startIndex = checkIndex
    return funcResult


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)