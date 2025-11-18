import copy
from collections import deque

row_len, col_len = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(row_len)]


def combination(n, k):
    def backtrack(cur, start):
        if len(cur) == k:
            result.append(cur[:])
            return

        for i in range(start, n):
            cur.append(i)
            backtrack(cur, i + 1)
            cur.pop()

    result = []
    backtrack([], 0)
    return result


spaces = []
viruses = []

for r in range(row_len):
    for c in range(col_len):
        if grid[r][c] == 0:
            spaces.append((r, c))
        if grid[r][c] == 2:
            viruses.append((r, c))

# 1. 벽 세울 수 있는 조합 계산
cases = combination(len(spaces), 3)

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

max_safe_area = 0

for case in cases:
    q = deque(viruses)
    copied_grid = copy.deepcopy(grid)

    # 1. 벽 세우기
    for wr, wc in case:
        copied_grid[wr][wc] = 1

    # 2. 바이러스 퍼뜨리기
    while q:
        r, c = q.popleft()

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if 0 <= nr < row_len and 0 <= nc < col_len and copied_grid[nr][nc] == 0:
                q.append((nr, nc))
                copied_grid[r][c] = 2

    # 3. 안전 영역 계산
    safe_area = 0

    for r in range(row_len):
        for c in range(col_len):
            if copied_grid[r][c] == 0:
                safe_area += 1

    max_safe_area = max(max_safe_area, safe_area)

print(max_safe_area)


# print(solution(3, 3, [
# 	[2,0,1],
# 	[1,0,0],
# 	[0,2,0]
# ]))
