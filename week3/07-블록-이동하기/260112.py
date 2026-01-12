from collections import deque


def solution(board):
    n = len(board)

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    q = deque()
    visited = set()

    q.append((0, 0, 0, 1, 0))
    visited.add((0, 0, 0, 1))
    visited.add((0, 1, 0, 0))

    def is_valid(r, c):
        if 0 <= r < n and 0 <= c < n:
            return board[r][c] == 0
        return False

    while q:
        r1, c1, r2, c2, t = q.popleft()
        print('현재 위치:', '(', r1, c1, '), (', r2, c2, ')', '시간:', t)

        if (r1 == n - 1 and c1 == n - 1) or (r2 == n - 1 and c2 == n - 1):
            return t

        # 상하좌우 이동
        for i in range(4):
            nr1, nc1, nr2, nc2 = r1 + dr[i], c1 + dc[i], r2 + dr[i], c2 + dc[i]

            if is_valid(nr1, nc1) and is_valid(nr2, nc2) and (nr1, nc1, nr2, nc2) not in visited and (nr2, nc2, nr1, nc1) not in visited:
                q.append((nr1, nc1, nr2, nc2, t + 1))
                visited.add((nr1, nc1, nr2, nc2))
                visited.add((nr2, nc2, nr1, nc1))

        # 가로 방향인 경우
        if r1 == r2:
            # 위로 회전
            # 왼쪽 좌표 기준으로 위로 회전 -> 현재 두 좌표 기준 위 두 칸 확인
            nr1, nc1, nr2, nc2 = r1 - 1, c1, r1, c1

            if is_valid(r1 - 1, c1) and is_valid(r2 - 1, c2) and (nr1, nc1, nr2, nc2) not in visited and (nr2, nc2, nr1, nc1) not in visited:
                q.append((nr1, nc1, nr2, nc2, t + 1))
                visited.add((nr1, nc1, nr2, nc2))
                visited.add((nr2, nc2, nr1, nc1))

            # 오른쪽 좌표 기준으로 위로 회전 -> 현재 두 좌표 기준 위 두 칸 확인
            nr1, nc1, nr2, nc2 = r2 - 1, c2, r2, c2

            if is_valid(r1 - 1, c1) and is_valid(r2 - 1, c2) and (nr1, nc1, nr2, nc2) not in visited and (nr2, nc2, nr1, nc1) not in visited:
                q.append((nr1, nc1, nr2, nc2, t + 1))
                visited.add((nr1, nc1, nr2, nc2))
                visited.add((nr2, nc2, nr1, nc1))

            # 아래로 회전
            # 왼쪽 좌표 기준으로 아래로 회전 -> 현재 두 좌표 기준 아래 두 칸 확인
            nr1, nc1, nr2, nc2 = r1 + 1, c1, r1, c1

            if is_valid(r1 + 1, c1) and is_valid(r2 + 1, c2) and (nr1, nc1, nr2, nc2) not in visited and (nr2, nc2, nr1, nc1) not in visited:
                q.append((nr1, nc1, nr2, nc2, t + 1))
                visited.add((nr1, nc1, nr2, nc2))
                visited.add((nr2, nc2, nr1, nc1))

            # 오른쪽 좌표 기준으로 아래로 회전 -> 현재 두 좌표 기준 아래 두 칸 확인
            nr1, nc1, nr2, nc2 = r2 + 1, c2, r2, c2

            if is_valid(r1 + 1, c1) and is_valid(r2 + 1, c2) and (nr1, nc1, nr2, nc2) not in visited and (nr2, nc2, nr1, nc1) not in visited:
                q.append((nr1, nc1, nr2, nc2, t + 1))
                visited.add((nr1, nc1, nr2, nc2))
                visited.add((nr2, nc2, nr1, nc1))

        # 세로 방향인 경우
        else:
            # 왼쪽으로 회전
            # 위쪽 좌표 기준으로 왼쪽으로 회전 -> 현재 두 좌표 기준 왼쪽 두 칸 확인
            nr1, nc1, nr2, nc2 = r1, c1 - 1, r1, c1

            if is_valid(r1, c1 - 1) and is_valid(r2, c2 - 1) and (nr1, nc1, nr2, nc2) not in visited and (nr2, nc2, nr1, nc1) not in visited:
                q.append((nr1, nc1, nr2, nc2, t + 1))
                visited.add((nr1, nc1, nr2, nc2))
                visited.add((nr2, nc2, nr1, nc1))

            # 아래쪽 좌표 기준으로 왼쪽으로 회전 -> 현재 두 좌표 기준 왼쪽 두 칸 확인
            nr1, nc1, nr2, nc2 = r2, c2 - 1, r2, c2

            if is_valid(r1, c1 - 1) and is_valid(r2, c2 - 1) and (nr1, nc1, nr2, nc2) not in visited and (nr2, nc2, nr1, nc1) not in visited:
                q.append((nr1, nc1, nr2, nc2, t + 1))
                visited.add((nr1, nc1, nr2, nc2))
                visited.add((nr2, nc2, nr1, nc1))

            # 오른쪽으로 회전
            # 위쪽 좌표 기준으로 오른쪽으로 회전 -> 현재 두 좌표 기준 오른쪽 두 칸 확인
            nr1, nc1, nr2, nc2 = r1, c1 + 1, r1, c1

            if is_valid(r1, c1 + 1) and is_valid(r2, c2 + 1) and (nr1, nc1, nr2, nc2) not in visited and (nr2, nc2, nr1, nc1) not in visited:
                q.append((nr1, nc1, nr2, nc2, t + 1))
                visited.add((nr1, nc1, nr2, nc2))
                visited.add((nr2, nc2, nr1, nc1))

            # 아래쪽 좌표 기준으로 오른쪽으로 회전 -> 현재 두 좌표 기준 오른쪽 두 칸 확인
            nr1, nc1, nr2, nc2 = r2, c2 + 1, r2, c2

            if is_valid(r1, c1 + 1) and is_valid(r2, c2 + 1) and (nr1, nc1, nr2, nc2) not in visited and (nr2, nc2, nr1, nc1) not in visited:
                q.append((nr1, nc1, nr2, nc2, t + 1))
                visited.add((nr1, nc1, nr2, nc2))
                visited.add((nr2, nc2, nr1, nc1))


print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))  # 7
