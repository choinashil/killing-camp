from collections import defaultdict
from heapq import heappop, heappush


def solution(n, s, a, b, fares):
    graph = defaultdict(list)
    for u, v, f in fares:
        graph[u].append((v, f))
        graph[v].append((u, f))

    def dijkstra(start):
        pq = []
        heappush(pq, (0, start))
        visited = [float('inf')] * (n + 1)
        visited[start] = 0

        while pq:
            cur_f, cur_v = heappop(pq)

            if visited[cur_v] < cur_f:
                continue

            for next_v, fare in graph[cur_v]:
                next_f = cur_f + fare
                if visited[next_v] > next_f:
                    visited[next_v] = next_f
                    heappush(pq, (next_f, next_v))

        return visited

    s_visited = dijkstra(s)
    a_visited = dijkstra(a)
    b_visited = dijkstra(b)

    print(s_visited)
    print(a_visited)
    print(b_visited)

    answer = float('inf')

    for v in range(1, n + 1):
        answer = min(answer, s_visited[v] + a_visited[v] + b_visited[v])

    return answer


# print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))  # 82
print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))  # 14
# print(solution(6, 4, 5, 6, [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]))  # 18
# print(solution(4, 2, 1, 3, [[1, 2, 2], [2, 3, 5]]))
