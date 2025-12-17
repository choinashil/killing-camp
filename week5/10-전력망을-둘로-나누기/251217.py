from collections import defaultdict, deque


def solution(n, wires):
    answer = float('inf')

    tree = defaultdict(list)
    for u, v in wires:
        tree[u].append(v)
        tree[v].append(u)

    for u, v in wires:
        q = deque()
        visited = set()
        count = 0

        q.append(u)
        visited.add(u)

        while q:
            cur_v = q.popleft()
            count += 1

            for next_v in tree[cur_v]:
                if next_v != v and next_v not in visited:
                    q.append(next_v)
                    visited.add(next_v)

        answer = min(answer, abs(n - count - count))

    return answer


print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))  # 3
print(solution(4, [[1, 2], [2, 3], [3, 4]]))  # 0
print(solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]))  # 1
