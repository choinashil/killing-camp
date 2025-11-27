from collections import defaultdict, deque


class Solution:
    def findOrder(self, numCourses, prerequisites):
        indegree = [0] * numCourses
        graph = defaultdict(list)
        for next, prev in prerequisites:
            graph[prev].append(next)
            indegree[next] += 1

        q = deque()
        answer = []

        for i, c in enumerate(indegree):
            if c == 0:
                q.append(i)

        while q:
            cur_c = q.popleft()
            answer.append(cur_c)

            for next_c in graph[cur_c]:
                indegree[next_c] -= 1
                if indegree[next_c] == 0:
                    q.append(next_c)

        return answer if len(answer) == numCourses else []


if __name__ == "__main__":
    solution = Solution()
    print(solution.findOrder(2, [[1, 0]]))  # [0, 1]
    print(solution.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))  # [0,1,2,3] 또는 [0,2,1,3]
    print(solution.findOrder(1, []))  # [0]
