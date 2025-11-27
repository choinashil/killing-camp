from collections import defaultdict
from heapq import heappop, heappush


class Solution:
    def maxProbability(self, n, edges, succ_prob, start, end):
        graph = defaultdict(list)
        for (u, v), p in zip(edges, succ_prob):
            graph[u].append((v, p))
            graph[v].append((u, p))

        max_probs = [0] * n
        max_probs[start] = 1

        pq = [(-1, 1, start)]
        while pq:
            _, cur_prob, cur_v = heappop(pq)

            if max_probs[cur_v] > cur_prob:
                continue

            if cur_v == end:
                return cur_prob

            for next_v, prob in graph[cur_v]:
                next_prob = cur_prob * prob
                if max_probs[next_v] < next_prob:
                    max_probs[next_v] = next_prob
                    heappush(pq, (-next_prob, next_prob, next_v))
        return 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProbability(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.2], 0, 2))
    print(solution.maxProbability(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.3], 0, 2))
    print(solution.maxProbability(3, [[0, 1]], [0.5], 0, 2))
    print(solution.maxProbability(5, [[1, 4], [2, 4], [0, 4], [0, 3], [0, 2], [2, 3]], [0.37, 0.17, 0.93, 0.23, 0.39, 0.04], 3, 4))
