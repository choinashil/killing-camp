# 일자: 2025-11-23
# 시작: 17:59
# 종료: 18:54
# 결과:
# - 정확성 10개 중 4개 통과
# - 효율성 30개 모두 실패

from collections import defaultdict


def solution(n, s, a, b, fares):
    graph = defaultdict(list)

    for v1, v2, f in fares:
        graph[v1].append((v2, f))
        graph[v2].append((v1, f))

    def dfs(cur_v, cur_f, a_arrived, b_arrived, visited):
        nonlocal a_min, b_min, together_min

        visited.add(cur_v)

        if cur_v >= together_min:
            return

        if cur_v == a:
            a_arrived = True
            a_min = min(a_min, cur_f)

        if cur_v == b:
            b_arrived = True
            b_min = min(b_min, cur_f)

        if a_arrived and b_arrived:
            together_min = min(together_min, cur_f)
            return

        for next_v, f in graph[cur_v]:
            if next_v not in visited:
                dfs(next_v, cur_f + f, a_arrived, b_arrived, visited)

    a_min = 999999999
    b_min = 999999999
    together_min = 999999999

    dfs(s, 0, False, False, set())

    return min(a_min + b_min, together_min)


# print(solution(3, 1, 2, 3, [[1, 2, 10], [2, 3, 5], [1, 3, 6]]))
# print(solution(3, 1, 2, 3, [[1, 2, 10], [2, 3, 5], [1, 3, 3]]))
print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))  # 82
# print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))  # 14
# print(solution(6, 4, 5, 6, [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]))  # 18
