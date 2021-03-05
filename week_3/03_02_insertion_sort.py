input = [4, 6, 2, 9, 1]


# 삽입정렬의 가장 큰 특징은 비교시에 변경이 필요없음이 감지되면 반복문이 중단되는 점
def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        for j in range(i):
            if array[i - j - 1] > array[i - j]:
                array[i - j - 1], array[i - j] = array[i - j], array[i - j - 1]
            else:
                break
    return


insertion_sort(input)
print(input)