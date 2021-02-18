value = 20

findNum = []
for num in range(value):
    num += 1
    count = 0
    for checkNum in range(num):
        checkNum += 1
        if num % checkNum == 0:
            count += 1
    if count == 2:
        print("num : ", num)
        findNum.append(num)

print(findNum)
