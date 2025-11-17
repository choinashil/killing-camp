from collections import deque

def solution(cacheSize, cities):
    answer = 0
    q = deque()

    for c in cities:
        city = c.lower()
        if city in q:
            q2 = deque()
            while q:
                deleted_city = q.popleft()
                if deleted_city != city:
                    q2.append(deleted_city)
            q2.append(city)
            q = q2
            answer += 1
        else:
            if len(q) < cacheSize:
                q.append(city)
            else:
                if q:
                    deleted_city = q.popleft()
                    q.append(city)
            answer += 5

    return answer

print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"])) # 50
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"])) # 21
print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"])) # 60
print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"])) # 52
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"])) # 16
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"])) # 25
print(solution(0, ['a', 'b', 'c'])) # 15
print(solution(1, ['a', 'b', 'a'])) # 15
print(solution(1, ['a', 'b', 'b'] )) # 11
print(solution(2, [] )) # 0
print(solution(10, ['a', 'b', 'b', 'b', 'a'] )) # 13
print(solution(2, ['a', 'b', 'a', 'c']))
print(solution(2, ['a', 'b', 'b', 'c']))
