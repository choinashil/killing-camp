from collections import deque


def solution(board):
    n = len(board)

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    q = deque()
    visited = set()

    def is_valid(r, c):
        if 0 <= r < n and 0 <= c < n:
            return board[r][c] == 0
        return False

    def is_visited(r1, c1, r2, c2):
        return (r1, c1, r2, c2) not in visited and (r2, c2, r1, c1) not in visited

    q.append((0, 0, 0, 1, 0))
    visited.add((0, 0, 0, 1))
    visited.add((0, 1, 0, 0))

    while q:
        r1, c1, r2, c2, t = q.popleft()

        if (r1 == n - 1 and c1 == n - 1) or (r2 == n - 1 and c2 == n - 1):
            return t

        for i in range(4):
            nr1, nc1, nr2, nc2 = r1 + dr[i], c1 + dc[i], r2 + dr[i], c2 + dc[i]
            if is_valid(nr1, nc1) and is_valid(nr2, nc2) and is_visited(nr1, nc1, nr2, nc2):
                q.append((nr1, nc1, nr2, nc2, t + 1))
                visited.add((nr1, nc1, nr2, nc2))
                visited.add((nr2, nc2, nr1, nc1))

        if r1 == r2:
            for dr1, dc1, dr2, dc2, dar, dac in [[-1, 0, 0, -1, -1, 1], [0, 0, 1, -1, 1, 1], [-1, 1, 0, 0, -1, 0], [0, 1, 1, 0, 1, 0]]:
                nr1, nc1, nr2, nc2 = r1 + dr1, c1 + dc1, r2 + dr2, c2 + dc2
                ar, ac = r1 + dar, c1 + dac

                if is_valid(nr1, nc1) and is_valid(nr2, nc2) and is_valid(ar, ac) and is_visited(nr1, nc1, nr2, nc2):
                    q.append((nr1, nc1, nr2, nc2, t + 1))
                    visited.add((nr1, nc1, nr2, nc2))
                    visited.add((nr2, nc2, nr1, nc1))
        else:
            for dr1, dc1, dr2, dc2, dar, dac in [(1, -1, 0, 0, 0, -1), (1, 0, 0, 1, 0, 1), (0, -1, 1, 0, 1, -1), (0, 0, -1, 1, 1, 1)]:
                nr1, nc1, nr2, nc2 = r1 + dr1, c1 + dc1, r2 + dr2, c2 + dc2
                ar, ac = r1 + dar, c1 + dac

                if is_valid(nr1, nc1) and is_valid(nr2, nc2) and is_valid(ar, ac) and is_visited(nr1, nc1, nr2, nc2):
                    q.append((nr1, nc1, nr2, nc2, t + 1))
                    visited.add((nr1, nc1, nr2, nc2))
                    visited.add((nr2, nc2, nr1, nc1))


print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))
