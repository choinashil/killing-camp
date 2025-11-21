from collections import deque


def solution(n, m, x, y, r, c, k):
    dr = [1, 0, 0, -1]
    dc = [0, -1, 1, 0]
    p = ['d', 'l', 'r', 'u']

    def in_range(r, c):
        return 1 <= r <= n and 1 <= c <= m

    def bfs(sr, sc):
        q = deque()
        q.append((sr, sc, ''))

        while q:
            cr, cc, cp = q.popleft()

            if cr == r and cc == c and len(cp) == k:
                return cp

            for i in range(4):
                nr, nc, np = cr + dr[i], cc + dc[i], cp + p[i]

                if in_range(nr, nc) and len(np) <= k:
                    q.append((nr, nc, np))

    answer = 'impossible'
    result = bfs(x, y)
    return result or answer


print(solution(2, 2, 1, 1, 2, 2, 2))  # "dr"
print(solution(3, 4, 2, 3, 3, 1, 5))  # "dllrl"
print(solution(3, 3, 1, 2, 3, 3, 4))  # "impossible"
