from collections import deque


def solution(n, m, hole):
    q = deque()

    visited = set()
    for r, c in hole:
        visited.add((r, c, True))
        visited.add((r, c, False))

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    q.append((1, 1, 0, True))
    visited.add((1, 1, True))

    answer = -1

    while q:
        cur_r, cur_c, cur_count, available = q.popleft()

        if cur_r == n and cur_c == m:
            answer = cur_count
            break

        for i in range(4):
            next_r = cur_r + dr[i]
            next_c = cur_c + dc[i]

            if 1 <= next_r <= n and 1 <= next_c <= m and (next_r, next_c, available) not in visited:
                q.append((next_r, next_c, cur_count + 1, available))
                visited.add((next_r, next_c, available))

        if available:
            for i in range(4):
                next_r = cur_r + dr[i] * 2
                next_c = cur_c + dc[i] * 2

                if 1 <= next_r <= n and 1 <= next_c <= m and (next_r, next_c, False) not in visited:
                    q.append((next_r, next_c, cur_count + 1, False))
                    visited.add((next_r, next_c, False))

    return answer


print(solution(4, 4, [[2, 3], [3, 3]]))  # 5
print(solution(5, 4, [[1, 4], [2, 1], [2, 2], [2, 3], [2, 4], [3, 3], [4, 1], [4, 3], [5, 3]]))  # -1
