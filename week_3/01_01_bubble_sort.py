input = [4, 6, 2, 9, 1]


def bubble_sort(array):
    # 이 부분을 채워보세요!
    end_index = len(array) - 1
    while 0 < end_index:
        print(end_index)
        for count in range(end_index):
            left_num = array[count]
            right_num = array[count + 1]
            if left_num > right_num:
                array[count], array[count + 1] = right_num, left_num
        end_index = end_index - 1
    return


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!