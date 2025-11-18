from collections import deque


class Solution:
    def isBipartite(self, graph):
        def bfs(start_v):
            q.append(start_v)

            if visited[start_v] == -1:
                visited[start_v] = 0

            while q:
                cur_v = q.popleft()

                for next_v in graph[cur_v]:
                    if visited[next_v] == -1:
                        q.append(next_v)
                        visited[next_v] = 0 if visited[cur_v] == 1 else 1
                    elif visited[next_v] == visited[cur_v]:
                        return False
            return True

        q = deque()
        visited = [-1] * len(graph)

        for i in range(len(graph)):
            if not bfs(i):
                return False

        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]))
    print(solution.isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]]))
    print(solution.isBipartite([[4, 1], [0, 2], [1, 3], [2, 4], [3, 0]]))
    print(solution.isBipartite([[], [2, 4, 6], [1, 4, 8, 9], [7, 8], [1, 2, 8, 9], [6, 9], [1, 5, 7, 8, 9], [3, 6, 9], [2, 3, 4, 6, 9], [2, 4, 5, 6, 7, 8]]))
