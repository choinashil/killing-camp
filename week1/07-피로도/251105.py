def solution(k, dungeons):
    def backtrack(cur_k, count):
        nonlocal answer
        answer = max(answer, count)

        for i in range(n):
            if not visited[i] and cur_k >= dungeons[i][0]:
                visited[i] = True
                backtrack(cur_k - dungeons[i][1], count + 1)
                visited[i] = False

    answer = 0
    n = len(dungeons)
    visited = [False] * n
    backtrack(k, 0)
    return answer

print(solution(80, [[80,20],[50,40],[30,10]]))
print(solution(80, [[50,40],[30,10],[80,20]]))
print(solution(80, [[30,10],[50,40],[80,20]]))
print(solution(80, [[100,20],[120,40],[150,10]]))