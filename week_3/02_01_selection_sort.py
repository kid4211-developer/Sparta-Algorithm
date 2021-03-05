input = [4, 6, 2, 9, 1]


def selection_sort(array):
    length = len(array) - 1
    for index in range(length):
        for count in range(length - index):
            if array[index] > array[count + index + 1]:
                array[index], array[count + index + 1] = array[count + index + 1], array[index]
    return


selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!