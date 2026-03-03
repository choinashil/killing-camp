from collections import deque


class Solution:
    def numIslands(self, grid):
        row_len, col_len = len(grid), len(grid[0])
        answer = 0

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            grid[r][c] = '0'

            dr = [-1, 0, 1, 0]
            dc = [0, 1, 0, -1]

            while q:
                cur_r, cur_c = q.popleft()

                for i in range(4):
                    next_r, next_c = cur_r + dr[i], cur_c + dc[i]

                    if 0 <= next_r < row_len and 0 <= next_c < col_len and grid[next_r][next_c] == '1':
                        q.append((next_r, next_c))
                        grid[next_r][next_c] = '0'

        for r in range(row_len):
            for c in range(col_len):
                if grid[r][c] == '1':
                    answer += 1
                    bfs(r, c)

        return answer


O(m * n)

if __name__ == '__main__':
    solution = Solution()
    print(solution.numIslands([
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]))
