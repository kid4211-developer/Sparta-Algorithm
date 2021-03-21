top_heights = [6, 9, 5, 7, 4]

# 시간복잡도 : O(N^2)
def get_receiver_top_orders(heights):
    answer = [0] * len(heights)
    while heights:  # while문에 배열을 조건으로 걸게되면 배열의 길이가 0이되면 멈추게 됨됨
        height = heights.pop()
        for index in range(len(heights) - 1, 0, -1):
            if heights[index] > height:
                answer[len(heights)] = index + 1
                break
    return answer


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!