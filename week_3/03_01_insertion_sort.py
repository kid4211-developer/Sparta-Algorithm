input = [4, 6, 2, 9, 1]


def insertion_sort(array):
    length = len(array) - 1
    for i in range(length):
        for j in range(i + 1):
            if array[i + 1 - j] < array[i - j]:
                array[i - j], array[i + 1 - j] = array[i + 1 - j], array[i - j]
    return


insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!