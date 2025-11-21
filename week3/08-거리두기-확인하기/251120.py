from collections import deque


def solution(places):
    def bfs(sr, sc):
        q = deque()
        visited = set()

        q.append((sr, sc, 0))
        visited.add((sr, sc))

        while q:
            cr, cc, cd = q.pop()

            if cd >= 3:
                continue

            for dr, dc in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
                nr, nc, nd = cr + dr, cc + dc, cd + 1

                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    if grid[nr][nc] == 'P' and nd <= 2:
                        return 0
                    elif grid[nr][nc] == 'O':
                        q.append((nr, nc, nd))

        return 1

    answer = []

    for place in places:
        n = 5
        grid = [list(r) for r in place]

        result = 1
        people = []
        for r in range(n):
            for c in range(n):
                if place[r][c] == 'P':
                    people.append((r, c))

        for pr, pc in people:
            result = bfs(pr, pc)
            if not result:
                break

        answer.append(result)

    return answer


# print(solution(["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"]))  # 1
print(solution(
    [
        ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
        ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
        ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
        ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
        ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]
    ]
))  # [1, 0, 1, 1, 1]

"""
[
    ['P', 'O', 'O', 'O', 'P'],
    ['O', 'X', 'X', 'O', 'X'],
    ['O', 'P', 'X', 'P', 'X'],
    ['O', 'O', 'X', 'O', 'X'],
    ['P', 'O', 'X', 'X', 'P']
]
"""
