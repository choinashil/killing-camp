from collections import defaultdict, deque


def solution(n, cars, links):
    tree = defaultdict(list)
    for u, v in links:
        tree[u].append(v)
        tree[v].append(u)

    total = sum(cars)
    answer = float('inf')

    for u, v in links:
        print(u, ',', v, '사이 끊기')
        q = deque()
        visited = set()
        count = 0

        q.append(u)
        visited.add(u)

        while q:
            cur_v = q.popleft()
            count += cars[cur_v - 1]

            for next_v in tree[cur_v]:
                if next_v not in visited and next_v != v:
                    q.append(next_v)
                    visited.add(next_v)
        print('그룹A 주차대수:', count, '그룹B 주차대수:', total - count, '= 차이:', abs(total - count - count))
        answer = min(answer, abs(total - count - count))

    return answer


print(solution(13, [22, 9, 1, 15, 8, 6, 20, 7, 11, 5, 10, 4, 1], [[4, 7], [13, 10], [6, 3], [7, 1], [6, 12], [5, 11], [5, 6], [5, 10], [9, 8], [8, 11], [8, 2], [7, 8]]))  # 5
print(solution(6, [6, 4, 10, 9, 8, 4], [[4, 1], [3, 2], [1, 6], [3, 5], [5, 1]]))  # 3
