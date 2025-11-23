# 일자: 2025-11-23
# 시작: 17:07
# 종료: 17:45

class Solution:
    def solveNQueens(self, n):
        def check_row(board, r, c):
            cur_r = r - 1
            while cur_r >= 0:
                if board[cur_r][c] == 'Q':
                    return False
                cur_r -= 1

            return True

        def check_col(board, r, c):
            cur_c = c - 1
            while cur_c >= 0:
                if board[r][cur_c] == 'Q':
                    return False
                cur_c -= 1

            return True

        def check_diagonal(board, r, c):
            cur_r = r - 1
            cur_c = c - 1

            while cur_r >= 0 and cur_c >= 0:
                if board[cur_r][cur_c] == 'Q':
                    return False
                cur_r -= 1
                cur_c -= 1

            cur_r = r - 1
            cur_c = c + 1
            while cur_r >= 0 and cur_c < n:
                if board[cur_r][cur_c] == 'Q':
                    return False
                cur_r -= 1
                cur_c += 1

            return True

        def get_next_pos(r, c):
            if c == n - 1:
                return r + 1, 0

            return r, c + 1

        def backtrack(cur_board, start_r, start_c, count):
            if count == n:
                answer.append([''.join(r) for r in board])
                return

            for r in range(start_r, n):
                col = start_c if r == start_r else 0
                for c in range(col, n):
                    if check_row(cur_board, r, c) and check_col(cur_board, r, c) and check_diagonal(cur_board, r, c):
                        cur_board[r][c] = 'Q'
                        count += 1

                        next_r, next_c = get_next_pos(r, c)
                        backtrack(cur_board, next_r, next_c, count)

                        cur_board[r][c] = '.'
                        count -= 1

        board = [['.'] * n for _ in range(n)]
        answer = []
        backtrack(board, 0, 0, 0)
        return answer


if __name__ == '__main__':
    solution = Solution()
    print(solution.solveNQueens(1))
    print(solution.solveNQueens(2))
    print(solution.solveNQueens(3))
    print(solution.solveNQueens(4))
    print(solution.solveNQueens(5))

# board = [['.', 'Q', '.', '.'], ['.', '.', '.', 'Q'], ['Q', '.', '.', '.'], ['.', '.', 'Q', '.']]

# print([''.join(r) for r in board])

# arr = ['.', 'Q', '.', '.']
# print(''.join(arr))
