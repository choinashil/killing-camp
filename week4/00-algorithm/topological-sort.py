from collections import deque


def topological_sort(n, prerequisites):
    graph = [[] for _ in range(n)]
    indegree = [0 for _ in range(n)]

    print(graph, indegree)

    for cur, prev in prerequisites:
        graph[prev].append(cur)
        indegree[cur] += 1

    print(graph, indegree)

    q = deque()
    visited = []

    for v in range(n):
        if indegree[v] == 0:
            q.append(v)

    while q:
        cur_v = q.popleft()
        visited.append(cur_v)

        for next_v in graph[cur_v]:
            indegree[next_v] -= 1

            if indegree[next_v] == 0:
                q.append(next_v)

    return visited


n = 4
prerequisites = [
    [1, 0],
    [2, 0],
    [3, 1],
    [3, 2]
]

print(topological_sort(n, prerequisites))
