from collections import defaultdict
from heapq import heappop, heappush


# 1차 시도
# def solution(n, s, a, b, fares):
#     graph = defaultdict(list)
#     for src, dst, fare in fares:
#         graph[src].append((dst, fare))
#         graph[dst].append((src, fare))

#     INF = float('inf')
#     min_fare = INF

#     def move(s, k):
#         pq = [(0, s)]
#         min_fares = [INF] * (n + 1)
#         min_fares[s] = 0

#         while pq:
#             cur_fare, cur_v = heappop(pq)

#             if min_fares[cur_v] < cur_fare:
#                 continue

#             if cur_v == k:
#                 return cur_fare

#             for nxt_v, fare in graph[cur_v]:
#                 nxt_fare = cur_fare + fare
#                 if min_fares[nxt_v] > nxt_fare:
#                     min_fares[nxt_v] = nxt_fare
#                     heappush(pq, (nxt_fare, nxt_v))
#         return INF

#     for k in range(1, n + 1):
#         k_fare = 0 if s == k else move(s, k)
#         a_fare = 0 if a == k else move(k, a)
#         b_fare = 0 if b == k else move(k, b)

#         min_fare = min(min_fare, k_fare + a_fare + b_fare)
#     return min_fare


# 2차 시도 (개선안)

def solution(n, s, a, b, fares):
    graph = defaultdict(list)
    for src, dst, fare in fares:
        graph[src].append((dst, fare))
        graph[dst].append((src, fare))

    INF = float('inf')
    min_fare = INF

    def dijkstra(s):
        pq = [(0, s)]
        min_fares = [INF] * (n + 1)
        min_fares[s] = 0

        while pq:
            cur_fare, cur_v = heappop(pq)

            if min_fares[cur_v] < cur_fare:
                continue

            for nxt_v, fare in graph[cur_v]:
                nxt_fare = cur_fare + fare
                if min_fares[nxt_v] > nxt_fare:
                    min_fares[nxt_v] = nxt_fare
                    heappush(pq, (nxt_fare, nxt_v))
        return min_fares

    s_min_fares = dijkstra(s)
    a_min_fares = dijkstra(a)
    b_min_fares = dijkstra(b)

    for v in range(1, n + 1):
        min_fare = min(min_fare, s_min_fares[v] + a_min_fares[v] + b_min_fares[v])

    return min_fare


print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))  # 82
print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))  # 14
print(solution(6, 4, 5, 6, [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]))  # 18
print(solution(4, 2, 1, 3, [[1, 2, 2], [2, 3, 5]]))
