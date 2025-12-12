class Solution:
    def maximalSquare(self, matrix):
        row_len, col_len = len(matrix), len(matrix[0])
        dp = [[0] * col_len for _ in range(row_len)]
        answer = 0

        for cr in range(0, row_len):
            for cc in range(0, col_len):
                if matrix[cr][cc] == '1':
                    if cr == 0 or cc == 0:
                        dp[cr][cc] = 1
                    else:
                        p1 = dp[cr - 1][cc - 1]
                        p2 = dp[cr - 1][cc]
                        p3 = dp[cr][cc - 1]

                        dp[cr][cc] = min(p1, p2, p3) + 1
                    answer = max(answer, dp[cr][cc])

        return answer * answer


if __name__ == '__main__':
    solution = Solution()
    print(solution.maximalSquare([
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]))  # 4
    print(solution.maximalSquare([
        ["0", "1"],
        ["1", "0"]
    ]))  # 1
    print(solution.maximalSquare([
        ["0"]
    ]))  # 0
