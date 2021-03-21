top_heights = [6, 9, 5, 7, 4]


def get_receiver_top_orders(heights):
    result = [0]
    for i in range(1, len(heights)):
        insert_value = 0
        for j in range(i):
            if heights[j] > heights[i]:
                insert_value = j + 1
        result.append(insert_value)
    return result


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!