from collections import defaultdict, deque
from heapq import heappop, heappush

# 다익스트라


def solution2(n, passenger, train):
    graph = defaultdict(list)
    for u, v in train:
        graph[u].append(v)

    max_p = [0] * n

    pq = []
    heappush(pq, (-passenger[0], -1))
    while pq:
        tmp_p, tmp_v = heappop(pq)
        cur_p, cur_v = -tmp_p, -tmp_v

        max_p[cur_v - 1] = max(max_p[cur_v - 1], cur_p)

        for next_v in graph[cur_v]:
            next_p = cur_p + passenger[next_v - 1]
            if max_p[next_v - 1] < next_p:
                max_p[next_v - 1] = next_p
                heappush(pq, (-next_p, -next_v))

    answer = [n, 0]

    for i in range(len(max_p), 0, -1):
        if answer[1] < max_p[i - 1]:
            answer[0] = i
            answer[1] = max_p[i - 1]

    return answer


# BFS
def solution(n, passenger, train):
    graph = defaultdict(list)
    for u, v in train:
        graph[u].append(v)

    max_p = [0] * n

    q = deque()
    q.append((1, passenger[0]))
    max_p[0] = passenger[0]

    while q:
        cur_v, cur_p = q.popleft()

        for next_v in graph[cur_v]:
            next_p = cur_p + passenger[next_v - 1]
            if max_p[next_v - 1] == 0:
                max_p[next_v - 1] = next_p
                q.append((next_v, next_p))

        answer = [n, 0]

    for i in range(len(max_p), 0, -1):
        if answer[1] < max_p[i - 1]:
            answer[0] = i
            answer[1] = max_p[i - 1]

    return answer


print(solution(6, [1, 1, 1, 1, 1, 1], [[1, 2], [1, 3], [1, 4], [3, 5], [3, 6]]))  # [6,3]
print(solution(4, [2, 1, 2, 2], [[1, 2], [1, 3], [2, 4]]))  # [4,5]
print(solution(5, [1, 1, 2, 3, 4], [[1, 2], [1, 3], [1, 4], [1, 5]]))  # [5,5]
