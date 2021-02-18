numArray = [3, 5, 6, 1, 2, 4]


def is_number_exist(number, array):
    for num in array:  # array 길이만큼 반복(N번)
        if num == number:  # 비교 연산 한번 실행(1번)
            return True
    return False

# is_number_exist 함수의 시간 복잡도 =  1 ~ N
# 최고 : 1 / 최악 : N
# 시간복잡도는 일정하지 않을수 있음, 엄청큰 배열의 경우 초반부와 후반부에 원소가 발견되는 것은 확실한 시간적 차이가 존재함


result = is_number_exist(3, numArray)
print(result)
