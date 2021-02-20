check_string = "0110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    one_to_zero = 0
    zero_to_one = 0
    if string[0] == "0":
        zero_to_one += 1
    else:
        one_to_zero += 1

    for index in range(len(string) - 1):
        index += 1
        if string[index] == string[index - 1]:
            continue
        else:
            if string[index] == "0":
                zero_to_one += 1
            else:
                one_to_zero += 1
    print("one_to_zero : ", one_to_zero)
    print("zero_to_one : ", zero_to_one)
    return min(zero_to_one, one_to_zero)


result = find_count_to_turn_out_to_all_zero_or_all_one(check_string)
print(result)