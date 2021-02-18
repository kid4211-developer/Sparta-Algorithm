stringArray = "abaccfabade"


def find_not_repeating_character(string):
    alphabet_array = [0] * 26
    result_str = "_"
    index = 0
    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")
        alphabet_array[arr_index] = alphabet_array[arr_index] + 1

    not_repeating_array = []
    for index in range(len(alphabet_array)):
        alphabet_occurrence = alphabet_array[index]

        if alphabet_occurrence == 1:
            not_repeating_array.append(chr(index + ord("a")))

    for str in string:
        if str in not_repeating_array:
            return str


result = find_not_repeating_character(stringArray)
print(result)
