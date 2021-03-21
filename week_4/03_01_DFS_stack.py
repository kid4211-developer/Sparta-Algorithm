# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}


# 1. 시작 node를 stack에 넣습니다.
# 2. 현재 stack의 node를 빼서 visited에 추가한다.
# 3. 현재 방문한 node와 인접한 node중에서 방문하지 않은 node를 stack에 추가한다
def dfs_stack(adjacent_graph, start_node):
    stack = [start_node]
    visited_array = []
    while stack:
        cur_node = stack.pop()
        visited_array.append(cur_node)
        for node in adjacent_graph[cur_node]:
            if node not in visited_array:
                stack.append(node)
    return visited_array


print(dfs_stack(graph, 1))
