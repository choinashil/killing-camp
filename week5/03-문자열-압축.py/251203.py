def solution(s):
    answer = len(s)

    for l in range(1, len(s) // 2 + 1):
        count = 0
        word = ''
        prev = ''
        for i in range(0, len(s), l):
            cur = s[i:i + l]
            if prev == cur:
                count += 1
            else:
                if count > 1:
                    word += str(count)
                word += prev
                prev = cur
                count = 1

        if count > 1:
            word += str(count)
        word += prev

        answer = min(answer, len(word))
    return answer


print(solution("aabbaccc"))  # 7 2a2ba3c
print(solution("ababcdcdababcdcd"))  # 9 2ababcdcd
print(solution("abcabcdede"))  # 8 3abcdede
print(solution("abcabcabcabcdededededede"))  # 14
print(solution("xababcdcdababcdcd"))  # 17
