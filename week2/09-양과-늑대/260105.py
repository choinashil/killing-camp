from collections import defaultdict


def solution(info, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    def dfs(cur_v, sheep, wolf, can_visit):
        if info[cur_v]:
            wolf += 1
        else:
            sheep += 1

        if wolf >= sheep:
            return

        answer[0] = max(answer[0], sheep)

        for child in graph[cur_v]:
            can_visit.add(child)

        for next_v in can_visit:
            dfs(next_v, sheep, wolf, can_visit - {next_v})

    answer = [0]
    dfs(0, 0, 0, set())
    return answer[0]


print(solution([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1], [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]))  # 5
print(solution([0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0], [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]]))  # 5
