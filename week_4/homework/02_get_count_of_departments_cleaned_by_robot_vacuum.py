current_r, current_c, current_d = 7, 4, 0
current_room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


# BFS 문제
# 1. 처리한 내용에 대한 data를 저장해야함 -> 미청소 : 0 / 청소 불가 : 1 / 청소완료 : 2
# 2. 방향의 이동 개념
# - 북쪽 : -1, 0 / 남쪽 : 1, 0 / 동쪽 : 0, 1 / 서쪽 : 0, -1
# dr : [-1, 0, 1, 0]
# dc : [0, 1, 0, -1]
# 3. 회전의 개념(왼쪽 방향) : 북 -> 서, 서 -> 남, 남 -> 동, 동 -> 북
#    ((현재의 방향 index + 3) % 4)가 바라보는 방향의 index가 된다

# 북 동 남 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


# 방향 전환
def get_d_index_when_rotate_to_left(d):
    return (d + 3) % 4


# 후진
def get_d_index_when_go_back(d):
    return (d + 2) % 4


def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):
    n = len(room_map)  # 세로
    m = len(room_map[0])  # 가로
    count_of_departments_cleaned = 1
    room_map[r][c] = 2
    queue = list([[r, c, d]])

    while queue:
        r, c, d = queue.pop(0)
        temp_d = d
        for index in range(4):
            # 현재방향 기준 왼쪽으로 회전해야함
            temp_d = get_d_index_when_rotate_to_left(temp_d)
            new_r, new_c = r + dr[temp_d], c + dc[temp_d]

            # 1. 청소할 타일이 있는 경우
            if 0 <= new_r < n and 0 <= new_c < m and room_map[new_r][new_c] == 0:
                count_of_departments_cleaned += 1
                room_map[new_r][new_c] = 2
                queue.append([new_r, new_c, temp_d])
                break

            # 2. 청소할 타일이 없는 경우(or 구역을 벗어난 경우)
            elif index == 3:
                # 3. 후진할 타일이 있는 경우
                new_r, new_c = r + dr[get_d_index_when_go_back(d)], c + dc[get_d_index_when_go_back(d)]
                queue.append([new_r, new_c, d])

                # 4. 뒤가 벽인 경우(후진을 할수 없는 경우)
                if room_map[new_r][new_c] == 1:  # 뒤가 벽인 경우
                    return count_of_departments_cleaned


# 57 가 출력되어야 합니다!
print(get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map))