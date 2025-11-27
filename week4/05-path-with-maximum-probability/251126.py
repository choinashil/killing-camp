from collections import defaultdict
from heapq import heappop, heappush


class Solution:
    def maxProbability(self, n, edges, succ_prob, start_node, end_node):
        pq = []
        probs = [0] * n
        graph = defaultdict(list)
        for i in range(len(edges)):
            n1, n2 = edges[i]
            prob = succ_prob[i]
            graph[n1].append((prob, n2))
            graph[n2].append((prob, n1))

        heappush(pq, (-1, 1, start_node))
        while pq:
            _, cur_prob, cur_node = heappop(pq)
            for prob, next_node in graph[cur_node]:
                next_prob = cur_prob * prob
                if probs[next_node] < next_prob:
                    heappush(pq, (-next_prob, next_prob, next_node))
                    probs[next_node] = next_prob

        return probs[end_node]


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProbability(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.2], 0, 2))
    print(solution.maxProbability(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.3], 0, 2))
    print(solution.maxProbability(3, [[0, 1]], [0.5], 0, 2))
    print(solution.maxProbability(5, [[1, 4], [2, 4], [0, 4], [0, 3], [0, 2], [2, 3]], [0.37, 0.17, 0.93, 0.23, 0.39, 0.04], 3, 4))
