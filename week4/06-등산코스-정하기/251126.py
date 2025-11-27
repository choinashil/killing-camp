from collections import defaultdict
from heapq import heappop, heappush


def solution(n, paths, gates, summits):
    graph = defaultdict(list)
    for u, v, t in paths:
        graph[u].append((v, t))
        graph[v].append((u, t))

    gates_set = set(gates)
    summits_set = set(summits)

    INF = float('inf')
    intensity = [INF] * (n + 1)
    pq = []
    courses = []

    for gate in gates:
        intensity[gate] = 0
        heappush(pq, (0, gate))

    while pq:
        cur_t, cur_v = heappop(pq)

        if cur_t > intensity[cur_v]:
            continue

        if cur_v in summits_set:
            heappush(courses, [intensity[cur_v], cur_v])
            continue

        for next_v, t in graph[cur_v]:
            if next_v in gates_set:
                continue

            new_intensity = max(cur_t, t)

            if new_intensity < intensity[next_v]:
                intensity[next_v] = new_intensity
                heappush(pq, (new_intensity, next_v))

    result = heappop(courses)
    return [result[1], result[0]]


print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]))  # [5, 3]
print(solution(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2, 3, 4]))  # [3, 4]
print(solution(7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]], [3, 7], [1, 5]))  # [5, 1]
print(solution(5, [[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]], [1, 2], [5]))  # [5, 6]
print(solution(5, [[1, 2, 5], [1, 3, 5], [2, 4, 1], [3, 5, 1]], [1], [4, 5]))  # [4, 5]
