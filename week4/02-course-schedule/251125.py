from collections import deque, defaultdict


class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for next, before in prerequisites:
            graph[before].append(next)
            indegree[next] += 1

        q = deque()

        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)

        while q:
            cur = q.popleft()
            for next in graph[cur]:
                indegree[next] -= 1
                if indegree[next] == 0:
                    q.append(next)

        return False if sum(indegree) else True


if __name__ == '__main__':
    solution = Solution()
    print(solution.canFinish(2, [[1, 0]]))  # True
    print(solution.canFinish(2, [[1, 0], [0, 1]]))  # False
    print(solution.canFinish(5, [[1, 4], [2, 4], [3, 1], [3, 2]]))  # True
