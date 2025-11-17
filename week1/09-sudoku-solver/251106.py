class Solution(object):
    def solveSudoku(self, board):
        def validate_num(cur_r, cur_c, num):
            for row in range(9):
                if row != cur_r and board[row][cur_c] == num:
                    return False
            
            for col in range(9):
                if col != cur_c and board[cur_r][col] == num:
                    return False

            start_r = cur_r // 3 * 3
            start_c = cur_c // 3 * 3

            for row in range(start_r, start_r + 3):
                for col in range(start_c, start_c + 3):
                    if (row != cur_r or col != cur_c) and board[row][col] == num:
                        return False

            return True

        def backtrack(r, c):
            # 1. 종료 조건: 마지막 행을 넘어감
            if r == 9:
                return True # 성공

            # 2. 다음 위치 계산 (get_next_pos 대체)
            next_r = r + 1 if c == 8 else r 
            next_c = 0 if c == 8 else c + 1

            # 3. 현재 칸이 이미 채워진 경우
            if board[r][c] != '.':         
                # 위치 계산하지 않고 바로 다음 칸으로 이동       
                return backtrack(next_r, next_c)
            
            # 2. 현재 칸이 빈 칸인 경우 
            for n in range(1, 10):
                if validate_num(r, c, str(n)):
                    board[r][c] = str(n)
                    
                    # 탐색 (+반환값 체크)
                    if backtrack(next_r, next_c):
                        return True 
                    
                    # 복원
                    board[r][c] = '.'
            
            # 모든 케이스 실패
            return False
        
        # (0,0)에서 한 번만 시작
        backtrack(0, 0)
        return board

    
if __name__ == '__main__':
    solution = Solution()
    
    print(solution.solveSudoku([
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]))