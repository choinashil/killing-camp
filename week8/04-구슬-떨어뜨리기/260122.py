from collections import deque


def solution(drum):
    n = len(drum)
    answer = 0
    dp = [[-1] * n for _ in range(n)]

    for start_col in range(n):
        q = deque()

        count = 0
        row = 0
        col = start_col

        while row < n:
            cur_v = drum[row][col]

            if dp[row][col] != -1:
                count += dp[row][col]
                break

            q.append((row, col, cur_v))

            if cur_v == '#':
                row += 1
            elif cur_v == '>':
                col += 1
            elif cur_v == '<':
                col -= 1
            elif cur_v == '*':
                row += 1
                count += 1

        if count < 2:
            answer += 1

        while q:
            row, col, cur_v = q.popleft()
            dp[row][col] = count
            if cur_v == '*':
                count -= 1

    return answer


print(solution([
    '*##<',
    '#<*#',
    '#>#>',
    '*##*'
]))  # 2
print(solution([
    '###<',
    '*<*#',
    '#>#>',
    '*##*'
]))  # 2
print(solution([
    '>>>#',
    '#<<<',
    '>>>#',
    '#<<<'
]))  # 4
print(solution([
    '######',
    '>#*###',
    '####*#',
    '#<#>>#',
    '>#*#*<',
    '######'
]))  # 4
