# 쉽게 일반화 되어지지 않는 문제, 모든 경우의수를 고려해야하는 문재
# => BFS를 사용하는 문제
# 규칙적 변화 -> 배열 // 자유자재로 바뀜 -> Dictionary

# 각 시간마다 브라운이 갈 수 있는 위치를 저장해야한다

from collections import deque

c = 11
b = 2


def catch_me(cony_loc, brown_loc):
    time = 0
    queue = deque()
    queue.append((brown_loc, 0))
    visited = [{} for _ in range(200001)] # 20만개의 dictionary가 저장됨
    while cony_loc < 20000:
        cony_loc += time  # cony의 위치는 time 만큼 변화 한다.
        if time in visited[cony_loc]:
            return time
        for index in range(0, len(queue)):
            current_position, current_time = queue.popleft()

            new_time = current_time + 1
            new_position = current_position - 1
            if 0 <= new_position <= 20000:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

            new_position = current_position + 1
            if 0 <= new_position <= 20000:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

            new_position = current_position * 2
            if 0 <= new_position <= 20000:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))
        time += 1
    return


print(catch_me(c, b))