from collections import deque


def solution(cacheSize, cities):
    answer = 0
    cache = deque()

    for city in cities:
        formatted_city = city.upper()

        if formatted_city in cache:
            cache.remove(formatted_city)
            answer += 1
        else:
            if cache and len(cache) == cacheSize:
                cache.popleft()
            answer += 5

        if len(cache) < cacheSize:
            cache.append(formatted_city)

    return answer


print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))  # 50
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))  # 21
print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))  # 60
print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))  # 52
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))  # 16
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))  # 25
print(solution(0, ['a', 'b', 'c']))  # 15
print(solution(1, ['a', 'b', 'a']))  # 15
print(solution(1, ['a', 'b', 'b']))  # 11
print(solution(2, []))  # 0
print(solution(10, ['a', 'b', 'b', 'b', 'a']))  # 13
print(solution(2, ['a', 'b', 'a', 'c']))  # 16
print(solution(2, ['a', 'b', 'b', 'c']))  # 16
