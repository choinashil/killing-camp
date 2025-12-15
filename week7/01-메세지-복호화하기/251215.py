def solution(m, k):
    answer = ''
    pointer = 0

    for char in m:
        if pointer < len(k):
            if char == k[pointer]:
                pointer += 1
            else:
                answer += char
        else:
            answer += char

    return answer


print(solution("kkaxbycyz", "abc"))
print(solution("acbbcdc", "abc"))
