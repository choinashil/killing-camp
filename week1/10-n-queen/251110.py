class Solution(object):
    def solveNQueens(self, n):
        def is_valid(row, col):
            for r in range(0, row):
                if board[r][col] == 'Q':
                    return False

            # 좌상
            cur_row, cur_col = row - 1, col - 1
            while cur_row >= 0 and cur_col >= 0:
                if board[cur_row][cur_col] == 'Q':
                    return False
                cur_row, cur_col = cur_row - 1, cur_col - 1

            # 우상
            cur_row, cur_col = row - 1, col + 1
            while cur_row >= 0 and cur_col < n:
                if board[cur_row][cur_col] == 'Q':
                    return False
                cur_row, cur_col = cur_row - 1, cur_col + 1

            return True

        def backtrack(row):
            if row == n:
                answer.append([''.join(row) for row in board])
                return

            for col in range(n):
                if is_valid(row, col):
                    # 1. 선택
                    board[row][col] = 'Q'

                    # 2. 탐색
                    backtrack(row + 1)

                    # 3. 복원
                    board[row][col] = '.'

        answer = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        backtrack(0)
        return answer


if __name__ == '__main__':
    solution = Solution()

    print(solution.solveNQueens(4))
