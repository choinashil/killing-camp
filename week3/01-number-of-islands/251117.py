from collections import deque


class Solution:
    def numIslands(self, grid):
        row_len = len(grid)
        col_len = len(grid[0])

        q = deque()
        visited = [[False for _ in range(col_len)] for _ in range(row_len)]

        answer = 0

        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]

        def in_range(r, c):
            return 0 <= r < row_len and 0 <= c < col_len

        def bfs(sc, sr):
            q.append((sc, sr))
            visited[sc][sr] = True

            while q:
                r, c = q.popleft()

                # 네 방향 탐색
                for i in range(4):
                    nr, nc = r + dr[i], c + dc[i]

                    if in_range(nr, nc) and grid[nr][nc] == '1' and not visited[nr][nc]:
                        q.append((nr, nc))
                        visited[nr][nc] = True

        for r in range(row_len):
            for c in range(col_len):
                if grid[r][c] == '1' and not visited[r][c]:
                    bfs(r, c)
                    answer += 1

        return answer


if __name__ == "__main__":
    solution = Solution()
    print(solution.numIslands([  # 1
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]))
    print(solution.numIslands([  # 3
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]))
    print(solution.numIslands([  # 3
        ["0", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]))
