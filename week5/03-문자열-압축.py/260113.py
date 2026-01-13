def solution(s):
    answer = len(s)

    for l in range(1, len(s) // 2 + 1):
        count = 1
        compacted = ''
        for i in range(0, len(s), l):
            prev = s[i:i + l]
            cur = s[i + l:i + 2 * l]

            if prev == cur:
                count += 1
            else:
                if count > 1:
                    compacted += str(count)
                compacted += prev
                count = 1

        answer = min(answer, len(compacted))
    return answer


print(solution("aabbaccc"))  # 7 2a2ba3c
print(solution("ababcdcdababcdcd"))  # 9 2ababcdcd
print(solution("abcabcdede"))  # 8 3abcdede
print(solution("abcabcabcabcdededededede"))  # 14
print(solution("xababcdcdababcdcd"))  # 17
