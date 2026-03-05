from collections import deque


class Solution:
    def updateBoard(self, board, click):
        row_len = len(board)
        col_len = len(board[0])

        q = deque()
        q.append(tuple(click))

        # 왼쪽 위부터 시계방향
        dr = [-1, -1, -1, 0, 1, 1, 1, 0]
        dc = [-1, 0, 1, 1, 1, 0, -1, -1]

        while q:
            r, c = q.popleft()

            if board[r][c] == 'M':
                board[r][c] = 'X'
                return board

            count = 0

            for i in range(8):
                nr, nc = r + dr[i], c + dc[i]

                if 0 <= nr < row_len and 0 <= nc < col_len:
                    if board[nr][nc] == 'M':
                        count += 1

            # 주변에 지뢰 없을 때만 인접한 셀들 큐에 넣기
            if not count:
                for i in range(8):
                    nr, nc = r + dr[i], c + dc[i]

                    if 0 <= nr < row_len and 0 <= nc < col_len:
                        if board[nr][nc] == 'E':
                            q.append((nr, nc))
                            board[nr][nc] = 'V'  # visited

            board[r][c] = str(count) if count else 'B'

        return board
