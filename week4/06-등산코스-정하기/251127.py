from collections import defaultdict
from heapq import heappop, heappush


def solution(n, paths, gates, summits):
    graph = defaultdict(list)
    for src, dst, it in paths:
        graph[src].append((dst, it))
        graph[dst].append((src, it))

    pq = []
    INF = float('inf')
    its = [INF] * (n + 1)

    gates_set = set(gates)
    summits_set = set(summits)

    courses = []

    for gate in gates:
        heappush(pq, (0, gate))
        its[gate] = 0

    while pq:
        cur_it, cur_v = heappop(pq)

        if its[cur_v] < cur_it:
            continue

        if cur_v in summits_set:
            heappush(courses, (cur_it, cur_v))
            continue

        for nxt_v, it in graph[cur_v]:
            if nxt_v not in gates_set:
                max_it = max(cur_it, it)
                if its[nxt_v] > max_it:
                    its[nxt_v] = max_it
                    heappush(pq, (max_it, nxt_v))

    result = heappop(courses)
    return [result[1], result[0]]


print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]))  # [5, 3]
print(solution(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2, 3, 4]))  # [3, 4]
print(solution(7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]], [3, 7], [1, 5]))  # [5, 1]
print(solution(5, [[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]], [1, 2], [5]))  # [5, 6]
print(solution(5, [[1, 2, 5], [1, 3, 5], [2, 4, 1], [3, 5, 1]], [1], [4, 5]))  # [4, 5]
