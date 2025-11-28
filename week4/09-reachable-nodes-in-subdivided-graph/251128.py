from collections import defaultdict
from heapq import heappop, heappush


class Solution:
    def reachableNodes(self, edges, max_moves, n):
        graph = defaultdict(list)
        for u, v, cnt in edges:
            graph[u].append((v, cnt))
            graph[v].append((u, cnt))
        # print('graph:', graph)

        edge_visited = defaultdict(int)
        node_visited = set()

        INF = float('inf')
        distances = [INF] * n
        distances[0] = 0

        pq = [(0, 0)]

        while pq:
            cur_dist, cur_v = heappop(pq)
            node_visited.add(cur_v)
            # print('cur_dist:', cur_dist, 'cur_v:', cur_v)

            if cur_dist > distances[cur_v]:
                continue

            for next_v, cnt in graph[cur_v]:
                # print('next_v:', next_v, 'cnt:', cnt)
                remaining = max_moves - cur_dist
                available = min(cnt, remaining)
                # print('max_moves:', max_moves, 'cur_dist:', cur_dist, 'remaining:', remaining, 'available:', available)
                edge_visited[(cur_v, next_v)] = max(edge_visited[(cur_v, next_v)], available)

                next_dist = cur_dist + cnt + 1
                if next_dist < distances[next_v] and next_dist <= max_moves:
                    distances[next_v] = next_dist
                    heappush(pq, (next_dist, next_v))

        answer = len(node_visited)
        print(distances)

        for u, v, cnt in edges:
            from_u = edge_visited[(u, v)]
            from_v = edge_visited[(v, u)]
            actual = min(from_u + from_v, cnt)
            answer += actual

        return answer


if __name__ == '__main__':
    solution = Solution()
    print(solution.reachableNodes([[0, 1, 10], [0, 2, 1], [1, 2, 2]], 6, 3))
    print(solution.reachableNodes([[0, 1, 4], [1, 2, 6], [0, 2, 8], [1, 3, 1]], 10, 4))
    print(solution.reachableNodes([[1, 2, 4], [1, 4, 5], [1, 3, 1], [2, 3, 4], [3, 4, 5]], 17, 5))
