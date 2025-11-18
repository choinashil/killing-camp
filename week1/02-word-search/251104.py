class Solution(object):
    def exist(self, board, word):
        def in_range(x, y):
            if x >= 0 and x < row_len and y >= 0 and y < col_len:
                return True
            return False

        def backtrack(r, c, i):
            if not visited[r][c] and word[i] == board[r][c]:
                if i == len(word) - 1:
                    return True

                visited[r][c] = True

                for x, y in directions:
                    next_r, next_c = r + x, c + y
                    if in_range(next_r, next_c):
                        if backtrack(next_r, next_c, i + 1):
                            return True

                visited[r][c] = False

                return False

        row_len, col_len = len(board), len(board[0])
        visited = [[False for _ in range(col_len)] for _ in range(row_len)]
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        for r in range(row_len):
            for c in range(col_len):
                if backtrack(r, c, 0):
                    return True

        return False


if __name__ == '__main__':
    solution = Solution()

    print(solution.exist([
        ["A", "B", "C", "D"],
        ["B", "B", "D", "E"],
        ["D", "C", "B", "A"]
    ], "ABCDE"))

    print(solution.exist([
        ["A", "B", "C", "D"],
        ["B", "B", "D", "F"],
        ["D", "C", "E", "A"]
    ], "ABCDE"))

    print(solution.exist([
        ["A", "B", "C", "D"],
        ["C", "E", "B", "A"],
        ["B", "D", "C", "B"]
    ], "ABCDE"))

    print(solution.exist([
        ["B", "B", "B", "C"],
        ["A", "B", "B", "D"],
        ["B", "C", "C", "D"]
    ], "ABBCD"))

    print(solution.exist([
        ["A", "B", "C", "D"],
        ["B", "C", "D", "D"],
        ["C", "D", "C", "E"]
    ], "ABCDE"))
