class Solution:
    def uniquePaths(self, m, n):
        grid = [[-1] * n for _ in range(m)]

        for r in range(m):
            grid[r][0] = 1
        for c in range(n):
            grid[0][c] = 1

        for r in range(1, m):
            for c in range(1, n):
                grid[r][c] = grid[r - 1][c] + grid[r][c - 1]

        return grid[m - 1][n - 1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.uniquePaths(3, 7))  # 28
    print(solution.uniquePaths(3, 2))  # 3
