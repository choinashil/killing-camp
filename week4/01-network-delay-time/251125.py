from heapq import heappop, heappush
from collections import defaultdict


class Solution:
    def networkDelayTime(self, times, n, k):
        graph = defaultdict(list)

        for start, end, time in times:
            graph[start].append((end, time))

        arrived_times = [float('inf')] * (n + 1)

        arrived_times[0] = 0
        arrived_times[k] = 0

        pq = []
        for next_v, t in graph[k]:
            heappush(pq, (t, k, next_v))

        while pq:
            t, cur_v, next_v = heappop(pq)
            next_t = arrived_times[cur_v] + t

            if arrived_times[next_v] > next_t:
                arrived_times[next_v] = next_t

                for nv, nt in graph[next_v]:
                    heappush(pq, (nt, next_v, nv))

        max_val = max(arrived_times)
        return -1 if max_val == float('inf') else max_val


if __name__ == '__main__':
    solution = Solution()
    print(solution.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))  # 2
    print(solution.networkDelayTime([[1, 2, 1]], 2, 1))  # 1
    print(solution.networkDelayTime([[1, 2, 1]], 2, 2))  # -1
    print(solution.networkDelayTime([[1, 2, 1], [2, 3, 2], [1, 3, 1]], 3, 2))  # -1
