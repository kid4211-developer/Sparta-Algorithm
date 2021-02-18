# 비교하고자 하는 알파벳 배열을 선언하여 하나하나 비교해보는 방법
input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26
    max_occurrence = 0
    max_alphabet = ""
    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char)-ord("a")
        alphabet_occurrence_array[arr_index] = alphabet_occurrence_array[arr_index] + 1
        if alphabet_occurrence_array[arr_index] > max_occurrence:
            max_occurrence = alphabet_occurrence_array[arr_index]
            max_alphabet = char
    return max_alphabet


result = find_max_occurred_alphabet(input)
print(result)