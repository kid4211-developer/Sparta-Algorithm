import itertools
import sys

a = 5
b = 3

map_array = [
    [0, 0, 1, 0, 0],
    [0, 0, 2, 0, 1],
    [0, 1, 2, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 2],
]


# 여러개 중에서 M개를 고른 뒤, 모든 치킨 거리의 합이 가장 작게 되는 경우를 반환
# -> 여러 개 중에서 특정 개수를 뽑는 경우의 수
# -> 모든 경우의수를 다 구해야하는 문제 : "조합" (itertools - combinations 개념 사용)
# 두값을 비교해서 더 작은값 반환 : min( ) / 절대값 반환 : abs( )
def get_min_city_chicken_distance(n, m, city_map):
    chicken_location_list = []
    home_location_list = []
    for i in range(n):  # n : city_map 행 & 열의 길이
        for j in range(n):
            if city_map[i][j] == 1:
                home_location_list.append([i, j])
            elif city_map[i][j] == 2:
                chicken_location_list.append([i, j])
    # 조합 생성
    chicken_location_m_combinations = list(itertools.combinations(chicken_location_list, m))
    min_distance_of_m_combinations = sys.maxsize

    for chicken_location_m_combination in chicken_location_m_combinations:
        city_chicken_distance = 0
        for home_r, home_c in home_location_list:
            min_home_chicken_distance = sys.maxsize
            for chicken_location in chicken_location_m_combination:
                min_home_chicken_distance = min(
                    min_home_chicken_distance,
                    (abs(home_r - chicken_location[0]) + abs(home_c - chicken_location[1]))
                )
            city_chicken_distance += min_home_chicken_distance
        min_distance_of_m_combinations = min(min_distance_of_m_combinations, city_chicken_distance)
    return min_distance_of_m_combinations


print(get_min_city_chicken_distance(a, b, map_array))