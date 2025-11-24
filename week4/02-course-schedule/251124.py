from collections import deque


class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]

        for cur, prev in prerequisites:
            graph[prev].append(cur)
            indegree[cur] += 1

        q = deque()
        visited = set()

        for v in range(len(indegree)):
            if indegree[v] == 0:
                q.append(v)

        while q:
            cur_v = q.popleft()
            visited.add(cur_v)

            for next_v in graph[cur_v]:
                indegree[next_v] -= 1

                if indegree[next_v] == 0:
                    q.append(next_v)

        return len(visited) == numCourses


if __name__ == '__main__':
    solution = Solution()
    print(solution.canFinish(2, [[1, 0]]))
    print(solution.canFinish(2, [[1, 0], [0, 1]]))
    print(solution.canFinish(5, [[1, 4], [2, 4], [3, 1], [3, 2]]))
