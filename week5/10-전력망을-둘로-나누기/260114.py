from collections import defaultdict, deque


def solution(n, wires):
    graph = defaultdict(list)
    for u, v in wires:
        graph[u].append(v)
        graph[v].append(u)

    answer = n

    for u, v in wires:
        q = deque()
        visited = set()

        q.append(u)
        visited.add(u)
        visited.add(v)

        count = 0

        while q:
            cur_v = q.popleft()
            count += 1

            for next_v in graph[cur_v]:
                if next_v not in visited:
                    q.append(next_v)
                    visited.add(next_v)

        answer = min(answer, abs(n - count * 2))

    return answer


print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))  # 3
