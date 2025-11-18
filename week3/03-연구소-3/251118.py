from collections import deque
import copy
import sys
from io import StringIO

case_1 = """3 1
2 0 1
0 0 0
0 1 2"""

case_2 = """7 3
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 2 0 1 1
0 1 0 0 0 0 0
2 1 0 0 0 0 2"""

case_3 = """7 3
2 0 2 0 1 1 0
0 0 1 0 1 2 0
0 1 1 2 1 0 0
2 1 0 0 0 0 2
0 0 0 2 0 1 1
0 1 0 0 0 0 0
2 1 0 0 2 0 2"""

case_4 = """7 5
2 0 2 0 1 1 0
0 0 1 0 1 2 0
0 1 1 2 1 0 0
2 1 0 0 0 0 2
0 0 0 2 0 1 1
0 1 0 0 0 0 0
2 1 0 0 2 0 2"""

case_5 = """7 2
2 0 2 0 1 1 0
0 0 1 0 1 0 0
0 1 1 1 1 0 0
2 1 0 0 0 0 2
1 0 0 0 0 1 1
0 1 0 0 0 0 0
2 1 0 0 2 0 2"""

case_6 = """5 1
2 2 2 1 1
2 1 1 1 1
2 1 1 1 1
2 1 1 1 1
2 2 2 1 1"""

# sys.stdin = StringIO(case_1)
sys.stdin = StringIO(case_2)  # 4
# sys.stdin = StringIO(case_3) # 4
# sys.stdin = StringIO(case_4) # 3
# sys.stdin = StringIO(case_5) # -1
# sys.stdin = StringIO(case_6) # 0


# ------------------------------------------------


n, active = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

viruses = []

for r in range(n):
    for c in range(n):
        if grid[r][c] == 2:
            viruses.append((r, c))

cases = []


def combination(cur, start):
    if len(cur) == active:
        cases.append(cur[:])

    for i in range(start, len(viruses)):
        cur.append(i)
        combination(cur, i + 1)
        cur.pop()


combination([], 0)

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

total_result = []
answer = 999999

for case in cases:
    copied_grid = copy.deepcopy(grid)

    for r in range(n):
        for c in range(n):
            if grid[r][c] == 0:
                copied_grid[r][c] = -1
            elif grid[r][c] == 1:
                copied_grid[r][c] = '-'
            elif grid[r][c] == 2:
                copied_grid[r][c] = '*'

    q = deque()
    time = 0
    result = True

    for virus in case:
        vr, vc = viruses[virus]
        copied_grid[vr][vc] = 0
        q.append((vr, vc, 0))

    while q:
        r, c, t = q.popleft()

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if 0 <= nr < n and 0 <= nc < n:
                if copied_grid[nr][nc] == -1:
                    copied_grid[nr][nc] = t + 1
                    q.append((nr, nc, t + 1))
                    time = max(time, t + 1)
                elif copied_grid[nr][nc] == '*':
                    copied_grid[nr][nc] = t + 1
                    q.append((nr, nc, t + 1))

    for r in range(n):
        for c in range(n):
            if copied_grid[r][c] == -1:
                result = False

    if result:
        answer = min(answer, time)

print(answer if answer != 999999 else -1)
