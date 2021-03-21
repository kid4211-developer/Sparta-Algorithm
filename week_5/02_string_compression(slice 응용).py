# 모든 경우의 수를 체크해서 최소값을 반환하는 구조
# 문자열을 자르는 문제 : slice 개념을 사용
input = "abcabcabcabcdededededede"


def string_compression(string):
    n = len(string)
    compression_length_array = []
    for separate_size in range(1, n // 2 + 1):
        separated = [string[index:(index + separate_size)] for index in range(0, n, separate_size)]
        count = 1
        compressed = ""
        for j in range(1, len(separated)):
            prevString, curString = separated[j - 1], separated[j]
            if prevString == curString:
                count += 1
            else:
                if count > 1:
                    compressed += str(count) + prevString
                else:
                    compressed += prevString
                count = 1
        if count > 1:
            compressed += str(count) + separated[-1]
        else:
            compressed += separated[-1]
        compression_length_array.append(len(compressed))
    return min(compression_length_array)


print(string_compression(input))  # 14 가 출력되어야 합니다!