from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)
        q = deque()

        if grid[0][0] == 0:
            q.append((0, 0, 1))
            grid[0][0] = 1

        dr = [0, 1, 1, 1, 0, -1, -1, -1]
        dc = [1, 1, 0, -1, -1, -1, 0, 1]

        while q:
            cur_r, cur_c, cur_count = q.popleft()

            if cur_r == n - 1 and cur_c == n - 1:
                return cur_count

            for i in range(8):
                next_r, next_c = cur_r + dr[i], cur_c + dc[i]

                if 0 <= next_r < n and 0 <= next_c < n and grid[next_r][next_c] == 0:
                    q.append((next_r, next_c, cur_count + 1))
                    grid[next_r][next_c] = 1

        return -1
