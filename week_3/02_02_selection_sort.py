input = [4, 6, 2, 9, 1]


def selection_sort(array):
    length = len(array)
    for index in range(length - 1):
        min_index = index
        for count in range(length - index):
            if array[index + count] < array[min_index]:
                min_index = index + count
        array[index], array[min_index] = array[min_index], array[index]
    return


selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!