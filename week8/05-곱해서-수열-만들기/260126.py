from heapq import heappush, heappop


def solution(n):
    pq = []
    nums = [2]

    pq.append((6, 2, 3))

    while len(nums) < n:
        v, l, r = heappop(pq)
        if nums[-1] != v:
            nums.append(v)

        if r - l == 1:
            # 연속하는 수 2개인 경우
            # 왼쪽 확장
            if l > 1:
                heappush(pq, (v * (l - 1), l - 1, r))

            # 오른쪽 이동
            heappush(pq, ((l + 1) * (r + 1), l + 1, r + 1))
        else:
            # 연속하는 수 3개 이상인 경우
            # 왼쪽 확장
            if l > 1:
                heappush(pq, (v * (l - 1), l - 1, r))

    return nums[-1]


print(solution(1))  # 2
print(solution(2))  # 6
print(solution(3))  # 12
print(solution(4))  # 20
print(solution(5))  # 24
print(solution(6))  # 30
print(solution(7))  # 42
print(solution(8))  # 56
print(solution(9))  # 60
print(solution(10))  # 72
print(solution(15))  # 156
print(solution(30))  # 600
print(solution(50))  # 1640
print(solution(80))  # 4032
print(solution(100))  # 6320
