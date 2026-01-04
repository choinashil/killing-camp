def solution(relation):
    def backtrack(cur, start, length):
        if len(cur) == length:
            vals = set()
            for row in range(len(relation)):
                val = []
                for col in cur:
                    val.append(relation[row][col])
                vals.add(tuple(val))

            if len(vals) == len(relation):
                valid = True
                for c in candidates:
                    if c.issubset(set(cur)):
                        valid = False
                        break

                if valid:
                    candidates.append(set(cur))
                    return True

        for i in range(start, len(relation[0])):
            if len(cur) < length:
                cur.append(i)
                result = backtrack(cur, i + 1, length)
                if result:
                    cur.pop()

        return True

    candidates = []
    for i in range(1, len(relation[0]) + 1):
        backtrack([], 0, i)
    return len(candidates)


print(solution([
    ["100", "ryan", "music", "2"],
    ["200", "apeach", "math", "2"],
    ["300", "tube", "computer", "3"],
    ["400", "con", "computer", "4"],
    ["500", "muzi", "music", "3"],
    ["600", "apeach", "music", "2"]
]))  # 2
print(solution([
    ['a', 'a', 'c'],
    ['b', 'a', 'd']
]))  # 3
