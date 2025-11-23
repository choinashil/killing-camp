# 일자: 2025-11-23
# 시작: 17:45
# 종료: 17:59

from collections import defaultdict


def solution(n, computers):
    graph = defaultdict(list)

    for c1 in range(n):
        for c2 in range(n):
            if c1 != c2 and computers[c1][c2] == 1:
                graph[c1].append(c2)

    def dfs(cur_com):
        visited.add(cur_com)

        for c in graph[cur_com]:
            if c not in visited:
                dfs(c)

    visited = set()
    answer = len(computers) - len(graph)

    for com in graph:
        if com not in visited:
            answer += 1
            dfs(com)

    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))  # 2
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))  # 1
