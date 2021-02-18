value = 20


def find_prime_list_under_number(number):
    findNum = []
    for num in range(number):
        num += 1
        count = 0
        for checkNum in range(num):
            checkNum += 1
            if num % checkNum == 0:
                count += 1
        if count == 2:
            findNum.append(num)

    return findNum


result = find_prime_list_under_number(value)
print(result)