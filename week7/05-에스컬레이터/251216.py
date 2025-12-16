def solution(n, escalator):
    INF = float('inf')
    dp = [[INF] * 3 for _ in range(n)]

    for col in range(3):
        if escalator[0][col] == 0:
            if col == 1:
                dp[0][col] = 0
            else:
                dp[0][col] = 1

    for row in range(1, n):
        for col in range(3):
            if escalator[row][col] == 0:
                dp[row][col] = min(
                    dp[row - 1][0] + col,
                    dp[row - 1][1] + abs(1 - col),
                    dp[row - 1][2] + abs(2 - col)
                )

    return min(dp[n - 1])


print(solution(5, [
    [0, 1, 0],
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
    [0, 1, 0]
]))  # 3
print(solution(5, [
    [0, 0, 1],
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
    [0, 1, 0]
]))  # 1
print(solution(7, [
    [0, 1, 1],
    [1, 0, 0],
    [0, 0, 1],
    [1, 1, 0],
    [0, 1, 0],
    [1, 0, 1],
    [1, 1, 0],
]))  # 5
print(solution(1, [
    [0, 0, 0]
]))  # 0
print(solution(1, [
    [0, 1, 0]
]))  # 1
