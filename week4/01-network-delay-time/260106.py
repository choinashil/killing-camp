from collections import defaultdict
from heapq import heappush, heappop


class Solution:
    def networkDelayTime(self, times, n, k):
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        INF = float('inf')
        memo = [INF] * (n + 1)
        memo[0] = 0
        memo[k] = 0

        pq = []
        heappush(pq, (0, k))

        while pq:
            cur_t, cur_v = heappop(pq)

            if memo[cur_v] < cur_t:
                continue

            for next_v, t in graph[cur_v]:
                next_t = cur_t + t

                if memo[next_v] > next_t:
                    memo[next_v] = next_t
                    heappush(pq, (next_t, next_v))

        return -1 if sum(memo) == INF else max(memo)


if __name__ == '__main__':
    solution = Solution()
    print(solution.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))  # 2
    print(solution.networkDelayTime([[1, 2, 1]], 2, 1))  # 1
    print(solution.networkDelayTime([[1, 2, 1]], 2, 2))  # -1
