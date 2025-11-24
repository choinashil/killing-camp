from heapq import heappop, heappush


class Solution:
    def networkDelayTime(self, times, n, k):
        INF = float('inf')

        pq = []
        graph = [[] for _ in range(n + 1)]
        arrived_times = [INF for _ in range(n + 1)]

        for cur, next, time in times:
            graph[cur].append((time, next))

        arrived_times[0] = 0
        arrived_times[k] = 0
        heappush(pq, (0, k))

        while pq:
            cur_t, cur_v = heappop(pq)

            if arrived_times[cur_v] < cur_t:
                continue

            for t, next_v in graph[cur_v]:
                next_t = cur_t + t

                if next_t < arrived_times[next_v]:
                    arrived_times[next_v] = next_t
                    heappush(pq, (next_t, next_v))

        result = max(arrived_times)
        return -1 if result == INF else result


# 참고 코드
# from collections import defaultdict


# class Solution:
#     def networkDelayTime(self, times, n, k):
#         graph = defaultdict(list)

#         for cur, next, time in times:
#             graph[cur].append((time, next))

#         visited = set()
#         pq = [(0, k)]

#         while pq:
#             cur_t, cur_v = heappop(pq)
#             visited.add(cur_v)

#             if len(visited) == n:
#                 return cur_t

#             for t, next_v in graph[cur_v]:
#                 if next_v not in visited:
#                     next_t = cur_t + t
#                     heappush(pq, (next_t, next_v))

if __name__ == '__main__':
    solution = Solution()
    print(solution.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))
    print(solution.networkDelayTime([[1, 2, 1]], 2, 1))
    print(solution.networkDelayTime([[1, 2, 1]], 2, 2))
    print(solution.networkDelayTime([[1, 2, 1], [2, 3, 2], [1, 3, 1]], 3, 2))
