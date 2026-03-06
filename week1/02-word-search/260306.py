class Solution:
    def exist(self, board, word):
        row_len, col_len = len(board), len(board[0])

        def backtrack(r, c, index):
            if word[:index + 1] == word:
                return True

            dr = [-1, 0, 1, 0]
            dc = [0, 1, 0, -1]

            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]

                if 0 <= nr < row_len and 0 <= nc < col_len and board[nr][nc] == word[index + 1]:
                    temp = board[nr][nc]
                    board[nr][nc] = '.'

                    if backtrack(nr, nc, index + 1):
                        return True

                    board[nr][nc] = temp

        for r in range(row_len):
            for c in range(col_len):
                if board[r][c] == word[0]:
                    temp = board[r][c]
                    board[r][c] = '.'

                    if backtrack(r, c, 0):
                        return True
                    else:
                        board[r][c] = temp

        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.exist([['A', 'C'], ['B', 'C']], 'AB'))  # True
    print(solution.exist([
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]
    ], 'ABA'))  # False
    print(solution.exist([
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]
    ], 'ABCCED'))  # True
    print(solution.exist([
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]
    ], 'SEE'))  # True
    print(solution.exist([
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]
    ], 'ABCB'))  # False
