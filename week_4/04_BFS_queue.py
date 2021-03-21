graph = {
    1: [2, 3, 4],
    2: [1, 5],
    3: [1, 6, 7],
    4: [1, 8],
    5: [2, 9],
    6: [3, 10],
    7: [3],
    8: [4],
    9: [5],
    10: [6]
}


# 1. 시작 node를 queue에 넣는다.
# 2. 현재 queue의 node를 빼서 visited에 추가한다. (queue의 특성상 stack과는 다르게 First in first out)
# 3. 현재 방문한 node와 인접한 node중 방문하지 않은 node를 queue에 추가한다.
def bfs_queue(adj_graph, start_node):
    queue = [start_node]
    visited_array = []
    while queue:
        cur_node = queue.pop(0)
        visited_array.append(cur_node)
        for node in adj_graph[cur_node]:
            if node not in visited_array:
                queue.append(node)
    return visited_array


print(bfs_queue(graph, 1))