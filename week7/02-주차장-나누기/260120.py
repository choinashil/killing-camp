from collections import defaultdict, deque

# BFS - O(n^2)


def solution(n, cars, links):
    total = sum(cars)
    answer = total

    tree = defaultdict(list)
    for u, v in links:
        tree[u].append(v)
        tree[v].append(u)

    for u, v in links:
        q = deque()
        visited = set()

        q.append(u)
        visited.add(u)
        visited.add(v)

        sub_total = 0

        while q:
            cur_v = q.popleft()
            sub_total += cars[cur_v - 1]

            for next_v in tree[cur_v]:
                if next_v not in visited:
                    q.append(next_v)
                    visited.add(next_v)

        answer = min(answer, abs(total - sub_total * 2))

    return answer

# DFS (후위순회) - O(n)


def solution(n, cars, links):
    total = sum(cars)
    answer = total

    tree = defaultdict(list)
    for u, v in links:
        tree[u].append(v)
        tree[v].append(u)

    def dfs(node, visited):
        nonlocal answer

        sub_total = cars[node - 1]
        visited.add(node)

        for next_v in tree[node]:
            if next_v not in visited:
                sub_total += dfs(next_v, visited)

        answer = min(answer, abs(total - sub_total * 2))
        return sub_total

    visited = set()
    dfs(1, visited)
    return answer


print(solution(13, [22, 9, 1, 15, 8, 6, 20, 7, 11, 5, 10, 4, 1], [[4, 7], [13, 10], [6, 3], [7, 1], [6, 12], [5, 11], [5, 6], [5, 10], [9, 8], [8, 11], [8, 2], [7, 8]]))  # 5
print(solution(6, [6, 4, 10, 9, 8, 4], [[4, 1], [3, 2], [1, 6], [3, 5], [5, 1]]))  # 3
print(solution(3, [2, 7, 3], [[1, 2], [1, 3]]))  # 2
