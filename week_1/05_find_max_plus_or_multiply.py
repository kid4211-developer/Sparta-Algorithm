input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    func_result = 0
    for num in array:
        if num > 1:
            if func_result > 1:
                func_result = func_result * num
            else:
                func_result = func_result + num
        else:
            func_result = func_result + num
    return func_result


result = find_max_plus_or_multiply(input)
print(result)