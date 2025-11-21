from collections import deque


def solution(n, m, hole):
    q = deque()
    visited = set()
    hole_pos = set()

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    for hr, hc in hole:
        hole_pos.add((hc - 1, hr - 1))

    def in_range(r, c):
        return 0 <= r < n and 0 <= c < m

    def bfs(sr, sc):
        q.append((sr, sc, 0, False))
        visited.add((sr, sc))

        while q:
            cr, cc, t, shoe_used = q.popleft()

            if cr == n - 1 and cc == m - 1:
                return t

            for i in range(4):
                nr, nc = cr + dr[i], cc + dc[i]

                if in_range(nr, nc) and (nr, nc) not in visited:
                    if (nr, nc) in hole_pos:
                        if shoe_used:
                            return -1
                        else:
                            nnr, nnc = nr + dr[i], nc + dc[i]
                            if (nnr, nnc) not in hole_pos:
                                q.append((nnr, nnc, t + 1, True))
                                visited.add((nr, nc))
                                visited.add((nnr, nnc))
                    else:
                        q.append((nr, nc, t + 1, shoe_used))
                        visited.add((nr, nc))

    return bfs(0, 0)


print(solution(4, 4, [[2, 3], [3, 3]]))  # 5
print(solution(5, 4, [[1, 4], [2, 1], [2, 2], [2, 3], [2, 4], [3, 3], [4, 1], [4, 3], [5, 3]]))  # -1
