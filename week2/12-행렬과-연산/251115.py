from collections import deque 

def solution(grid, operations):  
    row_len = len(grid)
    col_len = len(grid[0])

    left_col = deque([grid[r][0] for r in range(row_len)])
    right_col = deque([grid[r][col_len - 1] for r in range(row_len)])
    rows = deque([deque(grid[r][1:col_len - 1]) for r in range(row_len)])

    def shift_row(left_col, right_col, rows):
        left_col.rotate(1)
        right_col.rotate(1)
        rows.rotate(1)
        return left_col, right_col, rows

    def rotate(left_col, right_col, rows):
        temp = left_col.popleft()
        rows[0].appendleft(temp)
        temp = rows[0].pop()
        right_col.appendleft(temp)
        temp = right_col.pop()
        rows[row_len - 1].append(temp)
        temp = rows[row_len - 1].popleft()
        left_col.append(temp)
        return left_col, right_col, rows


    for op in operations:
        if op == 'ShiftRow':
            left_col, right_col, rows = shift_row(left_col, right_col, rows)
        else:
            left_col, right_col, rows = rotate(left_col, right_col, rows)

    answer = [[-1 for _ in range(col_len)] for _ in range(row_len)]

    for r in range(row_len):
        answer[r][0] = left_col[r]
        answer[r][col_len - 1] = right_col[r]

        for c in range(len(rows[0])):
            answer[r][c + 1] = rows[r][c]
    
    return answer

print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], ["ShiftRow", "Rotate"]))
print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], ["Rotate", "ShiftRow"]))
print(solution([[8, 6, 3], [3, 3, 7], [8, 4, 9]], ["Rotate", "ShiftRow", "ShiftRow"]))
print(solution([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], ["ShiftRow", "Rotate", "ShiftRow", "Rotate"]))
