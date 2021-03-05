array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]


def merge(array1, array2):
    new_array = []
    count = 0
    for i in range(len(array2)):
        print('array1 length', len(array1))
        print('count :', count)
        if count == len(array1):
            for j in range(i - 1, len(array2)):
                new_array.append(array_b[j])
            break
        for k in range(count, len(array1)):
            if array1[k] < array2[i]:
                new_array.append(array1[k])
                count = count + 1
            else:
                new_array.append(array2[i])
                break
    return new_array


print(merge(array_a, array_b))