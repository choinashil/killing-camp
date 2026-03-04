from collections import deque


def solution(n, m, x, y, r, c, k):
    q = deque()
    q.append((x, y, 0, ''))

    # 아래(d) -> 왼쪽(l) -> 오른쪽(r) -> 위쪽(u)
    dr = [1, 0, 0, -1]
    dc = [0, -1, 1, 0]
    directions = ['d', 'l', 'r', 'u']

    while q:
        cur_r, cur_c, cur_count, cur_char = q.popleft()

        if cur_count == k and cur_r == r and cur_c == c:
            return cur_char

        for i in range(4):
            next_r, next_c = cur_r + dr[i], cur_c + dc[i]

            if 1 <= next_r <= n and 1 <= next_c <= m and abs(next_r - r) + abs(next_c - c) <= k - cur_count:
                q.append((next_r, next_c, cur_count + 1, cur_char + directions[i]))
                break

    return 'impossible'


print(solution(3, 4, 2, 3, 3, 1, 5))  # dllrl
print(solution(3, 3, 1, 2, 3, 3, 4))  # impossible
