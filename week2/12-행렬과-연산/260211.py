from collections import deque


def solution(grid, operations):
    row_len = len(grid)
    col_len = len(grid[0])

    left_q = deque()
    mid_q = deque()
    right_q = deque()

    for r in range(row_len):
        inner_q = deque()
        for c in range(col_len):
            if c == 0:
                left_q.append(grid[r][c])
            elif c == col_len - 1:
                right_q.append(grid[r][c])
            else:
                inner_q.append(grid[r][c])
        mid_q.append(inner_q)

    for op in operations:
        if op == 'Rotate':
            mid_q[0].appendleft(left_q.popleft())
            right_q.appendleft(mid_q[0].pop())
            mid_q[-1].append(right_q.pop())
            left_q.append(mid_q[-1].popleft())
        else:
            left_q.rotate()
            mid_q.rotate()
            right_q.rotate()

    result = [[0] * col_len for _ in range(row_len)]
    for r in range(row_len):
        for c in range(col_len):
            if c == 0:
                result[r][c] = left_q[r]
            elif c == col_len - 1:
                result[r][c] = right_q[r]
            else:
                result[r][c] = mid_q[r][c - 1]

    return result


print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], ["Rotate", "ShiftRow"]))
