from collections import deque


class Solution:
    def isBipartite(self, graph):
        q = deque()
        visited = [0] * len(graph)

        for cur_v in range(len(graph)):
            q.append(cur_v)
            if visited[cur_v] == 0:
                visited[cur_v] = 1

            while q:
                cur_v = q.popleft()

                for next_v in graph[cur_v]:
                    if visited[next_v] == visited[cur_v]:
                        return False

                    if visited[next_v] == 0:
                        q.append(next_v)
                        visited[next_v] = 1 if visited[cur_v] == 2 else 2

        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]))
    print(solution.isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]]))
    print(solution.isBipartite([[], [2, 4, 6], [1, 4, 8, 9], [7, 8], [1, 2, 8, 9], [6, 9], [1, 5, 7, 8, 9], [3, 6, 9], [2, 3, 4, 6, 9], [2, 4, 5, 6, 7, 8]]))
