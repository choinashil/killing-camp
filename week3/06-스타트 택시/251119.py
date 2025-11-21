# autopep8: off
import sys
from io import StringIO

case_1 = """6 3 15
0 0 1 0 0 0
0 0 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 1 0
0 0 0 1 0 0
6 5
2 2 5 6
5 4 1 6
4 2 3 5"""

case_2 = """7 7
#######
#...RB#
#.#####
#.....#
#####.#
#O....#
#######"""

case_3 = """7 7
#######
#..R#B#
#.#####
#.....#
#####.#
#O....#
#######"""

case_4 = """10 10
##########
#R#...##B#
#...#.##.#
#####.##.#
#......#.#
#.######.#
#.#....#.#
#.#.#.#..#
#...#.O#.#
##########"""

case_5 = """3 7
#######
#R.O.B#
#######"""

case_6 = """10 10
##########
#R#...##B#
#...#.##.#
#####.##.#
#......#.#
#.######.#
#.#....#.#
#.#.##...#
#O..#....#
##########"""

case_7 = """3 10
##########
#.O....RB#
##########"""

sys.stdin = StringIO(case_1)  # 14
# sys.stdin = StringIO(case_2)  # 1
# sys.stdin = StringIO(case_3)  # 1
# sys.stdin = StringIO(case_4)  # 0
# sys.stdin = StringIO(case_5)  # 1
# sys.stdin = StringIO(case_6)  # 1
# sys.stdin = StringIO(case_7)  # 0

# ------------------------------------------------
from collections import deque

n, m, f = map(int, input().split())
print(n, m, f)

grid = [list(map(int, input().split())) for _ in range(n)]
print(grid)

sr, sc = map(lambda x: int(x) - 1, input().split())
print(sr, sc)

passengers = [[int(x) - 1 for x in input().split()] for _ in range(m)]
print(passengers)

p_pos = set()

for p in passengers:
    p_pos.add((p[0], p[1]))

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def find_target(r, c):
    for p in passengers:
        if p[0] == r and p[1] == c:
            return p[2], p[3]


def in_range(r, c):
    return 0 <= r < n and 0 <= c < n


def is_valid(r, c):
    return grid[r][c] == 0


def find_passenger(sr, sc, sf):
    q = deque()
    visited = set()

    q.append((sr, sc, sf))
    visited.add((sr, sc))

    while q:
        r, c, f = q.popleft()

        if (r, c) in p_pos:
            return r, c, f

        # 연료 없을 때 처리
        if f == 0:
            # 실패
            return r, c, f

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if in_range(nr, nc) and is_valid(nr, nc) and (nr, nc) not in visited:
                q.append((nr, nc, f - 1))
                visited.add((nr, nc))


def go_to_target(sr, sc, tr, tc, sf):
    q = deque()
    visited = set()

    q.append((sr, sc, sf, 0))
    visited.add((sr, sc))

    while q:
        r, c, f, l = q.popleft()

        if r == tr and c == tc:
            # 목적지 도착
            f += l * 2
            return r, c, f

        if f == 0:
            # 실패
            return r, c, f

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if in_range(nr, nc) and is_valid(nr, nc) and (nr, nc) not in visited:
                q.append((nr, nc, f - 1, l + 1))
                visited.add((nr, nc))


r, c = sr, sc

for i in range(m):
    # 1. 승객 찾기
    r, c, f = find_passenger(r, c, f)
    print(i, '번째 승객 발견', r, c, f)
    p_pos.remove((r, c))

    if f == 0:
        print(-1)

    # 2. 목적지 가기
    tr, tc = find_target(r, c)
    r, c, f = go_to_target(r, c, tr, tc, f)
    print(i, '번째 승객 목적지 도착', r, c, f)

    if f == 0:
        print(-1)

    if i == m - 1:
        print(f)
