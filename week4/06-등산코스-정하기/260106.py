from collections import defaultdict
from heapq import heappop, heappush


def solution(n, paths, gates, summits):
    graph = defaultdict(list)
    for u, v, w in paths:
        graph[u].append((v, w))
        graph[v].append((u, w))

    INF = float('inf')
    visited = [INF] * (n + 1)

    gates_set = set(gates)
    summits_set = set(summits)

    pq = []
    for gate in gates:
        visited[gate] = 0
        heappush(pq, (0, gate))

    courses = []

    while pq:
        cur_i, cur_v = heappop(pq)

        if visited[cur_v] < cur_i:
            continue

        if cur_v in summits_set:
            heappush(courses, (cur_i, cur_v))
            continue

        for next_v, t in graph[cur_v]:
            if next_v in gates_set:
                continue

            max_i = max(cur_i, t)

            if visited[next_v] > max_i:
                visited[next_v] = max_i
                heappush(pq, (max_i, next_v))

    answer = heappop(courses)
    return [answer[1], answer[0]]


print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]))  # [5, 3]
print(solution(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2, 3, 4]))  # [3, 4]
print(solution(7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]], [3, 7], [1, 5]))  # [5, 1]
print(solution(5, [[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]], [1, 2], [5]))  # [5, 6]
print(solution(5, [[1, 2, 5], [1, 3, 5], [2, 4, 1], [3, 5, 1]], [1], [4, 5]))  # [4, 5]
