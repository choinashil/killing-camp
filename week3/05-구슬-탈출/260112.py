from collections import deque

row_len, col_len = map(int, input().split())
board = [list(input()) for _ in range(row_len)]

q = deque()
visited = set()

rr = rc = br = bc = None

for r in range(row_len):
    for c in range(col_len):
        if board[r][c] == 'R':
            rr, rc = r, c
            board[r][c] = '.'

        elif board[r][c] == 'B':
            br, bc = r, c
            board[r][c] = '.'

q.append((rr, rc, br, bc, 1))
visited.add((rr, rc, br, bc))

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def in_range(r, c):
    return 1 <= r < row_len - 1 and 1 <= c < col_len - 1


def is_valid(r, c):
    return board[r][c] == '.' or board[r][c] == 'O'


def bfs(q):
    while q:
        rr, rc, br, bc, count = q.popleft()

        if count > 10:
            continue

        for i in range(4):
            nrr, nrc = rr, rc
            nbr, nbc = br, bc

            while in_range(nrr + dr[i], nrc + dc[i]) and is_valid(nrr + dr[i], nrc + dc[i]):
                nrr += dr[i]
                nrc += dc[i]

                if board[nrr][nrc] == 'O':
                    break  # 구멍에 빠져서 멈춤

            while in_range(nbr + dr[i], nbc + dc[i]) and is_valid(nbr + dr[i], nbc + dc[i]):
                nbr += dr[i]
                nbc += dc[i]

                if board[nbr][nbc] == 'O':
                    break  # 구멍에 빠져서 멈춤

            # 이동 완료 후, 최종 위치 확인
            red_in_hole = (board[nrr][nrc] == 'O')
            blue_in_hole = (board[nbr][nbc] == 'O')

            # 구멍에 빠지지 않았고, 같은 위치일 때 겹치지 않게 위치 조정
            if not red_in_hole and not blue_in_hole:
                if (nrr, nrc) == (nbr, nbc):
                    red_dist = abs(nrr - rr) + abs(nrc - rc)
                    blue_dist = abs(nbr - br) + abs(nbc - bc)

                    if red_dist > blue_dist:
                        nrr -= dr[i]
                        nrc -= dc[i]
                    else:
                        nbr -= dr[i]
                        nbc -= dc[i]

            # 위치 조정 후 성공/실패 판단
            if red_in_hole and not blue_in_hole:
                return 1

            if blue_in_hole:
                continue

            if not red_in_hole and (nrr, nrc, nbr, nbc) not in visited:
                visited.add((nrr, nrc, nbr, nbc))
                q.append((nrr, nrc, nbr, nbc, count + 1))

    return 0


print(bfs(q))
